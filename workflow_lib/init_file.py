"""
Author: Celray James CHAWANDA, VUB
"""
import os,sys
import cj_function_lib as cj

path = os.path.dirname(cj.__file__)
root = path.replace("workflow_lib", "")
#print("Lib: " + root)
sys.path.append(root)
import settings

ProjList = cj.list_files_from(root, "qgs")
if len(ProjList)>1:
    print ProjList
    print("Error: There are more than one project files in the directory, please make sure you only keep the one you want to work on.")
    sys.exit()
if len(ProjList)==0:
    print("Error: No project File Prepared")
    sys.exit()
ProjName = ProjList[0].split("\\")[-1].replace(".qgs","")

#Directories
ProjDir = root + ProjName + "\\"
DefaultSimDir = ProjDir + "Scenarios\\default\\"

#Databases
ProjMDB = ProjDir + ProjName + ".mdb"
QSWAT_MDB =  ProjDir + "QSWATRef2012.mdb"

# ____________________   Basic Settings    ____________________
# Leave = "" in settings if file does not exist (for file cio)

WeatherDIR = ProjDir + "Weather\\"

pcp_file_txt = WeatherDIR + settings.Precipitation
tmp_file_txt = WeatherDIR + settings.Temperature
hmd_file_txt = WeatherDIR + settings.Rel_Humidity
wnd_file_txt = WeatherDIR + settings.Wind
slr_file_txt = WeatherDIR + settings.Solar_Radiation

# for logging
logging = settings.log

# ____________________  Settings End here  ____________________


