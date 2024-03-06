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
    # Upgrade openai-whisper
    print("Installing/upgrading openai-whisper...")
    subprocess.run("pip install -U openai-whisper")

    # Install whisper from GitHub
    print("Installing whisper from GitHub...")
    subprocess.run("pip install git+https://github.com/openai/whisper.git")

    # Upgrade whisper from GitHub
    print("Upgrading whisper from GitHub...")
    subprocess.run("pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git")

    # Install ffmpeg
    print("Installing ffmpeg...")
    subprocess.run("pip install ffmpeg")

    # Install openai
    print("Installing openai...")
    subprocess.run("pip install openai")

    # Install setuptools-rust
    print("Installing setuptools-rust...")
    subprocess.run("pip install setuptools-rust")

    # Install torch for CUDA
    print("Installing torch, torchvision, and torchaudio...")
    subprocess.run("pip install torch torchvision torchaudio")

    # Create the directories if they don't exist
    if not os.path.exists('Input-Videos'):
        os.mkdir('Input-Videos')
