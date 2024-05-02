#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.4                                                      #
#-------------------------------------------------------------------#

import subprocess
import os

if __name__ == "__main__":

    # Install whisper from GitHub
    print("Installing whisper from GitHub...")
    subprocess.run("pip install git+https://github.com/openai/whisper.git")

    # Install ffmpeg
    print("Installing ffmpeg...")
    subprocess.run("pip install ffmpeg")

    # Install openai
    print("Installing openai...")
    subprocess.run("pip install openai")

    # Install torch for CUDA
    print("Installing torch, torchvision, and torchaudio...")
    subprocess.run("pip install torch torchvision torchaudio")

    # Create the directories if they don't exist
    if not os.path.exists('Input-Videos'):
        os.mkdir('Input-Videos')
