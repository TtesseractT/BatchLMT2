@echo off
cls
echo Checking for existing applications...

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

:: Check if GitHub Desktop is already installed
if exist "%LocalAppData%\GitHubDesktop\GitHubDesktop.exe" (
    echo GitHub Desktop is already installed.
) else (
    echo GitHub Desktop not found, installing...

    :: Download GitHub Desktop Installer
    echo Downloading GitHub Desktop Installer...
    powershell -command "Invoke-WebRequest -Uri 'https://central.github.com/deployments/desktop/desktop/latest/win32' -OutFile '%UserProfile%\Downloads\GitHubDesktopSetup.exe'"

    :: Install GitHub Desktop
    echo Installing GitHub Desktop...
    start /wait "" "%UserProfile%\Downloads\GitHubDesktopSetup.exe" /S
)

:: Step 3: Properly invoke Miniconda PowerShell, initialize environment, install package, and run script
echo Opening Miniconda PowerShell Prompt to update environment, install 'requests', and run script...
start "" powershell -NoExit -ExecutionPolicy ByPass -Command "& {& '%UserProfile%\Miniconda3\shell\condabin\conda-hook.ps1'; conda activate '%UserProfile%\Miniconda3'; pip install requests; python '%~dp0w10_invoke_setup.py'}"

echo Setup completed!
pause
