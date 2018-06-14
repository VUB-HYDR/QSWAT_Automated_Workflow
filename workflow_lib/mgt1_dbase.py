
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
mgt1rgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'mgt1rng', variables.path + "\\mgt1rgn.tmp~")
crop = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'crop', variables.path + "\\crop.tmp~")
usersoil = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'usersoil', variables.path + "\\usersoil.tmp~")

mgt1_defaults={} 
for record in mgt1rgn: # Getting a list of parameter names for mgt1 and their defaults
    if record.split(",")[0].strip(" ") != "":
        if (record.split(",")[5][0:4] == "AUTO") or (record.split(",")[5][0:4] == "INTE"):
            if record.split(",")[3] == "na":
                mgt1_defaults[record.split(",")[0]] = int(1)
            else:
                mgt1_defaults[record.split(",")[0]] = int(record.split(",")[3])
        elif (record.split(",")[5][0:4] == "FLOA"):
            mgt1_defaults[record.split(",")[0]] = float(record.split(",")[3])
        elif (record.split(",")[5][0:4] == "TEXT"):
            mgt1_defaults[record.split(",")[0]] = record.split(",")[3]

"""
# here we commit to table the parameters for the hru to a row in the table mgt1
"""

mgt1 = mdt.mdb_with_ops(variables.ProjMDB)
mgt1.RunSQL("""ALTER TABLE "mgt1" ADD UNIQUE (OID))""",True)
mgt1.clear_table("mgt1")

for hru in hrus:    # getting field values from from hrus table
    mgt1_defaults["SUBBASIN"] = int(hru.split(",")[1].split(".")[0])
    mgt1_defaults["HRU"] = int(hru.split(",")[12][6:10])
    mgt1_defaults["OID"] = int(hru.split(",")[0])
    mgt1_defaults["LANDUSE"] = hru.split(",")[3]
    mgt1_defaults["SOIL"] = hru.split(",")[5]
    mgt1_defaults["SLOPE_CD"] = hru.split(",")[7]
    
    HYDR_GROUP = None

    for record in usersoil:
        if mgt1_defaults["SOIL"] == record.split(",")[3].strip(" "):
            HYDR_GROUP = record.split(",")[7].strip(" ")
            break

    #getting CN2 from CN2C field in crop for a given land cover
    for crop_record in crop:
        if mgt1_defaults["LANDUSE"] == crop_record.split(",")[2]:
            # Choice of CN depends on the HYDRGROUP
            if HYDR_GROUP == "A":
                mgt1_defaults["CN2"] = crop_record.split(",")[35]
            elif HYDR_GROUP == "B":
                mgt1_defaults["CN2"] = crop_record.split(",")[36]
            elif HYDR_GROUP == "C":
                mgt1_defaults["CN2"] = crop_record.split(",")[37]
            elif HYDR_GROUP == "D":
                mgt1_defaults["CN2"] = crop_record.split(",")[38]                
            else:   # Fallback
                mgt1_defaults["CN2"] = crop_record.split(",")[36]

            mgt1_defaults["PLANT_ID"] = crop_record.split(",")[1]
            # HUSC in opSchedules?
        else:
            continue
    #if  mgt1_defaults["CN2"] == float(-999):
    #    print "Error: Could not find Curve Number for land use :" + mgt1_defaults["LANDUSE"]
    #    sys.exit()
    mgt1.insert_row("mgt1", mgt1_defaults, True)
    
mgt1.disconnect()
#for hru in hrus:
#    print hru