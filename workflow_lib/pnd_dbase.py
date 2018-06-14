
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

Watersheds = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
pndrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'pndrng', variables.path + "\\pndrgn.tmp~")

pnd_defaults={} 
for record in pndrgn: # Getting a list of parameter names for pnd and their defaults
    if record.split(",")[0].strip(" ") != "":
        pnd_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the pnd to a row in the table pnd
"""
pnd = mdt.mdb_with_ops(variables.ProjMDB)
pnd.clear_table("pnd")
pnd.RunSQL("""ALTER TABLE "pnd" ADD UNIQUE (OID))""",True)


for Watershed in Watersheds:    # getting field values from from hrus table
    pnd_defaults["SUBBASIN"] = Watershed.split(",")[3]
    pnd_defaults["OID"] = Watershed.split(",")[3]

    pnd_defaults = cj.format_data_type(pnd_defaults, pndrgn)
    pnd.insert_row("pnd", pnd_defaults, True)
pnd.disconnect()
