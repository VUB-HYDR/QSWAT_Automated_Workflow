@echo off
set mycd=%cd:\=\\%
@echo on
"C:\Python27\python.exe" "C:\SWAT\QSWAT Workflow\run_QSWAT.py" "%mycd%"
