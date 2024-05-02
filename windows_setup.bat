@echo off
cls
echo Checking for existing Miniconda installation...

:: Check if Miniconda is already installed
if exist "%UserProfile%\Miniconda3\" (
    echo Miniconda is already installed.
) else (
    echo Miniconda not found, installing...

    :: Step 1: Download Miniconda Installer
    echo Downloading Miniconda Installer...
    powershell -command "Invoke-WebRequest -Uri 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe' -OutFile '%UserProfile%\Downloads\Miniconda3-latest-Windows-x86_64.exe'"

    :: Step 2: Install Miniconda Silently
    echo Installing Miniconda...
    start /wait "" "%UserProfile%\Downloads\Miniconda3-latest-Windows-x86_64.exe" /InstallationType=JustMe /RegisterPython=1 /S /D=%UserProfile%\Miniconda3
)

:: Step 3: Properly invoke PowerShell, initialize Conda environment, install the package, and run the script
echo Opening PowerShell, initializing Conda, installing 'requests', and running script...
start "" powershell -NoExit -Command "cd '%UserProfile%\Miniconda3'; .\Scripts\activate; conda activate base; pip install requests; python '%~dp0w10_invoke_setup.py'"

echo Setup completed!
pause
