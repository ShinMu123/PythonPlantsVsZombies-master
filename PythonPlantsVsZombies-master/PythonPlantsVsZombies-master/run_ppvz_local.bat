@echo off
setlocal
pushd %~dp0
echo Running Plants vs Zombies locally...
echo.
python run_game.py
echo.
echo (Press any key to close)
pause >nul
popd
endlocal

