"""
Author: Celray James CHAWANDA, VUB
"""
import os,sys
import cj_function_lib as cj
import namelist
import root_path

path = os.path.dirname(cj.__file__)
root = root_path.pth
sys.path.append(root)
import namelist

ProjList = cj.list_files_from(root, "qgs")

if len(ProjList)==0:
    print("Error: No project File Prepared")
    sys.exit()
ProjName = namelist.Project_Name

#Directories
ProjDir = root + ProjName + "\\"
DefaultSimDir = ProjDir + "Scenarios\\default\\"

#Databases
ProjMDB = ProjDir + ProjName + ".mdb"
QSWAT_MDB =  ProjDir + "QSWATRef2012.mdb"

# ____________________   Basic Settings    ____________________
# Leave = "" in namelist if file does not exist (for file cio)

WeatherDIR = ProjDir + "Weather\\"

pcp_file_txt = WeatherDIR + namelist.Precipitation
tmp_file_txt = WeatherDIR + namelist.Temperature
hmd_file_txt = WeatherDIR + namelist.Rel_Humidity
wnd_file_txt = WeatherDIR + namelist.Wind
slr_file_txt = WeatherDIR + namelist.Solar_Radiation

# for logging
logging = namelist.log

# ____________________  Settings End here  ____________________


