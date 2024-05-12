import os
import argparse
import subprocess
import datetime

def get_video_duration(file_path):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration", "-of",
             "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return float(result.stdout)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def get_total_duration(directory):
    total_seconds = 0

    # Traverse directory and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                file_path = os.path.join(root, file)
                total_seconds += get_video_duration(file_path)

    # Convert total seconds to HH:MM:SS
    total_duration = str(datetime.timedelta(seconds=int(total_seconds)))
    return total_duration

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the total duration of all .mp4 files in a directory and its subdirectories.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Path to the directory")

    args = parser.parse_args()
    directory = args.input

    total_duration = get_total_duration(directory)
    print(f"Total duration of all .mp4 files: {total_duration}")
