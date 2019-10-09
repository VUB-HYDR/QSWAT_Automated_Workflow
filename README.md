# QSWAT_Automated_Workflow v1.5.8

Automated workflow for setting up the SWAT Model presented in Chawanda et al., 2019 EMS. 
## Find instructions in the [User Mannual](./QSWAT_WF_manual.pdf)

## What is new in v1.5.8?
Included mechanism to go back from model to input data and namelist.
New features in the namelist include:
   * Create Figures
   * Run Calibration

Descriptions are included in the namelist.

## To Install
[Qgis 2.6.1 (32bit)](http://qgis.org/downloads/QGIS-OSGeo4W-2.6.1-1-Setup-x86.exe)   
[QSWAT Workflow v1.5.8](https://github.com/VUB-HYDR/QSWAT_Automated_Workflow/releases/download/v1.5.8/QSWAT.Workflow.v1.5.8.msi)   
## For users
This repository includes the code for the wrapper presented in this paper. The wrapper runs in 32 bit version of python 2.7.

### 1. [runQSWAT.bat](./runQSWAT.bat) 
This file is called when the command "runQSWAT" is passed in command prompt or powershell

### 2. [run_QSWAT.py](./run_QSWAT.py) 
This file is used by [runQSWAT.bat](./runQSWAT.bat) to launch the model set up process

### 3. [namelist.py](./test_data/namelist.py)
This is the file where all settings for the configuration of the model are entered

### 4. [workflow_lib](./workflow_lib)
This directory contains all the modules for the  workflow

### 5. [test_data](./test_data)
This directory has an example data-set for testing 

## Versions
Version 1.5.8 - October 2019

## Authors
Celray James CHAWANDA   
Chris GEORGE

## License
This project is licensed under the MIT License. See also the [license](./LICENSE) file.

