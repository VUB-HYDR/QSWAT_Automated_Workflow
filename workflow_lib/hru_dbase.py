
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
hrurgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'hrurng', variables.path + "\\hrurgn.tmp~")
crop = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'crop', variables.path + "\\crop.tmp~")

hru_defaults={} 
for record in hrurgn: # Getting a list of parameter names for hru and their defaults
    if record.split(",")[0].strip(" ") != "":
        hru_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

fields_to_add = ["POT_SOLP", "POT_K", "N_REDUC", "N_LAG", "N_LN", "N_LNCO", "SURLAG", "R2ADJ"] #Adding fields, that are missing from the table in this order

"""
# here we commit to table the parameters for the hru to a row in the table hru
"""
hru = mdt.mdb_with_ops(variables.ProjMDB)
hru.connect()

for field in fields_to_add:
    try:
        hru.add_field("hru", field, "FLOAT")
        hru.disconnect()
    except:
        pass

hru.connect()
hru.RunSQL("""ALTER TABLE "hru" ADD UNIQUE (OID))""",True)
hru.clear_table("hru")

for hruID in hrus:    # getting field values from from hrus table

    hru_defaults["OID"] = hruID.split(",")[0]
    hru_defaults["SUBBASIN"] = hruID.split(",")[1].split(".")[0]
    hru_defaults["HRU"] = hruID.split(",")[12][6:10]
    hru_defaults["LANDUSE"] = hruID.split(",")[3]
    hru_defaults["SOIL"] = hruID.split(",")[5]
    hru_defaults["SLOPE_CD"] = hruID.split(",")[7]
    hru_defaults["HRU_SLP"] = float(hruID.split(",")[9])/100
    hru_defaults["HRU_FR"] = float(hruID.split(",")[8])/float(hruID.split(",")[2])  # Dividing columns from hrus table in Project Batabase
   
    #getting OV_N from crop table based on land use
    for crop_record in crop:
        if hru_defaults["LANDUSE"] == crop_record.split(",")[2]:
            hru_defaults["OV_N"] = crop_record.split(",")[34]

    hru_defaults = cj.format_data_type(hru_defaults, hrurgn)
    hru.insert_row("hru", hru_defaults, True)
hru.disconnect()
