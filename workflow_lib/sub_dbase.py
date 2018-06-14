
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
subrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'subrng', variables.path + "\\subrgn.tmp~")
basindata1 = cj.extract_table_from_mdb(variables.ProjMDB, 'BASINSDATA1', variables.path + "\\basindata1.tmp~")

try:
    subpcp = cj.extract_table_from_mdb(variables.ProjMDB, 'SubPcp', variables.path + "\\subpcp.tmp~")
except:
    pass
try:
    subslr = cj.extract_table_from_mdb(variables.ProjMDB, 'SubSlr', variables.path + "\\subslr.tmp~")
except:
    pass
try:
    subtmp = cj.extract_table_from_mdb(variables.ProjMDB, 'SubTmp', variables.path + "\\subtmp.tmp~")
except:
    pass
try:
    subhmd = cj.extract_table_from_mdb(variables.ProjMDB, 'SubHmd', variables.path + "\\subhmd.tmp~")
except:
    pass
try:
    subwnd = cj.extract_table_from_mdb(variables.ProjMDB, 'SubWnd', variables.path + "\\subwnd.tmp~")
except:
    pass

watershed_data = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")


sub_defaults={} 
for record in subrgn: # Getting a list of parameter names for sub and their defaults
    if record.split(",")[0].strip(" ") != "":
        sub_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the sub to a row in the table sub
"""

count_up_10 = ["ELEVB", "ELEVB_FR", "SNOEB"]
count_up_12 = ["RFINC", "TMPINC", "RADINC", "HUMINC"]

for c10 in count_up_10:
    for j in range(1,11):
        sub_defaults[c10 + str(j)] = sub_defaults[c10]
    sub_defaults.pop(c10)
    
for c12 in count_up_12:
    for j in range(1,13):
        sub_defaults[c12 + str(j)] = sub_defaults[c12]
    sub_defaults.pop(c12)

sub = mdt.mdb_with_ops(variables.ProjMDB)
sub.clear_table("sub")

for i in range(0, len(watershed_data)):    # getting field values from hrus table
    sub_defaults["OID"] = float(watershed_data[i].split(",")[0])
    sub_defaults["SUBBASIN"] = int(watershed_data[i].split(",")[3])

    sub_defaults["SUB_KM"] = float(watershed_data[i].split(",")[4])/100.000000
    sub_defaults["SUB_LAT"] = float(watershed_data[i].split(",")[11])
    sub_defaults["SUB_ELEV"] = float(watershed_data[i].split(",")[13])


    if os.path.isfile(variables.path + "\\subpcp.tmp~"):
        sub_defaults["IRGAGE"] = int(subpcp[i].split(",")[5])
    else:
        sub_defaults["IRGAGE"] = None

    if os.path.isfile(variables.path + "\\subtmp.tmp~"):
        sub_defaults["ITGAGE"] = int(subtmp[i].split(",")[5])
    else:
        sub_defaults["ITGAGE"] = None
    
    if os.path.isfile(variables.path + "\\subhmd.tmp~"):
        sub_defaults["IHGAGE"] = int(subhmd[i].split(",")[5])
    else:
        sub_defaults["IHGAGE"] = None

    if os.path.isfile(variables.path + "\\subslr.tmp~"):
        sub_defaults["ISGAGE"] = int(subslr[i].split(",")[5])
    else:
        sub_defaults["ISGAGE"] = None    

    if os.path.isfile(variables.path + "\\subwnd.tmp~"):
        sub_defaults["IWGAGE"] = int(subwnd[i].split(",")[5])
    else:
        sub_defaults["IWGAGE"] = None 


    sub_defaults["CH_L1"] = float(watershed_data[i].split(",")[6])/1000.00000
    sub_defaults["CH_S1"] = float(watershed_data[i].split(",")[8])/100.000000
    sub_defaults["CH_W1"] = float(watershed_data[i].split(",")[9])

    hru_counter = 0
    for hru_line in hrus:
        if int(sub_defaults["SUBBASIN"]) == int(float(hru_line.split(",")[1])):
            hru_counter += 1

    sub_defaults["HRUTOT"] = hru_counter

    sub_defaults = cj.format_data_type(sub_defaults, subrgn)
    sub.insert_row("sub", sub_defaults, True)
sub.disconnect()
