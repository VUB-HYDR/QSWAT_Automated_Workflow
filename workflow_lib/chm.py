import init_file as variables
import cj_function_lib as cj
from datetime import datetime

chm_table = cj.extract_table_from_mdb(variables.ProjMDB, "chm", variables.path + "\\chm.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for chm_record in chm_table:
    # Hru ID
    WshedHRU = chm_record.split(",")[0].strip('"')
    SubBasin = chm_record.split(",")[1].strip('"')
    HRU_No = chm_record.split(",")[2].strip('"')
    Luse = chm_record.split(",")[3].strip('"')
    Soil = chm_record.split(",")[4].strip('"')
    Slope = chm_record.split(",")[5].strip('"')

    # Parameters
    SOL_NO31 = chm_record.split(",")[6].strip('"')
    SOL_NO32 = chm_record.split(",")[7].strip('"')
    SOL_NO33 = chm_record.split(",")[8].strip('"')
    SOL_NO34 = chm_record.split(",")[9].strip('"')
    SOL_NO35 = chm_record.split(",")[10].strip('"')
    SOL_NO36 = chm_record.split(",")[11].strip('"')
    SOL_NO37 = chm_record.split(",")[12].strip('"')
    SOL_NO38 = chm_record.split(",")[13].strip('"')
    SOL_NO39 = chm_record.split(",")[14].strip('"')
    SOL_NO310 = chm_record.split(",")[15].strip('"')
    SOL_ORGN1 = chm_record.split(",")[16].strip('"')
    SOL_ORGN2 = chm_record.split(",")[17].strip('"')
    SOL_ORGN3 = chm_record.split(",")[18].strip('"')
    SOL_ORGN4 = chm_record.split(",")[19].strip('"')
    SOL_ORGN5 = chm_record.split(",")[20].strip('"')
    SOL_ORGN6 = chm_record.split(",")[21].strip('"')
    SOL_ORGN7 = chm_record.split(",")[22].strip('"')
    SOL_ORGN8 = chm_record.split(",")[23].strip('"')
    SOL_ORGN9 = chm_record.split(",")[24].strip('"')
    SOL_ORGN10 = chm_record.split(",")[25].strip('"')
    SOL_LABP1 = chm_record.split(",")[26].strip('"')
    SOL_LABP2 = chm_record.split(",")[27].strip('"')
    SOL_LABP3 = chm_record.split(",")[28].strip('"')
    SOL_LABP4 = chm_record.split(",")[29].strip('"')
    SOL_LABP5 = chm_record.split(",")[30].strip('"')
    SOL_LABP6 = chm_record.split(",")[31].strip('"')
    SOL_LABP7 = chm_record.split(",")[32].strip('"')
    SOL_LABP8 = chm_record.split(",")[33].strip('"')
    SOL_LABP9 = chm_record.split(",")[34].strip('"')
    SOL_LABP10 = chm_record.split(",")[35].strip('"')
    SOL_ORGP1 = chm_record.split(",")[36].strip('"')
    SOL_ORGP2 = chm_record.split(",")[37].strip('"')
    SOL_ORGP3 = chm_record.split(",")[38].strip('"')
    SOL_ORGP4 = chm_record.split(",")[39].strip('"')
    SOL_ORGP5 = chm_record.split(",")[40].strip('"')
    SOL_ORGP6 = chm_record.split(",")[41].strip('"')
    SOL_ORGP7 = chm_record.split(",")[42].strip('"')
    SOL_ORGP8 = chm_record.split(",")[43].strip('"')
    SOL_ORGP9 = chm_record.split(",")[44].strip('"')
    SOL_ORGP10 = chm_record.split(",")[45].strip('"')
    PESTNAME1 = chm_record.split(",")[46].strip('"')
    PESTNAME2 = chm_record.split(",")[47].strip('"')
    PESTNAME3 = chm_record.split(",")[48].strip('"')
    PESTNAME4 = chm_record.split(",")[49].strip('"')
    PESTNAME5 = chm_record.split(",")[50].strip('"')
    PESTNAME6 = chm_record.split(",")[51].strip('"')
    PESTNAME7 = chm_record.split(",")[52].strip('"')
    PESTNAME8 = chm_record.split(",")[53].strip('"')
    PESTNAME9 = chm_record.split(",")[54].strip('"')
    PESTNAME10 = chm_record.split(",")[55].strip('"')
    PLTPST1 = chm_record.split(",")[56].strip('"')
    PLTPST2 = chm_record.split(",")[57].strip('"')
    PLTPST3 = chm_record.split(",")[58].strip('"')
    PLTPST4 = chm_record.split(",")[59].strip('"')
    PLTPST5 = chm_record.split(",")[60].strip('"')
    PLTPST6 = chm_record.split(",")[61].strip('"')
    PLTPST7 = chm_record.split(",")[62].strip('"')
    PLTPST8 = chm_record.split(",")[63].strip('"')
    PLTPST9 = chm_record.split(",")[64].strip('"')
    PLTPST10 = chm_record.split(",")[65].strip('"')
    SOLPST1 = chm_record.split(",")[66].strip('"')
    SOLPST2 = chm_record.split(",")[67].strip('"')
    SOLPST3 = chm_record.split(",")[68].strip('"')
    SOLPST4 = chm_record.split(",")[69].strip('"')
    SOLPST5 = chm_record.split(",")[70].strip('"')
    SOLPST6 = chm_record.split(",")[71].strip('"')
    SOLPST7 = chm_record.split(",")[72].strip('"')
    SOLPST8 = chm_record.split(",")[73].strip('"')
    SOLPST9 = chm_record.split(",")[74].strip('"')
    SOLPST10 = chm_record.split(",")[75].strip('"')
    PSTENR1 = chm_record.split(",")[76].strip('"')
    PSTENR2 = chm_record.split(",")[77].strip('"')
    PSTENR3 = chm_record.split(",")[78].strip('"')
    PSTENR4 = chm_record.split(",")[79].strip('"')
    PSTENR5 = chm_record.split(",")[80].strip('"')
    PSTENR6 = chm_record.split(",")[81].strip('"')
    PSTENR7 = chm_record.split(",")[82].strip('"')
    PSTENR8 = chm_record.split(",")[83].strip('"')
    PSTENR9 = chm_record.split(",")[84].strip('"')
    PSTENR10 = chm_record.split(",")[85].strip('"')
    PPERCO_SUB1 = chm_record.split(",")[86].strip('"')
    PPERCO_SUB2 = chm_record.split(",")[87].strip('"')
    PPERCO_SUB3 = chm_record.split(",")[88].strip('"')
    PPERCO_SUB4 = chm_record.split(",")[89].strip('"')
    PPERCO_SUB5 = chm_record.split(",")[90].strip('"')
    PPERCO_SUB6 = chm_record.split(",")[91].strip('"')
    PPERCO_SUB7 = chm_record.split(",")[92].strip('"')
    PPERCO_SUB8 = chm_record.split(",")[93].strip('"')
    PPERCO_SUB9 = chm_record.split(",")[94].strip('"')
    PPERCO_SUB10 = chm_record.split(",")[95].strip('"')


    # Building String
    chm_file = " .chm file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + "Soil Nutrient Data" + \
        "\n" + " Soil Layer               :           1           2           3           4           5           6           7           8           9          10" + \
        "\n" + " Soil NO3 [mg/kg]         :" + cj.trailing_spaces(12, SOL_NO31, 2) 	+ cj.trailing_spaces(12, SOL_NO32, 2) 	+ cj.trailing_spaces(12, SOL_NO33, 2) 	+ cj.trailing_spaces(12, SOL_NO34, 2) 	+ cj.trailing_spaces(12, SOL_NO35, 2) 	+ cj.trailing_spaces(12, SOL_NO36, 2) 	+ cj.trailing_spaces(12, SOL_NO37, 2) 	+ cj.trailing_spaces(12, SOL_NO38, 2) 	+ cj.trailing_spaces(12, SOL_NO39, 2) 	+ cj.trailing_spaces(12, SOL_NO310, 2) + \
        "\n" + " Soil organic N [mg/kg]   :" + cj.trailing_spaces(12, SOL_ORGN1, 2) 	+ cj.trailing_spaces(12, SOL_ORGN2, 2) 	+ cj.trailing_spaces(12, SOL_ORGN3, 2) 	+ cj.trailing_spaces(12, SOL_ORGN4, 2) 	+ cj.trailing_spaces(12, SOL_ORGN5, 2) 	+ cj.trailing_spaces(12, SOL_ORGN6, 2) 	+ cj.trailing_spaces(12, SOL_ORGN7, 2) 	+ cj.trailing_spaces(12, SOL_ORGN8, 2) 	+ cj.trailing_spaces(12, SOL_ORGN9, 2) 	+ cj.trailing_spaces(12, SOL_ORGN10, 2) + \
        "\n" + " Soil labile P [mg/kg]    :" + cj.trailing_spaces(12, SOL_LABP1, 2) 	+ cj.trailing_spaces(12, SOL_LABP2, 2) 	+ cj.trailing_spaces(12, SOL_LABP3, 2) 	+ cj.trailing_spaces(12, SOL_LABP4, 2) 	+ cj.trailing_spaces(12, SOL_LABP5, 2) 	+ cj.trailing_spaces(12, SOL_LABP6, 2) 	+ cj.trailing_spaces(12, SOL_LABP7, 2) 	+ cj.trailing_spaces(12, SOL_LABP8, 2) 	+ cj.trailing_spaces(12, SOL_LABP9, 2) 	+ cj.trailing_spaces(12, SOL_LABP10, 2) + \
        "\n" + " Soil organic P [mg/kg]   :" + cj.trailing_spaces(12, SOL_ORGP1, 2) 	+ cj.trailing_spaces(12, SOL_ORGP2, 2) 	+ cj.trailing_spaces(12, SOL_ORGP3, 2) 	+ cj.trailing_spaces(12, SOL_ORGP4, 2) 	+ cj.trailing_spaces(12, SOL_ORGP5, 2) 	+ cj.trailing_spaces(12, SOL_ORGP6, 2) 	+ cj.trailing_spaces(12, SOL_ORGP7, 2) 	+ cj.trailing_spaces(12, SOL_ORGP8, 2) 	+ cj.trailing_spaces(12, SOL_ORGP9, 2) 	+ cj.trailing_spaces(12, SOL_ORGP10, 2) + \
        "\n" + " Phosphorus perc coef     :" + cj.trailing_spaces(12, PPERCO_SUB1, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB2, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB3, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB4, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB5, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB6, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB7, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB8, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB9, 2) 	+ cj.trailing_spaces(12, PPERCO_SUB10, 2) + \
        "\n" + "Soil Pesticide Data" + \
        "\n" + " Pesticide  Pst on plant    Pst in 1st soil layer Pst enrichment" + \
        "\n" + "   #           [kg/ha]           [kg/ha]           [kg/ha]" + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME1) 	+ cj.trailing_spaces(18, PLTPST1, 2) 	+ cj.trailing_spaces(18, SOLPST1, 2) 	+ cj.trailing_spaces(18, PSTENR1, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME2) 	+ cj.trailing_spaces(18, PLTPST2, 2) 	+ cj.trailing_spaces(18, SOLPST2, 2) 	+ cj.trailing_spaces(18, PSTENR2, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME3) 	+ cj.trailing_spaces(18, PLTPST3, 2) 	+ cj.trailing_spaces(18, SOLPST3, 2) 	+ cj.trailing_spaces(18, PSTENR3, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME4) 	+ cj.trailing_spaces(18, PLTPST4, 2) 	+ cj.trailing_spaces(18, SOLPST4, 2) 	+ cj.trailing_spaces(18, PSTENR4, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME5) 	+ cj.trailing_spaces(18, PLTPST5, 2) 	+ cj.trailing_spaces(18, SOLPST5, 2) 	+ cj.trailing_spaces(18, PSTENR5, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME6) 	+ cj.trailing_spaces(18, PLTPST6, 2) 	+ cj.trailing_spaces(18, SOLPST6, 2) 	+ cj.trailing_spaces(18, PSTENR6, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME7) 	+ cj.trailing_spaces(18, PLTPST7, 2) 	+ cj.trailing_spaces(18, SOLPST7, 2) 	+ cj.trailing_spaces(18, PSTENR7, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME8) 	+ cj.trailing_spaces(18, PLTPST8, 2) 	+ cj.trailing_spaces(18, SOLPST8, 2) 	+ cj.trailing_spaces(18, PSTENR8, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME9) 	+ cj.trailing_spaces(18, PLTPST9, 2) 	+ cj.trailing_spaces(18, SOLPST9, 2) 	+ cj.trailing_spaces(18, PSTENR9, 2) + \
        "\n" + cj.string_trailing_spaces(4, PESTNAME10)	+ cj.trailing_spaces(18, PLTPST10, 2) 	+ cj.trailing_spaces(18, SOLPST10, 2) 	+ cj.trailing_spaces(18, PSTENR10, 2) + \
        "\n"

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "chm")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, chm_file)
    # print fileName
