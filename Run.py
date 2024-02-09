#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.34                                                     #
#-------------------------------------------------------------------#

import os
import shutil
import subprocess
import argparse
import language_dict
import output_format_type

# Create an argument parser and provide a description for the argument
parser = argparse.ArgumentParser(description="Choose the type of process to run.")
parser.add_argument('--type', type=int, choices=range(1, 7), required=True, help="Type of process to run (1 to 6)")
args = parser.parse_args()

# Ask for the language input if the process type requires it
if args.type in [3, 4, 5, 6]:
    print("Available languages:", language_dict.available_languages)

    # Loop until a valid language is selected
    while True:
        print("---------------------------")
        full_language_name = input("Enter the full name of the language: ")
        language = language_dict.language_dict.get(full_language_name)
        if language is not None:
            print("Selected language:", language)
            break  # Exit the loop
        else:
            print("Unknown language:", full_language_name)

# Ask for the output format if the process type requires it
if args.type in [3, 4, 5, 6]:
    print("Available Output Formats:", output_format_type.available_op_format)

    while True:
        print("---------------------------")
        output_file_t = input("Enter the output format: ")
        out_format = output_format_type.output_format_type.get(output_file_t)
        if out_format is not None:
            print("Selected output format:", out_format)
            break  # Exit the loop
        else:
            print("Unknown output format:", output_file_t)

# Create the directories if they don't exist
if not os.path.exists('Videos'):
    os.mkdir('Videos')
num_files = len(os.listdir('Input-Videos'))
i = 1
root_directory = os.getcwd()

# Loop until all files have been processed
while num_files > 0:
    video_folder_name = f'Video - {i}'
    while os.path.exists(os.path.join('Videos', video_folder_name)):
        i += 1
        video_folder_name = f'Video - {i}'
    file_to_process = os.listdir('Input-Videos')[0]
    print(f"Processing file: {file_to_process}")
    shutil.move(os.path.join('Input-Videos', file_to_process), file_to_process)
    file_extension = os.path.splitext(file_to_process)[-1].lower()
    valid_audio_file = file_extension in ['.mp3', '.wav']

    # Convert non-audio files to WAV format if necessary
    if not valid_audio_file and args.type in [3, 4, 5, 6]:
        output_file = f'{os.path.splitext(file_to_process)[0]}.wav'
        subprocess.run(['ffmpeg',"-loglevel", "error", "-stats", "-i", file_to_process, '-acodec', 'pcm_s16le', '-ar', '44100', output_file])
        converted_file = output_file

    os.chdir(root_directory)

    # Run the specified process based on the process type
    if args.type == 1:
        subprocess.run(['python', 'Text_AudioSegments.py', file_to_process])
        
    elif args.type == 2:
        subprocess.run(['python', 'Text_AudioSegments_Translate.py', file_to_process])
        
    elif args.type == 3:
        subprocess.run(
            f'whisper "{output_file}" --device cpu --model large --language {language} --task translate --output_format {out_format}',
            shell=True)
        
    elif args.type == 4:
        subprocess.run(
            f'whisper "{output_file}" --device cuda --model large --language {language} --task translate --output_format {out_format}',
            shell=True)
        
    elif args.type == 5:
        subprocess.run(
            f'whisper "{output_file}" --device cpu --model large --language {language} --task transcribe --output_format {out_format}',
            shell=True)
        
    elif args.type == 6:
        subprocess.run(
            f'whisper "{output_file}" --device cuda --model large --language {language} --task transcribe --output_format {out_format}',
            shell=True)

    # Create a new directory for the processed video and move the files
    os.mkdir(os.path.join('Videos', video_folder_name))
    shutil.move(file_to_process, os.path.join('Videos', video_folder_name))

    if args.type in [3, 4, 5, 6]:
        output_file_base = os.path.splitext(output_file)[0]
        output_file_txt = f'{output_file_base}.{out_format}'
        shutil.move(output_file_txt, os.path.join('Videos', video_folder_name, output_file_txt))
        shutil.move(output_file, os.path.join('Videos', video_folder_name))

    if args.type in [1, 2]:
        shutil.move('transcripts.txt', os.path.join('Videos', video_folder_name))
        shutil.move('Audio_Segment', os.path.join('Videos', video_folder_name))

    num_files -= 1
    i += 1

cwd = os.getcwd()
directory = os.path.join(cwd, "Videos")

# Clean up the temporary files and directories
for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    subprocess.run(['python', 'CleanUp.py'])
    
