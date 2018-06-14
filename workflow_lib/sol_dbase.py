
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

hrus = cj.extract_table_from_mdb(variables.ProjMDB, 'hrus', variables.path + "\\hrus.tmp~")
solrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'solrng', variables.path + "\\solrgn.tmp~")
usersoils = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'usersoil', variables.path + "\\usersoils.tmp~")

sol_defaults={} 
for record in solrgn: # Getting a list of parameter names for sol and their defaults
    if record.split(",")[0].strip(" ") != "":
        sol_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

#sol_defaults.pop("ALPHA_BF_D")

count_up_fields = ["SOL_Z", "SOL_BD", "SOL_AWC", "SOL_K", "SOL_CBN", "CLAY", "SILT", "SAND", "ROCK", "SOL_ALB", "USLE_K", "SOL_EC", "SOL_CAL", "SOL_PH"]

for field in count_up_fields:   #removing the non numbered field-keys fo later numbering
    sol_defaults.pop(field)
    for numbering in range (1,11):
        sol_defaults[field + str(numbering)] = 0


"""
# here we commit to table the parameters for the hru to a row in the table sol
"""
sol = mdt.mdb_with_ops(variables.ProjMDB)
sol.clear_table("sol")
sol.RunSQL("""ALTER TABLE "sol" ADD UNIQUE (OID))""",True)

OID = 0
for hru in hrus:    # getting field values from from hrus table
    OID = OID + 1
    sol_defaults["OID"] = OID

    sol_defaults["SUBBASIN"] = int(hru.split(",")[1].split(".")[0])
    sol_defaults["HRU"] = int(hru.split(",")[12][6:10])
    sol_defaults["LANDUSE"] = hru.split(",")[3]
    sol_defaults["SLOPE_CD"] = hru.split(",")[7]
    sol_defaults["SOIL"] = hru.split(",")[5]
    sol_defaults["SNAM"] = hru.split(",")[5]

    count = 0
    for usersoil in usersoils:
        if usersoil.split(",")[3] ==  sol_defaults["SOIL"]:
            # taking the entire row for sol file
            sol_defaults["NLAYERS"] = usersoil.split(",")[6]
            sol_defaults["HYDGRP"] = usersoil.split(",")[7]
            sol_defaults["SOL_ZMX"] = usersoil.split(",")[8]
            sol_defaults["ANION_EXCL"] = usersoil.split(",")[9]
            sol_defaults["SOL_CRK"] = usersoil.split(",")[10]
            sol_defaults["TEXTURE"] = usersoil.split(",")[11]
            sol_defaults["SOL_Z1"] = usersoil.split(",")[12]
            sol_defaults["SOL_BD1"] = usersoil.split(",")[13]
            sol_defaults["SOL_AWC1"] = usersoil.split(",")[14]
            sol_defaults["SOL_K1"] = usersoil.split(",")[15]
            sol_defaults["SOL_CBN1"] = usersoil.split(",")[16]
            sol_defaults["CLAY1"] = usersoil.split(",")[17]
            sol_defaults["SILT1"] = usersoil.split(",")[18]
            sol_defaults["SAND1"] = usersoil.split(",")[19]
            sol_defaults["ROCK1"] = usersoil.split(",")[20]
            sol_defaults["SOL_ALB1"] = usersoil.split(",")[21]
            sol_defaults["USLE_K1"] = usersoil.split(",")[22]
            sol_defaults["SOL_EC1"] = usersoil.split(",")[23]
            sol_defaults["SOL_Z2"] = usersoil.split(",")[24]
            sol_defaults["SOL_BD2"] = usersoil.split(",")[25]
            sol_defaults["SOL_AWC2"] = usersoil.split(",")[26]
            sol_defaults["SOL_K2"] = usersoil.split(",")[27]
            sol_defaults["SOL_CBN2"] = usersoil.split(",")[28]
            sol_defaults["CLAY2"] = usersoil.split(",")[29]
            sol_defaults["SILT2"] = usersoil.split(",")[30]
            sol_defaults["SAND2"] = usersoil.split(",")[31]
            sol_defaults["ROCK2"] = usersoil.split(",")[32]
            sol_defaults["SOL_ALB2"] = usersoil.split(",")[33]
            sol_defaults["USLE_K2"] = usersoil.split(",")[34]
            sol_defaults["SOL_EC2"] = usersoil.split(",")[35]
            sol_defaults["SOL_Z3"] = usersoil.split(",")[36]
            sol_defaults["SOL_BD3"] = usersoil.split(",")[37]
            sol_defaults["SOL_AWC3"] = usersoil.split(",")[38]
            sol_defaults["SOL_K3"] = usersoil.split(",")[39]
            sol_defaults["SOL_CBN3"] = usersoil.split(",")[40]
            sol_defaults["CLAY3"] = usersoil.split(",")[41]
            sol_defaults["SILT3"] = usersoil.split(",")[42]
            sol_defaults["SAND3"] = usersoil.split(",")[43]
            sol_defaults["ROCK3"] = usersoil.split(",")[44]
            sol_defaults["SOL_ALB3"] = usersoil.split(",")[45]
            sol_defaults["USLE_K3"] = usersoil.split(",")[46]
            sol_defaults["SOL_EC3"] = usersoil.split(",")[47]
            sol_defaults["SOL_Z4"] = usersoil.split(",")[48]
            sol_defaults["SOL_BD4"] = usersoil.split(",")[49]
            sol_defaults["SOL_AWC4"] = usersoil.split(",")[50]
            sol_defaults["SOL_K4"] = usersoil.split(",")[51]
            sol_defaults["SOL_CBN4"] = usersoil.split(",")[52]
            sol_defaults["CLAY4"] = usersoil.split(",")[53]
            sol_defaults["SILT4"] = usersoil.split(",")[54]
            sol_defaults["SAND4"] = usersoil.split(",")[55]
            sol_defaults["ROCK4"] = usersoil.split(",")[56]
            sol_defaults["SOL_ALB4"] = usersoil.split(",")[57]
            sol_defaults["USLE_K4"] = usersoil.split(",")[58]
            sol_defaults["SOL_EC4"] = usersoil.split(",")[59]
            sol_defaults["SOL_Z5"] = usersoil.split(",")[60]
            sol_defaults["SOL_BD5"] = usersoil.split(",")[61]
            sol_defaults["SOL_AWC5"] = usersoil.split(",")[62]
            sol_defaults["SOL_K5"] = usersoil.split(",")[63]
            sol_defaults["SOL_CBN5"] = usersoil.split(",")[64]
            sol_defaults["CLAY5"] = usersoil.split(",")[65]
            sol_defaults["SILT5"] = usersoil.split(",")[66]
            sol_defaults["SAND5"] = usersoil.split(",")[67]
            sol_defaults["ROCK5"] = usersoil.split(",")[68]
            sol_defaults["SOL_ALB5"] = usersoil.split(",")[69]
            sol_defaults["USLE_K5"] = usersoil.split(",")[70]
            sol_defaults["SOL_EC5"] = usersoil.split(",")[71]
            sol_defaults["SOL_Z6"] = usersoil.split(",")[72]
            sol_defaults["SOL_BD6"] = usersoil.split(",")[73]
            sol_defaults["SOL_AWC6"] = usersoil.split(",")[74]
            sol_defaults["SOL_K6"] = usersoil.split(",")[75]
            sol_defaults["SOL_CBN6"] = usersoil.split(",")[76]
            sol_defaults["CLAY6"] = usersoil.split(",")[77]
            sol_defaults["SILT6"] = usersoil.split(",")[78]
            sol_defaults["SAND6"] = usersoil.split(",")[79]
            sol_defaults["ROCK6"] = usersoil.split(",")[80]
            sol_defaults["SOL_ALB6"] = usersoil.split(",")[81]
            sol_defaults["USLE_K6"] = usersoil.split(",")[82]
            sol_defaults["SOL_EC6"] = usersoil.split(",")[83]
            sol_defaults["SOL_Z7"] = usersoil.split(",")[84]
            sol_defaults["SOL_BD7"] = usersoil.split(",")[85]
            sol_defaults["SOL_AWC7"] = usersoil.split(",")[86]
            sol_defaults["SOL_K7"] = usersoil.split(",")[87]
            sol_defaults["SOL_CBN7"] = usersoil.split(",")[88]
            sol_defaults["CLAY7"] = usersoil.split(",")[89]
            sol_defaults["SILT7"] = usersoil.split(",")[90]
            sol_defaults["SAND7"] = usersoil.split(",")[91]
            sol_defaults["ROCK7"] = usersoil.split(",")[92]
            sol_defaults["SOL_ALB7"] = usersoil.split(",")[93]
            sol_defaults["USLE_K7"] = usersoil.split(",")[94]
            sol_defaults["SOL_EC7"] = usersoil.split(",")[95]
            sol_defaults["SOL_Z8"] = usersoil.split(",")[96]
            sol_defaults["SOL_BD8"] = usersoil.split(",")[97]
            sol_defaults["SOL_AWC8"] = usersoil.split(",")[98]
            sol_defaults["SOL_K8"] = usersoil.split(",")[99]
            sol_defaults["SOL_CBN8"] = usersoil.split(",")[100]
            sol_defaults["CLAY8"] = usersoil.split(",")[101]
            sol_defaults["SILT8"] = usersoil.split(",")[102]
            sol_defaults["SAND8"] = usersoil.split(",")[103]
            sol_defaults["ROCK8"] = usersoil.split(",")[104]
            sol_defaults["SOL_ALB8"] = usersoil.split(",")[105]
            sol_defaults["USLE_K8"] = usersoil.split(",")[106]
            sol_defaults["SOL_EC8"] = usersoil.split(",")[107]
            sol_defaults["SOL_Z9"] = usersoil.split(",")[108]
            sol_defaults["SOL_BD9"] = usersoil.split(",")[109]
            sol_defaults["SOL_AWC9"] = usersoil.split(",")[110]
            sol_defaults["SOL_K9"] = usersoil.split(",")[111]
            sol_defaults["SOL_CBN9"] = usersoil.split(",")[112]
            sol_defaults["CLAY9"] = usersoil.split(",")[113]
            sol_defaults["SILT9"] = usersoil.split(",")[114]
            sol_defaults["SAND9"] = usersoil.split(",")[115]
            sol_defaults["ROCK9"] = usersoil.split(",")[116]
            sol_defaults["SOL_ALB9"] = usersoil.split(",")[117]
            sol_defaults["USLE_K9"] = usersoil.split(",")[118]
            sol_defaults["SOL_EC9"] = usersoil.split(",")[119]
            sol_defaults["SOL_Z10"] = usersoil.split(",")[120]
            sol_defaults["SOL_BD10"] = usersoil.split(",")[121]
            sol_defaults["SOL_AWC10"] = usersoil.split(",")[122]
            sol_defaults["SOL_K10"] = usersoil.split(",")[123]
            sol_defaults["SOL_CBN10"] = usersoil.split(",")[124]
            sol_defaults["CLAY10"] = usersoil.split(",")[125]
            sol_defaults["SILT10"] = usersoil.split(",")[126]
            sol_defaults["SAND10"] = usersoil.split(",")[127]
            sol_defaults["ROCK10"] = usersoil.split(",")[128]
            sol_defaults["SOL_ALB10"] = usersoil.split(",")[129]
            sol_defaults["USLE_K10"] = usersoil.split(",")[130]
            sol_defaults["SOL_EC10"] = usersoil.split(",")[131]

            # Set the rest to zeros as they are not in the defaults table of user soils
            sol_defaults["SOL_CAL2"] = 0 #usersoil.split(",")[131]
            sol_defaults["SOL_CAL3"] = 0 #usersoil.split(",")[132]
            sol_defaults["SOL_CAL4"] = 0 #usersoil.split(",")[133]
            sol_defaults["SOL_CAL5"] = 0 #usersoil.split(",")[134]
            sol_defaults["SOL_CAL6"] = 0 #usersoil.split(",")[135]
            sol_defaults["SOL_CAL7"] = 0 #usersoil.split(",")[136]
            sol_defaults["SOL_CAL8"] = 0 #usersoil.split(",")[137]
            sol_defaults["SOL_CAL9"] = 0 #usersoil.split(",")[138]
            sol_defaults["SOL_CAL10"] = 0 #usersoil.split(",")[139]
            sol_defaults["SOL_PH1"] = 0 #usersoil.split(",")[140]
            sol_defaults["SOL_PH2"] = 0 #usersoil.split(",")[141]
            sol_defaults["SOL_PH3"] = 0 #usersoil.split(",")[142]
            sol_defaults["SOL_PH4"] = 0 #usersoil.split(",")[143]
            sol_defaults["SOL_PH5"] = 0 #usersoil.split(",")[144]
            sol_defaults["SOL_PH6"] = 0 #usersoil.split(",")[145]
            sol_defaults["SOL_PH7"] = 0 #usersoil.split(",")[146]
            sol_defaults["SOL_PH8"] = 0 #usersoil.split(",")[147]
            sol_defaults["SOL_PH9"] = 0 #usersoil.split(",")[148]
            sol_defaults["SOL_PH10"] = 0 #usersoil.split(",")[149]

            break
    sol_defaults = cj.format_data_type(sol_defaults, solrgn)
    sol.insert_row("sol", sol_defaults, True)
sol.disconnect()
