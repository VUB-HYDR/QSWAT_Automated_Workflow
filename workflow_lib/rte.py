import init_file as variables
import cj_function_lib as cj
from datetime import datetime

rte_table = cj.extract_table_from_mdb(variables.ProjMDB, "rte", variables.path + "\\rte.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for sub_record in rte_table:

    # Hru ID
    WshedHRU = sub_record.split(",")[0].strip('"')
    SubBasin = sub_record.split(",")[1].strip('"')

    # Parameters
    CHW2            = sub_record.split(",")[2].strip('"')
    CHD             = sub_record.split(",")[3].strip('"')
    CH_S2           = sub_record.split(",")[4].strip('"')
    CH_L2           = sub_record.split(",")[5].strip('"')
    CH_N2           = sub_record.split(",")[6].strip('"')
    CH_K2           = sub_record.split(",")[7].strip('"')
    CH_COV1         = sub_record.split(",")[8].strip('"')
    CH_COV2         = sub_record.split(",")[9].strip('"')
    CH_WDR          = sub_record.split(",")[10].strip('"')
    ALPHA_BNK       = sub_record.split(",")[11].strip('"')
    ICANAL          = sub_record.split(",")[12].strip('"')
    CH_ONCO         = sub_record.split(",")[13].strip('"')
    CH_OPCO         = sub_record.split(",")[14].strip('"')
    CH_SIDE         = sub_record.split(",")[15].strip('"')
    CH_BNK_BD       = sub_record.split(",")[16].strip('"')
    CH_BED_BD       = sub_record.split(",")[17].strip('"')
    CH_BNK_KD       = sub_record.split(",")[18].strip('"')
    CH_BED_KD       = sub_record.split(",")[19].strip('"')
    CH_BNK_D50      = sub_record.split(",")[20].strip('"')
    CH_BED_D50      = sub_record.split(",")[21].strip('"')
    CH_BNK_TC       = sub_record.split(",")[22].strip('"')
    CH_BED_TC       = sub_record.split(",")[23].strip('"')

    CH_ERODMO1      = sub_record.split(",")[24].strip('"')
    CH_ERODMO2      = sub_record.split(",")[25].strip('"')
    CH_ERODMO3      = sub_record.split(",")[26].strip('"')
    CH_ERODMO4      = sub_record.split(",")[27].strip('"')
    CH_ERODMO5      = sub_record.split(",")[28].strip('"')
    CH_ERODMO6      = sub_record.split(",")[29].strip('"')
    CH_ERODMO7      = sub_record.split(",")[30].strip('"')
    CH_ERODMO8      = sub_record.split(",")[31].strip('"')
    CH_ERODMO9      = sub_record.split(",")[32].strip('"')
    CH_ERODMO10      = sub_record.split(",")[33].strip('"')
    CH_ERODMO11      = sub_record.split(",")[34].strip('"')
    CH_ERODMO12      = sub_record.split(",")[35].strip('"') 

    CH_EQN          = sub_record.split(",")[36].strip('"')

    # Building String
    rte_file = " .rte file Subbasin: " + SubBasin + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + cj.trailing_spaces(14, CHW2, 3) + "    | CHW2 : Main channel width [m]" + \
        "\n" + cj.trailing_spaces(14, CHD, 3) + "    | CHD : Main channel depth [m]" + \
        "\n" + cj.trailing_spaces(14, CH_S2, 5) + "    | CH_S2 : Main channel slope [m/m]" + \
        "\n" + cj.trailing_spaces(14, CH_L2, 3) + "    | CH_L2 : Main channel length [km]" + \
        "\n" + cj.trailing_spaces(14, CH_N2, 3) + "    | CH_N2 : Manning's nvalue for main channel" + \
        "\n" + cj.trailing_spaces(14, CH_K2, 3) + "    | CH_K2 : Effective hydraulic conductivity [mm/hr]" + \
        "\n" + cj.trailing_spaces(14, CH_COV1, 3) + "    | CH_COV1: Channel erodibility factor" + \
        "\n" + cj.trailing_spaces(14, CH_COV2, 3) + "    | CH_COV2 : Channel cover factor" + \
        "\n" + cj.trailing_spaces(14, CH_WDR, 3) + "    | CH_WDR : Channel width:depth ratio [m/m]" + \
        "\n" + cj.trailing_spaces(14, ALPHA_BNK, 3) + "    | ALPHA_BNK : Baseflow alpha factor for bank storage [days]" + \
        "\n" + cj.trailing_spaces(14, ICANAL, 2) + "    | ICANAL : Code for irrigation canal" + \
        "\n" + cj.trailing_spaces(14, CH_ONCO, 2) + "    | CH_ONCO : Organic nitrogen concentration in the channel [ppm]" + \
        "\n" + cj.trailing_spaces(14, CH_OPCO, 2) + "    | CH_OPCO : Organic phosphorus concentration in the channel [ppm]" + \
        "\n" + cj.trailing_spaces(14, CH_SIDE, 2) + "    | CH_SIDE : Change in horizontal distance per unit vertical distance" + \
        "\n" + cj.trailing_spaces(14, CH_BNK_BD, 2) + "    | CH_BNK_BD : Bulk density of channel bank sediment (g/cc)" + \
        "\n" + cj.trailing_spaces(14, CH_BED_BD, 2) + "    | CH_BED_BD : Bulk density of channel bed sediment (g/cc)" + \
        "\n" + cj.trailing_spaces(14, CH_BNK_KD, 2) + "    | CH_BNK_KD : Erodibility of channel bank sediment by jet test (cm3/N-s)" + \
        "\n" + cj.trailing_spaces(14, CH_BED_KD, 2) + "    | CH_BED_KD : Erodibility of channel bed sediment by jet test (cm3/N-s)" + \
        "\n" + cj.trailing_spaces(14, CH_BNK_D50, 2) + "    | CH_BNK_D50 : D50 Median particle size diameter of channel bank sediment (micro-m)" + \
        "\n" + cj.trailing_spaces(14, CH_BED_D50, 2) + "    | CH_BED_D50 : D50 Median particle size diameter of channel bed sediment (micro-m)" + \
        "\n" + cj.trailing_spaces(14, CH_BNK_TC, 2) + "    | CH_BNK_TC : Critical shear stress of channel bank (N/m2)" + \
        "\n" + cj.trailing_spaces(14, CH_BED_TC, 2) + "    | CH_BED_TC : Critical shear stress of channel bed (N/m2)" + \
        "\n" + cj.trailing_spaces(6, CH_ERODMO1, 2) + cj.trailing_spaces(6, CH_ERODMO2, 2) + cj.trailing_spaces(6, CH_ERODMO3, 2) + cj.trailing_spaces(6, CH_ERODMO4, 2) + cj.trailing_spaces(6, CH_ERODMO5, 2) + cj.trailing_spaces(6, CH_ERODMO6, 2) + cj.trailing_spaces(6, CH_ERODMO7, 2) + cj.trailing_spaces(6, CH_ERODMO8, 2) + cj.trailing_spaces(6, CH_ERODMO9, 2) + cj.trailing_spaces(6, CH_ERODMO10, 2) + cj.trailing_spaces(6, CH_ERODMO11, 2) + cj.trailing_spaces(6, CH_ERODMO12, 2) + \
        "\n" + cj.trailing_spaces(14, CH_EQN, 0) + "    | CH_EQN : Sediment routing methods\n"

    fileName = cj.get_filename(int(SubBasin), int(0), "rte")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, rte_file)
    #print fileName

