
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
mgt2rgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'mgt2rng', variables.path + "\\mgt2rgn.tmp~")
crop = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'crop', variables.path + "\\crop.tmp~")
opSchedules = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'OpSchedules', variables.path + "\\opSchedules.tmp~")


mgt2_defaults={} 
for record in mgt2rgn: # Getting a list of parameter names for mgt2 and their defaults
    if record.split(",")[0].strip(" ") != "":
        mgt2_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]
        #if (record.split(",")[5][0:4] == "AUTO") or (record.split(",")[5][0:4] == "INTE"):
        #    if record.split(",")[3] == "na":
        #        mgt2_defaults[record.split(",")[0].strip("\[").strip("\]")] = int(1)
        #    else:
        #        mgt2_defaults[record.split(",")[0].strip("\[").strip("\]")] = int(record.split(",")[3])
        #elif (record.split(",")[5][0:4] == "FLOA"):
        #    mgt2_defaults[record.split(",")[0].strip("\[").strip("\]")] = float(record.split(",")[3])
        #elif (record.split(",")[5][0:4] == "TEXT"):
        #    mgt2_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]
"""
# here we commit to table the parameters for the hru to a row in the table mgt2
"""
mgt2 = mdt.mdb_with_ops(variables.ProjMDB)

mgt2.clear_table("mgt2")

mgt2.RunSQL("""ALTER TABLE "mgt2" ADD UNIQUE (OID))""",True) #doesnt seem to help with having a ordered properly ordered table extract

OID = 0
for hru in hrus:    # getting field values from from hrus table
    mgt2_defaults["SUBBASIN"] = int(hru.split(",")[1].split(".")[0])
    mgt2_defaults["HRU"] = int(hru.split(",")[12][6:10])
    mgt2_defaults["LANDUSE"] = hru.split(",")[3]
    mgt2_defaults["SOIL"] = hru.split(",")[5]
    mgt2_defaults["SLOPE_CD"] = hru.split(",")[7]

    for crop_record in crop:
        if mgt2_defaults["LANDUSE"] == crop_record.split(",")[2]:
            mgt2_defaults["PLANT_ID"] = crop_record.split(",")[1]
            OpSchedule = crop_record.split(",")[46]
            break

    for op_group in opSchedules:
        if op_group.split(",")[0].strip("\n") == OpSchedule.strip("\n"): 
            OID += 1

            mgt2_defaults["OID"] = int(OID)

            mgt2_defaults["CROP"] = op_group.split(",")[6]
            mgt2_defaults["YEAR"] = op_group.split(",")[7]
            mgt2_defaults["MONTH"] = None #op_group.split(",")[8]
            mgt2_defaults["DAY"] = None #op_group.split(",")[9]
            mgt2_defaults["HUSC"] = op_group.split(",")[10]
            mgt2_defaults["MGT_OP"] = op_group.split(",")[11]
            mgt2_defaults["HEATUNITS"] = op_group.split(",")[12]
            #mgt2_defaults["PLANT_ID"] = op_group.split(",")[13]
            mgt2_defaults["CURYR_MAT"] = op_group.split(",")[14]
            mgt2_defaults["LAI_INIT"] = op_group.split(",")[15]
            mgt2_defaults["BIO_INIT"] = op_group.split(",")[16]
            mgt2_defaults["HI_TARG"] = op_group.split(",")[17]
            mgt2_defaults["BIO_TARG"] = op_group.split(",")[18]
            mgt2_defaults["CNOP"] = op_group.split(",")[19]
            mgt2_defaults["IRR_AMT"] = op_group.split(",")[20]
            mgt2_defaults["FERT_ID"] = op_group.split(",")[21]
            mgt2_defaults["FRT_KG"] = op_group.split(",")[22]
            mgt2_defaults["FRT_SURFACE"] = op_group.split(",")[23]
            mgt2_defaults["PEST_ID"] = op_group.split(",")[24]
            mgt2_defaults["PST_KG"] = op_group.split(",")[25]
            mgt2_defaults["TILLAGE_ID"] = op_group.split(",")[26]
            mgt2_defaults["HARVEFF"] = op_group.split(",")[27]
            mgt2_defaults["HI_OVR"] = op_group.split(",")[28]
            mgt2_defaults["GRZ_DAYS"] = op_group.split(",")[29]
            mgt2_defaults["MANURE_ID"] = op_group.split(",")[30]
            mgt2_defaults["BIO_EAT"] = op_group.split(",")[31]
            mgt2_defaults["BIO_TRMP"] = op_group.split(",")[32]
            mgt2_defaults["MANURE_KG"] = op_group.split(",")[33]
            mgt2_defaults["WSTRS_ID"] = op_group.split(",")[34]
            mgt2_defaults["AUTO_WSTRS"] = op_group.split(",")[35]
            mgt2_defaults["AFERT_ID"] = op_group.split(",")[36]
            mgt2_defaults["AUTO_NSTRS"] = op_group.split(",")[37]
            mgt2_defaults["AUTO_NAPP"] = op_group.split(",")[38]
            mgt2_defaults["AUTO_NYR"] = op_group.split(",")[39]
            mgt2_defaults["AUTO_EFF"] = op_group.split(",")[40]
            mgt2_defaults["AFRT_SURFACE"] = op_group.split(",")[41]
            mgt2_defaults["SWEEPEFF"] = op_group.split(",")[42]
            mgt2_defaults["FR_CURB"] = op_group.split(",")[43]
            mgt2_defaults["IMP_TRIG"] = op_group.split(",")[44]
            mgt2_defaults["FERT_DAYS"] = op_group.split(",")[45]
            mgt2_defaults["CFRT_ID"] = op_group.split(",")[46]
            mgt2_defaults["IFRT_FREQ"] = op_group.split(",")[47]
            mgt2_defaults["CFRT_KG"] = op_group.split(",")[48]
            mgt2_defaults["PST_DEP"] = op_group.split(",")[49]
            mgt2_defaults["IHV_GBM"] = op_group.split(",")[50]
            mgt2_defaults["IRR_SALT"] = op_group.split(",")[51]
            mgt2_defaults["IRR_EFM"] = op_group.split(",")[52]
            mgt2_defaults["IRR_SQ"] = op_group.split(",")[53]
            mgt2_defaults["IRR_EFF"] = op_group.split(",")[54]
            mgt2_defaults["IRR_MX"] = op_group.split(",")[55]
            mgt2_defaults["IRR_ASQ"] = op_group.split(",")[56]
            mgt2_defaults["CPST_ID"] = op_group.split(",")[57]
            mgt2_defaults["PEST_DAYS"] = op_group.split(",")[58]
            mgt2_defaults["IPEST_FREQ"] = op_group.split(",")[59]
            mgt2_defaults["CPST_KG"] = op_group.split(",")[60]
            mgt2_defaults["BURN_FRLB"] = op_group.split(",")[61]
            mgt2_defaults["OP_NUM"] = op_group.split(",")[62]
            mgt2_defaults["IRR_SC"] = op_group.split(",")[63]
            mgt2_defaults["IRR_NO"] = op_group.split(",")[64]
            mgt2_defaults["IRR_SCA"] = op_group.split(",")[65]
            mgt2_defaults["IRR_NOA"] = op_group.split(",")[66]

            mgt2_defaults = cj.format_data_type(mgt2_defaults, mgt2rgn)

            #mgt2_defaults["MGT_OP"]
            mgt2.insert_row("mgt2", mgt2_defaults, True)

mgt2.disconnect()
