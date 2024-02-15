import shutil
import py7zr
import subprocess
import requests
import os

filename = "cuda_11.8.0_522.06_windows"
url = "https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe"
filename_ffmpeg = "ffmpeg"
url_ffmpeg = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z"

# This code will install all dependancies based on the current needs of the user:
def create_and_activate_conda_env(env_name="Batch_Env", python_version="3.10"):
    """Installs conda, creates a new conda environment with the specified Python version,
       activates it, and changes the working directory to the environment's root."""
    try:
        subprocess.run(["conda", "create", "-n", env_name, f"python={python_version}", "-y"], check=True)
        subprocess.run(["conda", "activate", env_name], check=True, shell=True)
        os.chdir(os.environ["CONDA_PREFIX"])
        print(f"Conda environment '{env_name}' created and activated!")
        print(f"Current working directory: {os.getcwd()}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def download_cuda_file_w10(url: str, filename: str, download_dir: str) -> None:
    """Downloads a file from the specified URL and
    then opens it using the default application."""
    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)
    
    response = requests.get(url)
    with open(os.path.join(download_dir, filename), 'wb') as file:
        file.write(response.content)

    # Open the downloaded file using the default application
    subprocess.Popen([os.path.join(download_dir, filename)], shell=True)

def download_ffmpeg_file(url_ffmpeg: str, filename_ffmpeg: str) -> None:
    """Downloads a file from the specified URL
    Extracts file, and moves bin files to current directory."""
    response = requests.get(url_ffmpeg)
    with open(filename_ffmpeg, 'wb') as file:
        file.write(response.content)
    
    # Extract the 7z file
    with py7zr.SevenZipFile(filename_ffmpeg, mode='r') as z:
        z.extractall()
    
    # Move all .exe binaries from the bin folder to the current directory
    for file in os.listdir(os.path.join(filename_ffmpeg, 'bin')):
        if file.endswith('.exe'):
            shutil.move(os.path.join(filename_ffmpeg, 'bin', file), os.getcwd())


if __name__ == "__main__":
    print("Running Blanket Install for Windows 10")

    # ------------------------------------------------------------------------------------------
    """ This part of the code makes sure that the conda runtime is installed 
    and once installed the code will create an environment needed for the 
    package manager to install all prerecs:
    
    Packages:
        <Conda>
            <Python 3.10>

    """

    user_accepted_confirm = input("""
    Please Install the following software before continuing:
    
    Anaconda: 
    Download Link - https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Windows-x86_64.exe
    
    Once installed close this terminal and launch Anaconda terminal via start menu.
                                  
    If this is the Conda Terminal you will see this-- (Base) at the start of your CLI.
                                  
    Please type 'confirm' if this is true.
    Response: """)
    if user_accepted_confirm.lower() == "confirm":
        try:
            subprocess.run(["conda", "--version"])
            print("Anaconda (Conda) is already installed.")

        except subprocess.CalledProcessError:
            print("Anaconda (Conda) is not installed.\n Installing now")
            create_and_activate_conda_env()
            print("Conda installed, Moving on")

    # ------------------------------------------------------------------------------------------

    """Cuda 11.8 Installation"""
    print("Attempting to install Cuda 11.8")
    subprocess.run(["pip", "install", "requests"])
    download_dir = os.getcwd()  # or any other directory
    download_cuda_file_w10(url, filename, download_dir)

    user_accepted = input("Please type Y only when you have installed CUDA TOOLKIT: ")
    if user_accepted.lower() == "y":
        print("CUDA TOOLKIT Defined as Installed")
        print("Gathering dependancies and installing them")

        subprocess.run(["pip", "install", "py7zr"])

        # Download ffmpeg to the directory using the function:
        download_ffmpeg_file()

        # Upgrade openai-whisper
        print("Installing/upgrading openai-whisper...")
        subprocess.run("pip install -U openai-whisper")

        # Install whisper from GitHub
        print("Installing whisper from GitHub...")
        subprocess.run("pip install git+https://github.com/openai/whisper.git")

        # Upgrade whisper from GitHub
        print("Upgrading whisper from GitHub...")
        subprocess.run("pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git")

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
            #
#