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

:: Check if Git is installed
if exist "%ProgramFiles%\Git\bin\git.exe" (
    echo Git is already installed.
) else (
    echo Git not found, installing...

    :: Download Git Installer
    echo Downloading Git Installer...
    powershell -command "Invoke-WebRequest -Uri 'https://github.com/git-for-windows/git/releases/latest/download/Git-2.32.0.2-64-bit.exe' -OutFile '%UserProfile%\Downloads\GitInstaller.exe'"

    :: Install Git and add it to the system PATH
    echo Installing Git...
    start /wait "" "%UserProfile%\Downloads\GitInstaller.exe" /VERYSILENT /NORESTART /NOCANCEL /SP- /LOG /COMPONENTS="icons,ext\reg\shellhere,assoc,assoc_sh"

    :: Optionally, add Git to PATH immediately for this session
    set PATH=%PATH%;%ProgramFiles%\Git\bin
)

:: Step 3: Properly invoke Miniconda PowerShell, initialize environment, install package, and run script
echo Opening Miniconda PowerShell Prompt to update environment, install 'requests', and run script...
start "" powershell -NoExit -ExecutionPolicy ByPass -Command "& {& '%UserProfile%\Miniconda3\shell\condabin\conda-hook.ps1'; conda activate '%UserProfile%\Miniconda3'; pip install requests; python '%~dp0w10_invoke_setup.py'}"

echo Setup completed!
pause
