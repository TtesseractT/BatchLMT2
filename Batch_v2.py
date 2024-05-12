import os
import shutil
import subprocess
import concurrent.futures
import pynvml
import queue
from tqdm import tqdm
import json
import threading

LOG_FILE = 'processing_log.json'
INPUT_DIR = 'Input-Videos'
OUTPUT_DIR = 'Videos'

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        json.dump({"queue": [], "processed": []}, f)

def get_gpu_memory_info():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    pynvml.nvmlShutdown()
    return info.total, info.free

def update_log(action, file_name=None):
    with threading.Lock():
        with open(LOG_FILE, 'r') as f:
            log_data = json.load(f)
        if action == 'enqueue':
            log_data['queue'].append(file_name)
        elif action == 'dequeue':
            log_data['queue'].remove(file_name)
            log_data['processed'].append(file_name)
        with open(LOG_FILE, 'w') as f:
            json.dump(log_data, f)

def process_file(file_to_process, video_folder_name, progress_bar):
    try:
        shutil.move(os.path.join(INPUT_DIR, file_to_process), file_to_process)
        
        # Run Whisper processing
        cmd = f'whisper "{file_to_process}" --device cuda --model large --language en --task transcribe --output_format all'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        new_folder_path = os.path.join(OUTPUT_DIR, video_folder_name)
        os.mkdir(new_folder_path)
        
        shutil.move(file_to_process, new_folder_path)
        
        output_file_base = os.path.splitext(file_to_process)[0]
        for filename in os.listdir('.'):
            if filename.startswith(output_file_base):
                shutil.move(filename, new_folder_path)

        update_log('dequeue', file_to_process)

    except Exception as e:
        if os.path.exists(os.path.join(OUTPUT_DIR, video_folder_name, file_to_process)):
            shutil.move(os.path.join(OUTPUT_DIR, video_folder_name, file_to_process), '.')
        if os.path.exists(os.path.join(OUTPUT_DIR, video_folder_name)):
            shutil.rmtree(os.path.join(OUTPUT_DIR, video_folder_name))
    finally:
        progress_bar.update(1)

def worker(file_queue, progress_bar):
    while not file_queue.empty():
        try:
            file_to_process = file_queue.get_nowait()
        except queue.Empty:
            break

        video_folder_name = f'Video - {file_to_process[1]}'
        process_file(file_to_process[0], video_folder_name, progress_bar)
        file_queue.task_done()

def process_files_LMT2_batch():
    total_memory, free_memory = get_gpu_memory_info()
    vram_per_process = 11.7 * 1024**3
    max_processes = int(free_memory // vram_per_process)

    files_to_process = os.listdir(INPUT_DIR)
    num_files = len(files_to_process)

    file_queue = queue.Queue()
    for i, file_to_process in enumerate(files_to_process, 1):
        file_queue.put((file_to_process, i))
        update_log('enqueue', file_to_process)

    with tqdm(total=num_files, desc="Transcribing files") as progress_bar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_processes) as executor:
            futures = [executor.submit(worker, file_queue, progress_bar) for _ in range(max_processes)]
            concurrent.futures.wait(futures)

def cleanup_filenames():
    for subdir in os.listdir(OUTPUT_DIR):
        subdir_path = os.path.join(OUTPUT_DIR, subdir)
        if os.path.isdir(subdir_path):
            files = os.listdir(subdir_path)
            if files:
                largest_file = max(files, key=lambda f: os.path.getsize(os.path.join(subdir_path, f)))
                new_name = os.path.splitext(largest_file)[0]
                os.rename(subdir_path, os.path.join(OUTPUT_DIR, new_name))

def run_multiple_instances(num_scripts, script_name):
    processes = []
    for _ in range(num_scripts):
        process = subprocess.Popen(["python", script_name], env={**os.environ, "RUN_AS_SUBPROCESS": "1"}, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)

    for process in processes:
        process.wait()

if __name__ == '__main__':
    # Determine how many instances to run based on available VRAM
    total_memory, free_memory = get_gpu_memory_info()
    vram_per_process = 11.7 * 1024**3
    num_instances = int(free_memory // vram_per_process)

    script_name = os.path.basename(__file__)

    if os.getenv('RUN_AS_SUBPROCESS') == '1':
        process_files_LMT2_batch()
        cleanup_filenames()
    else:
        run_multiple_instances(num_instances, script_name)
