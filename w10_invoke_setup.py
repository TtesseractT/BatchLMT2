import shutil
import subprocess
import requests
import os

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

def download_and_install_cuda(url: str, filename: str, download_dir: str) -> None:
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

if __name__ == "__main__":
    print("Running Blanket Install for Windows 10")

    user_accepted_confirm = input("""

    Conda: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe                             
                                  
    Please type 'confirm' if this is true.
    Response: """)
    if user_accepted_confirm.lower() == "confirm":
        try:
            subprocess.run(["conda", "--version"])
            print("Anaconda (Conda) is already installed.")

        except subprocess.CalledProcessError:
            print("Anaconda (Conda) is not installed.\n Please follow the link above to download Conda.")

    # Close current 
    # ------------------------------------------------------------------------------------------

    """Cuda 11.8 Installation"""
    print("Attempting to install Cuda 11.8")
    download_dir = os.getcwd()  # Use the current working directory or specify another
    filename = "cuda_11.8.0_522.06_windows.exe"
    url = "https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe"
    download_and_install_cuda(url, filename, download_dir)

    print("Gathering dependancies and installing them")
    subprocess.run(["pip", "install", "py7zr"])

    # Install whisper from GitHub
    print("Installing whisper from GitHub...")
    subprocess.run(["pip", "install", "git+https://github.com/openai/whisper.git"])

    # Upgrade whisper from GitHub
    print("Upgrading whisper from GitHub...")
    subprocess.run(["pip", "install", "--upgrade", "--no-deps", "--force-reinstall", "git+https://github.com/openai/whisper.git"])

    print("Upgrading PyTorch...")
    subprocess.run([f'pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118'])
    
    print("Setup Complete, Creating Directory")
    # Create the directories if they don't exist
    if not os.path.exists('Input-Videos'):
        os.mkdir('Input-Videos')
