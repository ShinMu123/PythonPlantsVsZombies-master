@echo off
REM Launcher created to run the copied PlantsVsZombies project using the workspace .venv
REM Uses relative paths so cmd can execute the script without complex quoting in the terminal tool.
echo Starting PythonPlantsVsZombies...
".\.venv\Scripts\python.exe" "PythonPlantsVsZombies-master\PythonPlantsVsZombies-master\main.py"
echo Game process exited with code %ERRORLEVEL%
pause
