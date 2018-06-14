
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

rtergn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'rterng', variables.path + "\\rtergn.tmp~")
reach_data = cj.extract_table_from_mdb(variables.ProjMDB, 'Reach', variables.path + "\\reach_data.tmp~")

rte_defaults={} 
for record in rtergn: # Getting a list of parameter names for rte and their defaults
    if record.split(",")[0].strip(" ") != "":
        rte_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the rte to a row in the table rte
"""
rte = mdt.mdb_with_ops(variables.ProjMDB)
rte.clear_table("rte")

for reach in reach_data:    # getting field values from from Reach table
    rte_defaults["SUBBASIN"] = reach.split(",")[6]#.split(".")[0]
    rte_defaults["OID"] = reach.split(",")[0]

    rte_defaults["CH_W2"] = reach.split(",")[11]
    rte_defaults["CH_D"] = reach.split(",")[12]
    rte_defaults["CH_S2"] = float(reach.split(",")[10])/100.00000
    rte_defaults["CH_L2"] = float(reach.split(",")[9])/1000.00000
    rte_defaults["CH_WDR"] = float(rte_defaults["CH_W2"])/float(rte_defaults["CH_D"])

    rte_defaults = cj.format_data_type(rte_defaults, rtergn)
    rte.insert_row("rte", rte_defaults, True)
rte.disconnect()
