
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

watersheds = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
swqrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'swqrng', variables.path + "\\swqrgn.tmp~")

swq_defaults={} 
for record in swqrgn: # Getting a list of parameter names for swq and their defaults
    if record.split(",")[0].strip(" ") != "":
        swq_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the subbasin to a row in the table swq
"""
swq = mdt.mdb_with_ops(variables.ProjMDB)
swq.clear_table("swq")

OID = 0
for watershed in watersheds:    # getting field values from from watershed table
    OID = OID + 1
    swq_defaults["OID"] = OID
    swq_defaults["SUBBASIN"] = int(watershed.split(",")[3])

    swq_defaults = cj.format_data_type(swq_defaults, swqrgn)
    swq.insert_row("swq", swq_defaults, True)
swq.disconnect()
