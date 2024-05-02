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

:: Step 3: Start the Anaconda PowerShell prompt and run the update and Python script
echo Opening Anaconda PowerShell Prompt to update Conda and run script...
start "" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Miniconda3 (64-bit)\Anaconda Powershell Prompt (Miniconda3).lnk" powershell -Command "& {conda update conda -y; conda run -n base python %UserProfile%\path\to\your\script\windows_blank_setup.py}"

echo Setup completed!
pause

