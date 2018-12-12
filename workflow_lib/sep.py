import init_file as variables
import cj_function_lib as cj
from datetime import datetime

sep_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "sep", variables.path + "\\sep.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in sep_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')
    HRU_No = hru_record.split(",")[2].strip('"')
    Luse = hru_record.split(",")[3].strip('"')
    Soil = hru_record.split(",")[4].strip('"')
    Slope = hru_record.split(",")[5].strip('"')

    # Parameters
    ISEP_TYP        = hru_record.split(",")[6].strip('"')
    ISEP_IYR        = hru_record.split(",")[7].strip('"')
    ISEP_OPT        = hru_record.split(",")[8].strip('"')
    SEP_CAP         = hru_record.split(",")[9].strip('"')
    BZ_AREA         = hru_record.split(",")[10].strip('"')  
    ISEP_TFAIL      = hru_record.split(",")[11].strip('"')
    BZ_Z            = hru_record.split(",")[12].strip('"')
    BZ_THK          = hru_record.split(",")[13].strip('"')
    SEP_STRM_DIST   = hru_record.split(",")[14].strip('"')
    SEP_DEN         = hru_record.split(",")[15].strip('"')
    BIO_BD          = hru_record.split(",")[16].strip('"')
    COEFF_BOD_DC    = hru_record.split(",")[17].strip('"')
    COEFF_BOD_CONV  = hru_record.split(",")[18].strip('"')
    COEFF_FC1       = hru_record.split(",")[19].strip('"')
    COEFF_FC2       = hru_record.split(",")[20].strip('"')
    COEFF_FECAL     = hru_record.split(",")[21].strip('"')
    COEFF_PLQ       = hru_record.split(",")[22].strip('"')
    COEFF_MRT       = hru_record.split(",")[23].strip('"')
    COEFF_RSP       = hru_record.split(",")[24].strip('"')       
    COEFF_SLG1      = hru_record.split(",")[25].strip('"')
    COEFF_SLG2      = hru_record.split(",")[26].strip('"')
    COEFF_NITR      = hru_record.split(",")[27].strip('"')
    COEFF_DENITR    = hru_record.split(",")[28].strip('"')
    COEFF_PDISTRB   = hru_record.split(",")[29].strip('"')
    COEFF_PSORPMAX  = hru_record.split(",")[30].strip('"')
    COEFF_SOLPSLP   = hru_record.split(",")[31].strip('"')
    COEFF_SOLPINTC  = hru_record.split(",")[32].strip('"')

    # Building String
    sep_file = " .sep file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + \
        DateAndTime + " " + SWAT_Vers + \
        "\n" + \
        "\n            " + str(int(ISEP_TYP)) + "    | ISEP_TYP : The type of septic system" + \
        "\n            " + str(int(ISEP_IYR)) + "    | ISEP_IYR :  Year the septic system began operation" + \
        "\n            " + str(int(ISEP_OPT)) + "    | ISEP_OPT :  1=active, 2=failing, 0=non-septic" + \
        "\n          " + '{0:.1f}'.format(float(SEP_CAP)) + "    | SEP_CAP : Average number of permanent residents in a house" + \
        "\n      " + '{0:.3f}'.format(float(BZ_AREA)) + "    | BZ_AREA : Surface area of drainfield (m2)" + \
        "\n           " + str(int(ISEP_TFAIL)) + "    | ISEP_TFAIL :  Time until failing system gets fixed, days" + \
        "\n      " + '{0:.3f}'.format(float(BZ_Z)) + "    | BZ_Z : Depth to the top of biozone layer (mm)" + \
        "\n       " + '{0:.3f}'.format(float(BZ_THK)) + "    | BZ_THK : Thickness of biozone layer (mm)" + \
        "\n        " + '{0:.3f}'.format(float(SEP_STRM_DIST)) + "    | SEP_STRM_DIST : Distance to the stream from the septic HRU (km)" + \
        "\n        " + '{0:.3f}'.format(float(SEP_DEN)) + "    | SEP_DEN : Number of septic systems per square kilometer" + \
        "\n     " + '{0:.3f}'.format(float(BIO_BD)) + "    | BIO_BD : Density of biomass (kg/m3)" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_BOD_DC)) + "    | COEFF_BOD_DC : BOD decay rate coefficient,m3/d " + \
        "\n        " + '{0:.3f}'.format(float(COEFF_BOD_CONV)) + "    | COEFF_BOD_CONV : Gram of bacterial growth/gram of BOD" + \
        "\n       " + '{0:.3f}'.format(float(COEFF_FC1)) + "    | COEFF_FC1 : Field capacity coefficient 1, unitless" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_FC2)) + "    | COEFF_FC2 : Field capacity coefficient 2, unitless" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_FECAL)) + "    | COEFF_FECAL : F. coli bacteria decay rate coefficient,m3/d " + \
        "\n        " + '{0:.3f}'.format(float(COEFF_PLQ)) + "    | COEFF_PLQ : Conversion factor for plaque from TDS" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_MRT)) + "    | COEFF_MRT : Mortality rate coefficient" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_RSP)) + "    | COEFF_RSP : Respiration rate coefficient" + \
        "\n      " + '{0:.5f}'.format(float(COEFF_SLG1)) + "    | COEFF_SLG1 : Sloughing coefficient 1" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_SLG2)) + "    | COEFF_SLG2 : Sloughing coefficient 2" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_NITR)) + "    | COEFF_NITR : Nitrification rate coefficient" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_DENITR)) + "    | COEFF_DENITR : Denitrification rate coefficient" + \
        "\n    " + '{0:.5f}'.format(float(COEFF_PDISTRB)) + "    | COEFF_PDISTRB : Linear P sorption distribution coefficient,L/kg" + \
        "\n      " + '{0:.3f}'.format(float(COEFF_PSORPMAX)) + "    | COEFF_PSORPMAX : Maximum P sorption capacity, mg P/kg Soil" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_SOLPSLP)) + "    | COEFF_SOLPSLP : Slope in the effluent soluble P equation" + \
        "\n        " + '{0:.3f}'.format(float(COEFF_SOLPINTC)) + "    | COEFF_SOLPINTC : Intercept in the effluent soluble P equation" + \
        "\n\n"

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "sep")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, sep_file)
    #print fileName

