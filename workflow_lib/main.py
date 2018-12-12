import os, osr
import sys
import init_file as variables
from shutil import copyfile
import cj_function_lib as cj
import namelist

cwd = variables.path + "\\"

os.chdir(variables.root)
copyfile(cwd + "runQSWATBatch.bat", variables.root + "\\runQSWATBatch.bat")
os.system("runQSWATBatch.bat " + variables.ProjName + ".qgs")

# set projections for shape files in "...\Project Name\Watershed\Shapes\"
prj_ = osr.SpatialReference()
prj_.ImportFromEPSG(int(cj.read_from("workflow_lib/epsg_code.tmp~")[0]))
prj_wkt = prj_.ExportToWkt()
cj.write_to("{0}/Watershed/Shapes/subs1.prj".format(namelist.Project_Name), prj_wkt)
cj.write_to("{0}/Watershed/Shapes/riv1.prj".format(namelist.Project_Name), prj_wkt)

# work on the databases
os.chdir(variables.path)

print ''
cj.update_status("Working on the Project Database : chm", logging = variables.logging)
execfile(cwd + "chm_dbase.py")
cj.update_status("Working on the Project Database : gw", logging = variables.logging)
execfile(cwd + "gw_dbase.py")
cj.update_status("Working on the Project Database : bsn", logging = variables.logging)
execfile(cwd + "bsn_dbase.py")
cj.update_status("Working on the Project Database : hru", logging = variables.logging)
execfile(cwd + "hru_dbase.py")
cj.update_status("Working on the Project Database : mgt", logging = variables.logging)
execfile(cwd + "mgt1_dbase.py")
execfile(cwd + "mgt2_dbase.py")
cj.update_status("Working on the Project Database : pnd", logging = variables.logging)
execfile(cwd + "pnd_dbase.py")
cj.update_status("Working on the Project Database : rte", logging = variables.logging)
execfile(cwd + "rte_dbase.py")
cj.update_status("Working on the Project Database : sep", logging = variables.logging)
execfile(cwd + "sep_dbase.py")
cj.update_status("Working on the Project Database : sol", logging = variables.logging)
execfile(cwd + "sol_dbase.py")
cj.update_status("Working on the Project Database : weather", logging = variables.logging)
execfile(cwd + "subhmd_dbase.py")
execfile(cwd + "subpcp_dbase.py")
execfile(cwd + "subslr_dbase.py")
execfile(cwd + "subtmp_dbase.py")
execfile(cwd + "subwnd_dbase.py")
cj.update_status("Working on the Project Database : sub          ", logging = variables.logging)
execfile(cwd + "sub_dbase.py")
cj.update_status("Working on the Project Database : swq", logging = variables.logging)
execfile(cwd + "swq_dbase.py")
cj.update_status("Working on the Project Database : wgn", logging = variables.logging)
execfile(cwd + "wgn_dbase.py")
cj.update_status("Working on the Project Database : wus", logging = variables.logging)
execfile(cwd + "wus_dbase.py")
cj.update_status("Working on the Project Database : wwq", logging = variables.logging)
execfile(cwd + "wwq_dbase.py")
cj.update_status("Working on the Project Database : Finished...", logging = variables.logging)

print ''

# write files to txtinout
cj.update_status("Writing files : chm", logging = variables.logging)
try:
    execfile(cwd + "chm.py")
except IOError:
    print("\n\t> could not write files to TxtInOut, make sure that 'QSWAT completed ok'")
    sys.exit()
cj.update_status("Writing files : gw        ", logging = variables.logging)
execfile(cwd + "gw.py")
cj.update_status("Writing files : hru", logging = variables.logging)
execfile(cwd + "hru.py")
cj.update_status("Writing files : mgt", logging = variables.logging)
execfile(cwd + "mgt.py")
cj.update_status("Writing files : pnd", logging = variables.logging)
execfile(cwd + "pnd.py")
cj.update_status("Writing files : rte", logging = variables.logging)
execfile(cwd + "rte.py")
cj.update_status("Writing files : sep", logging = variables.logging)
execfile(cwd + "sep.py")
cj.update_status("Writing files : sol", logging = variables.logging)
execfile(cwd + "sol.py")
cj.update_status("Writing files : sub", logging = variables.logging)
execfile(cwd + "sub.py")
cj.update_status("Writing files : swq", logging = variables.logging)
execfile(cwd + "swq.py")
cj.update_status("Writing files : wus", logging = variables.logging)
execfile(cwd + "wus.py")
cj.update_status("Writing files : wwq", logging = variables.logging)
execfile(cwd + "wwq.py")
cj.update_status("Writing files : bsn", logging = variables.logging)
execfile(cwd + "bsn.py")
cj.update_status("Writing files : wgn", logging = variables.logging)
execfile(cwd + "wgn.py")
cj.update_status("Writing files : wnd", logging = variables.logging)
execfile(cwd + "wnd.py")
cj.update_status("Writing files : tmp", logging = variables.logging)
execfile(cwd + "tmp.py")
cj.update_status("Writing files : pcp", logging = variables.logging)
execfile(cwd + "pcp.py")
cj.update_status("Writing files : hmd", logging = variables.logging)
execfile(cwd + "hmd.py")
cj.update_status("Writing files : slr", logging = variables.logging)
execfile(cwd + "slr.py")

cj.update_status("Writing files : ATMO, fig", logging = variables.logging)
execfile(cwd + "fig_ATMO.py")
cj.update_status("Writing files : fert        ", logging = variables.logging)
execfile(cwd + "fert.py")
cj.update_status("Writing files : till", logging = variables.logging)
execfile(cwd + "till.py")
cj.update_status("Writing files : pest", logging = variables.logging)
execfile(cwd + "pest.py")
cj.update_status("Writing files : septwq", logging = variables.logging)
execfile(cwd + "septwq.py")
cj.update_status("Writing files : urban", logging = variables.logging)
execfile(cwd + "urban.py")
cj.update_status("Writing files : plant", logging = variables.logging)
execfile(cwd + "plant.py")
cj.update_status("Writing files : file.cio", logging = variables.logging)
execfile(cwd + "cio.py")
cj.update_status("Writing files : Finnished...\n", logging = variables.logging)
execfile(cwd + "master_table_db.py") # enable buttons in interface
execfile(cwd + "put_params.py")
copyfile(cwd + "swat_64rel.exe", variables.DefaultSimDir + "\\TxtInOut\\swat_64rel.exe")

os.chdir(variables.DefaultSimDir + "TxtInOut")

print ("____________________________________________\nRunning SWAT...\n")
os.system("swat_64rel.exe")

# Cleaning up
tmp_files = cj.list_files_from(variables.path, "tmp~")
tmp_files += cj.list_files_from(variables.path, "pyc")
tmp_files += cj.list_files_from(variables.root, "pyc")
tmp_files += cj.list_files_from(variables.root, "bat")

for tmp_file in tmp_files:
    cj.delete_file(tmp_file)

os.chdir(variables.root)
print ("\n\nFinnished running QSWAT Workflow\n____________________________________________\n\n")
