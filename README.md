# 2018_Chawanda_etal_EMS

Automated workflow for setting up the SWAT Model presented in Chawanda et al., 2018 EMS. 

## To Install
[Qgis 2.6.1 (32bit)](http://qgis.org/downloads/QGIS-OSGeo4W-2.6.1-1-Setup-x86.exe)   
[QSWAT 1.5](https://swat.tamu.edu/media/115805/qswatinstall15.zip)   
[gdal](https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows)   
install pyodbc via `pip install pyodbc`   


## For users
This repository includes the code for the wrapper presented in this paper. The wrapper runs in 32 bit version of python 2.7.

### 1. [runQGISWorkflow.py](./runQGISWorkflow.py) 
This is the file used to launch the model set up process

### 2. [settings.py](./settings.py)
This is the namelist where all settings for the configuration of the model are entered

### 3. [workflow_lib](./workflow_lib)
This directory contains all the modules for the  workflow

## Versions
Version 0.1.0 - June 2018

## Authors
Celray James CHAWANDA   
Chris GEORGE

## License
This project is licensed under the MIT License. See also the [license](./LICENCE) file.

