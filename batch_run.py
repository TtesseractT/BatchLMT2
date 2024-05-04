#-------------------------------------------------------------------#
# BatchWhisper                                                      #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.5                                                      #
#-------------------------------------------------------------------#

import os
import shutil
import subprocess

# Count the number of files in the input directory
num_files = len(os.listdir('Input-Videos'))
i = 1

try:
    while num_files > 0:
        video_folder_name = f'Video - {i}'

        while os.path.exists(os.path.join('Videos', video_folder_name)):
            i += 1
            video_folder_name = f'Video - {i}'

        # Move the first file from input directory to processing directory
        file_to_process = os.listdir('Input-Videos')[0]
        shutil.move(os.path.join('Input-Videos', file_to_process), file_to_process)
        print(f"Processing file: {file_to_process}")
        
        # Run Processing
        subprocess.run(f'whisper "{file_to_process}" --device cuda --model large --language en --task transcribe --output_format all', shell=True)
        
        # Create a new directory for the processed video and move all related files
        new_folder_path = os.path.join('Videos', video_folder_name)
        os.mkdir(new_folder_path)
        
        # Move the original file
        shutil.move(file_to_process, new_folder_path)

        # Move all related output files
        output_file_base = os.path.splitext(file_to_process)[0]
        for filename in os.listdir('.'):  # list all files in the current directory
            if filename.startswith(output_file_base):  # check if the filename starts with the base name
                shutil.move(filename, new_folder_path)  # move the file to the new directory
        num_files -= 1
        i += 1

except Exception as e:
    print(f"Processing failed with error: {e}")
    print("Reversing the file operations...")

    # Move the files back to their original locations
    shutil.move(os.path.join('Videos', video_folder_name, file_to_process), '.')
    shutil.move(os.path.join('Videos', video_folder_name, output_file_txt), '.')
    shutil.move(os.path.join('Videos', video_folder_name, output_file), '.')
        
    # Delete the (file_to_process).wav file
    os.remove(f'{file_to_process}.wav')
    print("File operations reversed.")