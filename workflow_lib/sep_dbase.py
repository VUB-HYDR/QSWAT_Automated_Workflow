
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
seprgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'seprng', variables.path + "\\seprgn.tmp~")

sep_defaults={} 
for record in seprgn: # Getting a list of parameter names for sep and their defaults
    if record.split(",")[0].strip(" ") != "":
        sep_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the sep to a row in the table sep
"""
sep = mdt.mdb_with_ops(variables.ProjMDB)
sep.clear_table("sep")
sep.RunSQL("""ALTER TABLE "sep" ADD UNIQUE (OID))""",True)

OID = 0
for hru in hrus:    # getting field values from from hrus table
    OID = OID + 1
    sep_defaults["OID"] = OID

    sep_defaults["SUBBASIN"] = int(hru.split(",")[1].split(".")[0])
    sep_defaults["HRU"] = int(hru.split(",")[12][6:10])
    sep_defaults["LANDUSE"] = hru.split(",")[3]
    sep_defaults["SOIL"] = hru.split(",")[5]
    sep_defaults["SLOPE_CD"] = hru.split(",")[7]
    
    sep_defaults = cj.format_data_type(sep_defaults, seprgn)
    sep.insert_row("sep", sep_defaults, True)
sep.disconnect()
