import shutil
import subprocess
import requests
import platform
import os
from zipfile import ZipFile
from pathlib import Path

def windows_install():
    print("System detected: Windows")
    print("\nRunning Blanket Install for Windows 10\n")
    try:
        print("Testing Cuda Availability")
        subprocess.run(['nvidia-smi'])
    except:
        print("Cuda Not Installed")

    """Cuda 11.8 Installation"""
    print("\nAttempting to install Cuda 11.8")
    download_dir = os.getcwd()  # Use the current working directory or specify another
    filename = "cuda_11.8.0_522.06_windows.exe"
    url = "https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe"
    download_and_install_cuda_w(url, filename, download_dir)

    try:
        print("Conda Version:\n")
        subprocess.run(["conda", "--version"])
    except:
        print("Conda Not Installed\n Run windows_setup.bat as Admin")
    
    print("Testing for git")
    try:
        subprocess.run(['conda', '--version'])
    except:
        subprocess.run(['conda', 'install', 'git', '-y'])

    print("\nInstalling Whisper from OpenAI\n")
    subprocess.run(['pip', 'install', 'git+https://github.com/openai/whisper.git'])
    subprocess.run(['pip', 'install', '--upgrade', '--no-deps', '--force-reinstall', 'git+https://github.com/openai/whisper.git'])

    print("\nUpgrading PyTorch...")
    subprocess.run(['pip', 'install', 'torch', 'torchvision', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu118'])
    
    print("\nSetup Complete, Creating Directory")
    # Create the directories if they don't exist
    if not os.path.exists('Input-Videos'):
        os.mkdir('Input-Videos')

    print("\nDownload Complete: Follow Instructions with CUDA for your system.")
    print("\nPlease 'Restart' computer for changes to be saved once CUDA has finished installing.")

def mac_install():
    print("System detected: Mac OS")

def linux_install():
    print("System detected: Linux")

def download_and_install_cuda_w(url: str, filename: str, download_dir: str) -> None:
    """Downloads CUDA installer from the specified URL to the given directory,
    and then executes a silent installation."""
    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Download the file
    print("Downloading CUDA installer...")
    response = requests.get(url)
    installer_path = os.path.join(download_dir, filename)
    with open(installer_path, 'wb') as file:
        file.write(response.content)
    print("Download complete.")

    # Execute the installer silently
    print("Installing CUDA...")
    subprocess.Popen([installer_path, '/S', f'/D={download_dir}'], shell=True)
    print("Installation started. Please wait for it to complete.")
    
def get_os_variable():
    system, node, release, version, machine, processor = platform.uname()
    os_name = platform.system()
    
    if os_name == "Windows":
        # Extracting major version number for Windows
        major_version = version.split('.')[2]
        return f'w_{major_version}'
    elif os_name == "Darwin":
        # MacOS version can be found directly in `release`
        return f'm_{release}'
    elif os_name == "Linux":
        # Optionally handle Linux differently; here we use the kernel release
        return f'l_{release}'
    else:
        return f'other_{release}'

if __name__ == "__main__":

    os_variable = get_os_variable()
    print(os_variable)

    if os_variable.startswith('w_'):
        print("The system is running Windows.")
        windows_install()

    elif os_variable.startswith('m_'):
        print("The system is running macOS.")

    elif os_variable.startswith('l_'):
        print("The system is running Linux.")
    else:
        print("The operating system is unknown or not supported.")

