import os, osr
import sys
# import init_file as variables
from shutil import copyfile
import cj_function_lib as cj
import namelist

# cwd = variables.path + "\\"
cwd = sys.argv[1] + "/model/"
path = os.path.dirname(cj.__file__)


cj.write_to(path + "/root_path.py", "pth = '{0}'\n".format(cwd.replace("\\", "/")))

root = path.replace("workflow_lib", "")
sys.path.append(root)
import namelist

ProjList = cj.list_files_from(cwd, "qgs")

if len(ProjList)==0:
    print("Error: No project File Prepared")
    sys.exit()
ProjName = namelist.Project_Name

#Directories
ProjDir = cwd + ProjName + "\\"
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

os.chdir(cwd)
copyfile(root + "workflow_lib/runQSWATBatch.bat", cwd + "\\runQSWATBatch.bat")
os.system("runQSWATBatch.bat " + ProjName + ".qgs")

# set projections for shape files in "...\Project Name\Watershed\Shapes\"
prj_ = osr.SpatialReference()
prj_.ImportFromEPSG(int(cj.read_from(root + "workflow_lib/epsg_code.tmp~")[0]))
prj_wkt = prj_.ExportToWkt()
cj.write_to(cwd + "{0}/Watershed/Shapes/subs1.prj".format(namelist.Project_Name), prj_wkt)
cj.write_to(cwd + "{0}/Watershed/Shapes/riv1.prj".format(namelist.Project_Name), prj_wkt)

# work on the databases
os.chdir(cwd)

print ''
cj.update_status("Working on the Project Database : chm", logging = logging)
execfile(root + "workflow_lib/chm_dbase.py")
cj.update_status("Working on the Project Database : gw", logging = logging)
execfile(root + "workflow_lib/gw_dbase.py")
cj.update_status("Working on the Project Database : bsn", logging = logging)
execfile(root + "workflow_lib/bsn_dbase.py")
cj.update_status("Working on the Project Database : hru", logging = logging)
execfile(root + "workflow_lib/hru_dbase.py")
cj.update_status("Working on the Project Database : mgt", logging = logging)
execfile(root + "workflow_lib/mgt1_dbase.py")
execfile(root + "workflow_lib/mgt2_dbase.py")
cj.update_status("Working on the Project Database : pnd", logging = logging)
execfile(root + "workflow_lib/pnd_dbase.py")
cj.update_status("Working on the Project Database : rte", logging = logging)
execfile(root + "workflow_lib/rte_dbase.py")
cj.update_status("Working on the Project Database : sep", logging = logging)
execfile(root + "workflow_lib/sep_dbase.py")
cj.update_status("Working on the Project Database : sol", logging = logging)
execfile(root + "workflow_lib/sol_dbase.py")
cj.update_status("Working on the Project Database : weather", logging = logging)
execfile(root + "workflow_lib/subhmd_dbase.py")
execfile(root + "workflow_lib/subpcp_dbase.py")
execfile(root + "workflow_lib/subslr_dbase.py")
execfile(root + "workflow_lib/subtmp_dbase.py")
execfile(root + "workflow_lib/subwnd_dbase.py")
cj.update_status("Working on the Project Database : sub          ", logging = logging)
execfile(root + "workflow_lib/sub_dbase.py")
cj.update_status("Working on the Project Database : swq", logging = logging)
execfile(root + "workflow_lib/swq_dbase.py")
cj.update_status("Working on the Project Database : wgn", logging = logging)
execfile(root + "workflow_lib/wgn_dbase.py")
cj.update_status("Working on the Project Database : wus", logging = logging)
execfile(root + "workflow_lib/wus_dbase.py")
cj.update_status("Working on the Project Database : wwq", logging = logging)
execfile(root + "workflow_lib/wwq_dbase.py")
cj.update_status("Working on the Project Database : Finished...", logging = logging)

print ''

# write files to txtinout
cj.update_status("Writing files : chm", logging = logging)
try:
    execfile(root + "workflow_lib/chm.py")
except IOError:
    print("\n\t> could not write files to TxtInOut, make sure that 'QSWAT completed ok'")
    sys.exit()
cj.update_status("Writing files : gw        ", logging = logging)
execfile(root + "workflow_lib/gw.py")
cj.update_status("Writing files : hru", logging = logging)
execfile(root + "workflow_lib/hru.py")
cj.update_status("Writing files : mgt", logging = logging)
execfile(root + "workflow_lib/mgt.py")
cj.update_status("Writing files : pnd", logging = logging)
execfile(root + "workflow_lib/pnd.py")
cj.update_status("Writing files : rte", logging = logging)
execfile(root + "workflow_lib/rte.py")
cj.update_status("Writing files : sep", logging = logging)
execfile(root + "workflow_lib/sep.py")
cj.update_status("Writing files : sol", logging = logging)
execfile(root + "workflow_lib/sol.py")
cj.update_status("Writing files : sub", logging = logging)
execfile(root + "workflow_lib/sub.py")
cj.update_status("Writing files : swq", logging = logging)
execfile(root + "workflow_lib/swq.py")
cj.update_status("Writing files : wus", logging = logging)
execfile(root + "workflow_lib/wus.py")
cj.update_status("Writing files : wwq", logging = logging)
execfile(root + "workflow_lib/wwq.py")
cj.update_status("Writing files : bsn", logging = logging)
execfile(root + "workflow_lib/bsn.py")
cj.update_status("Writing files : wgn", logging = logging)
execfile(root + "workflow_lib/wgn.py")
cj.update_status("Writing files : wnd", logging = logging)
execfile(root + "workflow_lib/wnd.py")
cj.update_status("Writing files : tmp", logging = logging)
execfile(root + "workflow_lib/tmp.py")
cj.update_status("Writing files : pcp", logging = logging)
execfile(root + "workflow_lib/pcp.py")
cj.update_status("Writing files : hmd", logging = logging)
execfile(root + "workflow_lib/hmd.py")
cj.update_status("Writing files : slr", logging = logging)
execfile(root + "workflow_lib/slr.py")

cj.update_status("Writing files : ATMO, fig", logging = logging)
execfile(root + "workflow_lib/fig_ATMO.py")
cj.update_status("Writing files : fert        ", logging = logging)
execfile(root + "workflow_lib/fert.py")
cj.update_status("Writing files : till", logging = logging)
execfile(root + "workflow_lib/till.py")
cj.update_status("Writing files : pest", logging = logging)
execfile(root + "workflow_lib/pest.py")
cj.update_status("Writing files : septwq", logging = logging)
execfile(root + "workflow_lib/septwq.py")
cj.update_status("Writing files : urban", logging = logging)
execfile(root + "workflow_lib/urban.py")
cj.update_status("Writing files : plant", logging = logging)
execfile(root + "workflow_lib/plant.py")
cj.update_status("Writing files : file.cio", logging = logging)
execfile(root + "workflow_lib/cio.py")
cj.update_status("Writing files : Finnished...\n", logging = logging)
execfile(root + "workflow_lib/master_table_db.py") # enable buttons in interface
execfile(root + "workflow_lib/put_params.py")
# print(root + "workflow_lib/swat_64rel.exe")
# print(DefaultSimDir + "\\TxtInOut\\swat_64rel.exe")
copyfile(path + "/swat_64rel.exe", DefaultSimDir + "\\TxtInOut\\swat_64rel.exe")

os.chdir(DefaultSimDir + "TxtInOut")

print ("____________________________________________\nRunning SWAT...\n")
os.system("swat_64rel.exe")

# Cleaning up
tmp_files = cj.list_files_from(cwd, "tmp~")
tmp_files += cj.list_files_from(cwd, "pyc")
tmp_files += cj.list_files_from(root, "pyc")
tmp_files += cj.list_files_from(root, "bat")

for tmp_file in tmp_files:
    cj.delete_file(tmp_file)

os.chdir(root)
print ("\n\nFinnished running QSWAT Workflow\n____________________________________________\n\n")
