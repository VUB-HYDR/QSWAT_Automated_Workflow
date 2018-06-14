
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
gwrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'gwrng', variables.path + "\\gwrgn.tmp~")

gw_defaults={} 
for record in gwrgn: # Getting a list of parameter names for gw and their defaults
    if record.split(",")[0].strip(" ") != "":
        gw_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

#gw_defaults.pop("ALPHA_BF_D")

"""
# here we commit to table the parameters for the hru to a row in the table gw
"""
gw = mdt.mdb_with_ops(variables.ProjMDB)
gw.connect()
try:
    gw.add_field("gw", "ALPHA_BF_D", "FLOAT")
    gw.disconnect()
except:
    pass

gw.connect()
gw.RunSQL("""ALTER TABLE "gw" ADD UNIQUE (OID))""",True)
gw.clear_table("gw")

OID = 0
for hru in hrus:    # getting field values from from hrus table
    OID = OID + 1
    gw_defaults["OID"] = OID
   
    gw_defaults["SUBBASIN"] = int(hru.split(",")[1].split(".")[0])
    gw_defaults["HRU"] = int(hru.split(",")[12][6:10])
    gw_defaults["LANDUSE"] = hru.split(",")[3]
    gw_defaults["SOIL"] = hru.split(",")[5]
    gw_defaults["SLOPE_CD"] = hru.split(",")[7]
    
    gw_defaults = cj.format_data_type(gw_defaults, gwrgn)
    gw.insert_row("gw", gw_defaults, True)
gw.disconnect()
