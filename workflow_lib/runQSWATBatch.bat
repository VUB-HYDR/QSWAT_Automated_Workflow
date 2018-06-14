@echo off
set OSGEO4W_ROOT=C:\Program Files (x86)\QGIS Brighton
rem Seems that setting the path is a waste of time - php does not change the path it uses,
rem and qgis_core.dll and qgis_gui.dll are not found.
rem Solution is to place them in the projects folder,  where this cript is run by php.
set PATH=%OSGEO4W_ROOT%\bin

rem Add application-specific environment settings
for %%f in ("%OSGEO4W_ROOT%\etc\ini\*.bat") do call "%%f"

set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python
rem QGIS binaries
set PATH=%PATH%;%OSGEO4W_ROOT%\apps\qgis\bin;%OSGEO4W_ROOT%\apps\qgis\python
rem disable QGIS console messages
set QGIS_DEBUG=-1

rem default QGIS plugins
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python\plugins
rem user installed plugins
set PYTHONPATH=%PYTHONPATH%;%USERPROFILE%\.qgis2\python\plugins

"%OSGEO4W_ROOT%\bin\python.exe" "%USERPROFILE%\.qgis2\python\plugins\QSWAT\QSWATBatch.py" %1
rem QSWATBatch.py returns 0 (OK) or 1 (error)
exit /b %ERRORLEVEL%



