#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.34                                                     #
#-------------------------------------------------------------------#

import os

# Define the path to the 'Videos' folder
videos_folder = "./Videos"

# Loop through each subdirectory in the 'Videos' folder
for subdir in os.listdir(videos_folder):
    subdir_path = os.path.join(videos_folder, subdir)

    # Get a list of all files in the subdirectory
    files = os.listdir(subdir_path)

    # Get the file with the largest size
    largest_file = max(files, key=lambda f: os.path.getsize(os.path.join(subdir_path, f)))

    # Rename the subdirectory to the name of the largest file
    new_name = os.path.splitext(largest_file)[0]  # Remove the file extension
    os.rename(subdir_path, os.path.join(videos_folder, new_name))