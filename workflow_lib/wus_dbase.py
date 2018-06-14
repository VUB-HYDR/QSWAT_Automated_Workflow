
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

watersheds = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
wusrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'wusrng', variables.path + "\\wusrgn.tmp~")

wus_defaults={} 
for record in wusrgn: # Getting a list of parameter names for wus and their defaults
    if record.split(",")[0].strip(" ") != "":
        wus_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

#wus_defaults.pop("ALPHA_BF_D")

count_up_fields=[]

for key in wus_defaults:
    if key == "SUBBASIN" or key == "OID":
        continue
    count_up_fields.append(key)


for field in count_up_fields:   #removing the non numbered field-keys fo later numbering
    wus_defaults.pop(field)
    for numbering in range (1,13):
        wus_defaults[field + str(numbering)] = 0

"""
# here we commit to table the parameters for the subbasin to a row in the table wus
"""
wus = mdt.mdb_with_ops(variables.ProjMDB)
wus.clear_table("wus")

OID = 0
for watershed in watersheds:    # getting field values from from subbasins table
    OID = OID + 1
    wus_defaults["OID"] = OID
    wus_defaults["SUBBASIN"] = int(watershed.split(",")[3])

    wus_defaults = cj.format_data_type(wus_defaults, wusrgn)
    wus.insert_row("wus", wus_defaults, True)
wus.disconnect()
