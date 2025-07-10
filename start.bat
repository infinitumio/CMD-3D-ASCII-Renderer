@echo off
echo.
echo  ██████╗███╗   ███╗██████╗      ██████╗ ██████╗ 
echo ██╔════╝████╗ ████║██╔══██╗     ╚════██╗██╔══██╗
echo ██║     ██╔████╔██║██║  ██║█████╗ ███╔═╝██║  ██║
echo ██║     ██║╚██╔╝██║██║  ██║╚════╝ ╚══██╗██║  ██║
echo ╚██████╗██║ ╚═╝ ██║██████╔╝     ██████╔╝██████╔╝
echo  ╚═════╝╚═╝     ╚═╝╚═════╝      ╚═════╝ ╚═════╝ 
echo.
echo        Command Prompt 3D ASCII Renderer
echo          Real-time 3D graphics in CMD!
echo.
echo Checking system compatibility...
python src\setup.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Setup check failed. Please resolve the issues above.
    pause
    exit /b 1
)

echo.
echo Starting Command Prompt 3D renderer...
echo Make sure your Command Prompt window is maximized for the best experience!
echo.
timeout /t 3 /nobreak
python src\cmdASCIIRenderer.py

echo.
echo Thanks for using Command Prompt 3D ASCII Renderer!
pause
