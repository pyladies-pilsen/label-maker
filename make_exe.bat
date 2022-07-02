@echo off

ECHO --- Creating exe file ---
ECHO (make sure you have "venv" folder with pyinstaller in project root)


SET SCRIPTPATH=%~dp0

rem ECHO %SCRIPTPATH%
ECHO - removing old dist folder
rmdir /s /q "%SCRIPTPATH%\dist"

ECHO - preparing new dist folder structure
mkdir "%SCRIPTPATH%\dist\label_maker_executable"
set TEMPEXECUTABLE="%SCRIPTPATH%\dist\label_maker_executable"

ECHO - copying source files
xcopy /i /y "calc.py" "%TEMPEXECUTABLE%" > nul
xcopy /i /y "config.py" "%TEMPEXECUTABLE%" > nul
xcopy /i /y "inputs.py" "%TEMPEXECUTABLE%" > nul
xcopy /i /y "outputs.py" "%TEMPEXECUTABLE%" > nul
xcopy /i /y "label_maker.py" "%TEMPEXECUTABLE%" > nul


rem Do the work in the temp executable folder
cd /D %TEMPEXECUTABLE%

ECHO - generating executable, please wait ...
"%SCRIPTPATH%\venv\Scripts\pyinstaller.exe" label_maker.py -F --log-level=WARN --name label_maker > nul

rem copy the created executable
xcopy /i /y "%TEMPEXECUTABLE%\dist\label_maker.exe" "%SCRIPTPATH%" > nul

rem remove build files
cd %SCRIPTPATH%
@RD /S /Q "%SCRIPTPATH%\dist" > nul

ECHO -- Executable generated
