@echo off
cls
echo Setting up Miniconda...

:: Step 1: Download Miniconda Installer
echo Downloading Miniconda Installer...
powershell -command "Invoke-WebRequest -Uri 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe' -OutFile '%UserProfile%\Downloads\Miniconda3-latest-Windows-x86_64.exe'"

:: Step 2: Install Miniconda Silently
echo Installing Miniconda...
start /wait "" "%UserProfile%\Downloads\Miniconda3-latest-Windows-x86_64.exe" /InstallationType=JustMe /RegisterPython=1 /S /D=%UserProfile%\Miniconda3

:: Step 3: Update Conda in a new Miniconda PowerShell session
echo Updating Conda...
powershell -command "Start-Process 'powershell.exe' -ArgumentList '-NoExit','-Command', 'conda init; conda update conda -y'"

:: Optional: Execute a Python script (uncomment and modify the following line as needed)
powershell -command "& {Start-Process PowerShell -ArgumentList '-NoExit', '-Command', 'conda run -n base python w10_invoke_setup.py'}"

echo Setup completed!
pause

