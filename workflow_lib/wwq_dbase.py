
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

wwqrng = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'wwqrng', variables.path + "\\wwqrng.tmp~")

wwq_defaults={} 
for record in wwqrng: # Getting a list of parameter names for wwq and their defaults
    if record.split(",")[0].strip(" ") != "":
        wwq_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

"""
# here we commit to table the parameters for the wwq to the row in the table wwq
"""
wwq = mdt.mdb_with_ops(variables.ProjMDB)
wwq.clear_table("wwq")

wwq_defaults["OID"] = 1

wwq_defaults = cj.format_data_type(wwq_defaults, wwqrng)
wwq.insert_row("wwq", wwq_defaults, True)
wwq.disconnect()
