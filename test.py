import shutil
import subprocess
import requests
import os

# This code will install all dependancies based on the current needs of the user:
def create_and_activate_conda_env_w(env_name, python_version):
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


if __name__ == "__main__":
    print("Setup Test Env")
    env_name="Batch_Env"
    python_version="3.10"
    create_and_activate_conda_env_w(env_name, python_version)
