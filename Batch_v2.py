import os
import shutil
import subprocess
import concurrent.futures
import pynvml
import queue

def get_gpu_memory_info():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    pynvml.nvmlShutdown()
    return info.total, info.free

def transcribe_audio(file_to_process):
    import torch
    from transformers import WhisperProcessor, WhisperForConditionalGeneration

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load model and processor
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2").to(device)
    processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")

    # Prepare inputs
    inputs = processor(file_to_process, return_tensors="pt").to(device)

    # Perform mixed precision inference
    with torch.cuda.amp.autocast():
        with torch.no_grad():
            generated_ids = model.generate(inputs.input_ids)

    # Decode the transcription
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
    return transcription

def process_file(file_to_process, video_folder_name):
    try:
        # Move the file to the processing directory
        shutil.move(os.path.join('Input-Videos', file_to_process), file_to_process)
        print(f"Processing file: {file_to_process}")

        # Run Processing
        transcription = transcribe_audio(file_to_process)
        print(f"Transcription: {transcription}")

        # Create a new directory for the processed video and move all related files
        new_folder_path = os.path.join('Videos', video_folder_name)
        os.mkdir(new_folder_path)

        # Move the original file
        shutil.move(file_to_process, new_folder_path)

        # Save transcription to a file
        output_file_base = os.path.splitext(file_to_process)[0]
        with open(os.path.join(new_folder_path, f"{output_file_base}.txt"), 'w') as f:
            f.write(transcription[0])

    except Exception as e:
        print(f"Processing failed with error: {e}")
        print("Reversing the file operations...")
        if os.path.exists(os.path.join('Videos', video_folder_name, file_to_process)):
            shutil.move(os.path.join('Videos', video_folder_name, file_to_process), '.')
        if os.path.exists(os.path.join('Videos', video_folder_name)):
            shutil.rmtree(os.path.join('Videos', video_folder_name))

def worker(file_queue):
    while not file_queue.empty():
        try:
            file_to_process = file_queue.get_nowait()
        except queue.Empty:
            break

        video_folder_name = f'Video - {file_to_process[1]}'
        process_file(file_to_process[0], video_folder_name)
        file_queue.task_done()

def process_files_LMT2_batch():
    total_memory, free_memory = get_gpu_memory_info()
    vram_per_process = 11 * 1024**3  # Convert 11.7 GB to bytes
    max_processes = int(free_memory // vram_per_process)

    input_dir = 'Input-Videos'
    files_to_process = os.listdir(input_dir)
    num_files = len(files_to_process)

    file_queue = queue.Queue()
    for i, file_to_process in enumerate(files_to_process, 1):
        file_queue.put((file_to_process, i))

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_processes) as executor:
        futures = [executor.submit(worker, file_queue) for _ in range(max_processes)]
        concurrent.futures.wait(futures)

def cleanup_filenames():
    videos_folder = "./Videos"

    for subdir in os.listdir(videos_folder):
        subdir_path = os.path.join(videos_folder, subdir)
        if os.path.isdir(subdir_path):
            files = os.listdir(subdir_path)
            if files:
                largest_file = max(files, key=lambda f: os.path.getsize(os.path.join(subdir_path, f)))
                new_name = os.path.splitext(largest_file)[0]
                os.rename(subdir_path, os.path.join(videos_folder, new_name))

if __name__ == '__main__':
    process_files_LMT2_batch()
    cleanup_filenames()
