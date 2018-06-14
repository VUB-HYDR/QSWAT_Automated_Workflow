
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
chmrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'chmrng', variables.path + "\\chmrgn.tmp~")

chm_defaults={}

for record in chmrgn: # Getting a list of parameter names for chm and their defaults
    if record.split(",")[0].strip(" ") != "":
        chm_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

#chm_defaults.pop("ALPHA_BF_D")

count_up_fields = ["SOL_NO3", "SOL_ORGN", "SOL_LABP", "SOL_ORGP", "PESTNAME", "PLTPST", "SOLPST", "PSTENR", "PPERCO_SUB"]

chm_defaults["PESTNAME"] = None  #It overrided an if statement in cj_functions formating function

for field in count_up_fields:   #removing the non numbered field-keys fo later numbering
    for numbering in range (1,11):
        chm_defaults[field + str(numbering)] =  chm_defaults[field]
    chm_defaults.pop(field)

"""
# here we commit to table the parameters for the basin to a row in the table chm
"""
chm = mdt.mdb_with_ops(variables.ProjMDB)
chm.connect()
chm.clear_table("chm")

hold_val = 0
LocalHRU = 0
for hru in hrus:    # getting field values from from watershed table
    chm_defaults["OID"] =hru.split(",")[0]
    chm_defaults["SUBBASIN"] = hru.split(",")[1]
    
    if chm_defaults["SUBBASIN"] == hold_val:
        LocalHRU += 1
    else:
        LocalHRU = 1

    hold_val = chm_defaults["SUBBASIN"]

    chm_defaults["HRU"] = LocalHRU
    chm_defaults["LANDUSE"] = hru.split(",")[3]
    chm_defaults["SOIL"] = hru.split(",")[5]
    chm_defaults["SLOPE_CD"] = hru.split(",")[7]

    chm_defaults = cj.format_data_type(chm_defaults, chmrgn)
    chm.insert_row("chm", chm_defaults, True)
chm.disconnect()
