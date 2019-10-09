# QSWAT_Automated_Workflow v1.5.8

Automated workflow for setting up the SWAT Model presented in Chawanda et al., 2018 EMS. 

## What is new in v1.5.8?
Included mechanism to go back from model to input data and namelist.
New setting in the namelist include:
   * Model_2_namelist
   * ET_method
   * Routing_method
   * Rainfall_timestep
   * Run_off_method
Descriptions are included in the namelist.


## To Install
[Qgis 2.6.1 (32bit)](http://qgis.org/downloads/QGIS-OSGeo4W-2.6.1-1-Setup-x86.exe)   
[QSWAT Workflow v1.5.8](https://swat.tamu.edu/media/115805/qswatinstall15.zip)   

## For users
This repository includes the code for the wrapper presented in this paper. The wrapper runs in 32 bit version of python 2.7.

### 1. [runQSWAT.py](./runQSWAT.py) 
This is the file used to launch the model set up process

### 2. [namelist.py](./namelist.py)
This is the file where all settings for the configuration of the model are entered

### 3. [workflow_lib](./workflow_lib)
This directory contains all the modules for the  workflow

### 4. [Data](./Data)
This directory has an example dataset for testing 

## Versions
Version 1.5.8 - September 2019

## Authors
Celray James CHAWANDA   
Chris GEORGE

## License
This project is licensed under the MIT License. See also the [license](./LICENSE) file.

