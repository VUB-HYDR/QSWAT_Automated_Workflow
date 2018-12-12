import init_file as variables
import cj_function_lib as cj
from datetime import datetime

sub_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "sub", variables.path + "\\sub.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for sub_record in sub_table:
    # Parameters
    SUBBASIN = sub_record.split(",")[1].strip("\n")
    SUB_KM = sub_record.split(",")[2].strip("\n")
    SUB_LAT = sub_record.split(",")[3].strip("\n")
    SUB_ELEV = sub_record.split(",")[4].strip("\n")
    IRGAGE = sub_record.split(",")[5].strip("\n")
    ITGAGE = sub_record.split(",")[6].strip("\n")
    ISGAGE = sub_record.split(",")[7].strip("\n")
    IHGAGE = sub_record.split(",")[8].strip("\n")
    IWGAGE = sub_record.split(",")[9].strip("\n")
    ELEVB1 = sub_record.split(",")[10].strip("\n")
    ELEVB2 = sub_record.split(",")[11].strip("\n")
    ELEVB3 = sub_record.split(",")[12].strip("\n")
    ELEVB4 = sub_record.split(",")[13].strip("\n")
    ELEVB5 = sub_record.split(",")[14].strip("\n")
    ELEVB6 = sub_record.split(",")[15].strip("\n")
    ELEVB7 = sub_record.split(",")[16].strip("\n")
    ELEVB8 = sub_record.split(",")[17].strip("\n")
    ELEVB9 = sub_record.split(",")[18].strip("\n")
    ELEVB10 = sub_record.split(",")[19].strip("\n")
    ELEVB_FR1 = sub_record.split(",")[20].strip("\n")
    ELEVB_FR2 = sub_record.split(",")[21].strip("\n")
    ELEVB_FR3 = sub_record.split(",")[22].strip("\n")
    ELEVB_FR4 = sub_record.split(",")[23].strip("\n")
    ELEVB_FR5 = sub_record.split(",")[24].strip("\n")
    ELEVB_FR6 = sub_record.split(",")[25].strip("\n")
    ELEVB_FR7 = sub_record.split(",")[26].strip("\n")
    ELEVB_FR8 = sub_record.split(",")[27].strip("\n")
    ELEVB_FR9 = sub_record.split(",")[28].strip("\n")
    ELEVB_FR10 = sub_record.split(",")[29].strip("\n")
    SNOEB1 = sub_record.split(",")[30].strip("\n")
    SNOEB2 = sub_record.split(",")[31].strip("\n")
    SNOEB3 = sub_record.split(",")[32].strip("\n")
    SNOEB4 = sub_record.split(",")[33].strip("\n")
    SNOEB5 = sub_record.split(",")[34].strip("\n")
    SNOEB6 = sub_record.split(",")[35].strip("\n")
    SNOEB7 = sub_record.split(",")[36].strip("\n")
    SNOEB8 = sub_record.split(",")[37].strip("\n")
    SNOEB9 = sub_record.split(",")[38].strip("\n")
    SNOEB10 = sub_record.split(",")[39].strip("\n")
    PLAPS = sub_record.split(",")[40].strip("\n")
    TLAPS = sub_record.split(",")[41].strip("\n")
    SNO_SUB = sub_record.split(",")[42].strip("\n")
    CH_L1 = sub_record.split(",")[43].strip("\n")
    CH_S1 = sub_record.split(",")[44].strip("\n")
    CH_W1 = sub_record.split(",")[45].strip("\n")
    CH_K1 = sub_record.split(",")[46].strip("\n")
    CH_N1 = sub_record.split(",")[47].strip("\n")
    CO2 = sub_record.split(",")[48].strip("\n")
    RFINC1 = sub_record.split(",")[49].strip("\n")
    RFINC2 = sub_record.split(",")[50].strip("\n")
    RFINC3 = sub_record.split(",")[51].strip("\n")
    RFINC4 = sub_record.split(",")[52].strip("\n")
    RFINC5 = sub_record.split(",")[53].strip("\n")
    RFINC6 = sub_record.split(",")[54].strip("\n")
    RFINC7 = sub_record.split(",")[55].strip("\n")
    RFINC8 = sub_record.split(",")[56].strip("\n")
    RFINC9 = sub_record.split(",")[57].strip("\n")
    RFINC10 = sub_record.split(",")[58].strip("\n")
    RFINC11 = sub_record.split(",")[59].strip("\n")
    RFINC12 = sub_record.split(",")[60].strip("\n")
    TMPINC1 = sub_record.split(",")[61].strip("\n")
    TMPINC2 = sub_record.split(",")[62].strip("\n")
    TMPINC3 = sub_record.split(",")[63].strip("\n")
    TMPINC4 = sub_record.split(",")[64].strip("\n")
    TMPINC5 = sub_record.split(",")[65].strip("\n")
    TMPINC6 = sub_record.split(",")[66].strip("\n")
    TMPINC7 = sub_record.split(",")[67].strip("\n")
    TMPINC8 = sub_record.split(",")[68].strip("\n")
    TMPINC9 = sub_record.split(",")[69].strip("\n")
    TMPINC10 = sub_record.split(",")[70].strip("\n")
    TMPINC11 = sub_record.split(",")[71].strip("\n")
    TMPINC12 = sub_record.split(",")[72].strip("\n")
    RADINC1 = sub_record.split(",")[73].strip("\n")
    RADINC2 = sub_record.split(",")[74].strip("\n")
    RADINC3 = sub_record.split(",")[75].strip("\n")
    RADINC4 = sub_record.split(",")[76].strip("\n")
    RADINC5 = sub_record.split(",")[77].strip("\n")
    RADINC6 = sub_record.split(",")[78].strip("\n")
    RADINC7 = sub_record.split(",")[79].strip("\n")
    RADINC8 = sub_record.split(",")[80].strip("\n")
    RADINC9 = sub_record.split(",")[81].strip("\n")
    RADINC10 = sub_record.split(",")[82].strip("\n")
    RADINC11 = sub_record.split(",")[83].strip("\n")
    RADINC12 = sub_record.split(",")[84].strip("\n")
    HUMINC1 = sub_record.split(",")[85].strip("\n")
    HUMINC2 = sub_record.split(",")[86].strip("\n")
    HUMINC3 = sub_record.split(",")[87].strip("\n")
    HUMINC4 = sub_record.split(",")[88].strip("\n")
    HUMINC5 = sub_record.split(",")[89].strip("\n")
    HUMINC6 = sub_record.split(",")[90].strip("\n")
    HUMINC7 = sub_record.split(",")[91].strip("\n")
    HUMINC8 = sub_record.split(",")[92].strip("\n")
    HUMINC9 = sub_record.split(",")[93].strip("\n")
    HUMINC10 = sub_record.split(",")[94].strip("\n")
    HUMINC11 = sub_record.split(",")[95].strip("\n")
    HUMINC12 = sub_record.split(",")[96].strip("\n")
    HRUTOT = sub_record.split(",")[97].strip("\n")
    IPOT = sub_record.split(",")[98].strip("\n")
    FCST_REG = sub_record.split(",")[99].strip("\n")
    SUBSNOW = sub_record.split(",")[100].strip("\n")


    if ISGAGE == "":
        ISGAGE = 0
    if IHGAGE == "":
        IHGAGE = 0
    if IWGAGE == "":
        IWGAGE = 0

    hru_files_in_sub = ""
    for i in range (1, int(HRUTOT) + 1):
        HRU_ID = cj.trailing_zeros(5, SUBBASIN, 0) + cj.trailing_zeros(4, i, 0)
        hru_files_in_sub += "\n" + HRU_ID + ".hru" + HRU_ID + ".mgt" + HRU_ID + ".sol" + HRU_ID + ".chm " + HRU_ID + ".gw             " + HRU_ID + ".sep"
    
    # Building String
    sub_file = " .sub file Subbasin: " + SUBBASIN + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + cj.trailing_spaces(16, SUB_KM, 6) + "    | SUB_KM : Subbasin area [km2]" + \
        "\n" + \
        "\n" + "Climate in subbasin" + \
        "\n" + cj.trailing_spaces(16, SUB_LAT, 6)  + "    | LATITUDE : Latitude of subbasin [degrees]" + \
        "\n" + cj.trailing_spaces(16, SUB_ELEV, 2)  + "    | ELEV : Elevation of subbasin [m]" + \
        "\n" + cj.trailing_spaces(16, IRGAGE, 0)  + "    | IRGAGE: precip gage data used in subbasin" + \
        "\n" + cj.trailing_spaces(16, ITGAGE, 0) + "    | ITGAGE: temp gage data used in subbasin" + \
        "\n" + cj.trailing_spaces(16, ISGAGE, 0) + "    | ISGAGE: solar radiation gage data used in subbasin" + \
        "\n" + cj.trailing_spaces(16, IHGAGE, 0) + "    | IHGAGE: relative humidity gage data used in subbasin" + \
        "\n" + cj.trailing_spaces(16, IWGAGE, 0) + "    | IWGAGE: wind speed gage data used in subbasin" + \
        "\n" + cj.get_filename(int(SUBBASIN), int(0), "wgn") + "       | WGNFILE: name of weather generator data file" + \
        "\n" + cj.trailing_spaces(16, FCST_REG, 0) + "    | FCST_REG: Region number used to assign forecast data to the subbasin" + \
        "\n" + "Elevation Bands" + \
        "\n" + "| ELEVB: Elevation at center of elevation bands [m]" + \
        "\n" +  cj.trailing_spaces(8, ELEVB1, 3) + cj.trailing_spaces(8, ELEVB2, 3) + cj.trailing_spaces(8, ELEVB3, 3) + cj.trailing_spaces(8, ELEVB4, 3) + cj.trailing_spaces(8, ELEVB5, 3) + cj.trailing_spaces(8, ELEVB6, 3) + cj.trailing_spaces(8, ELEVB7, 3) + cj.trailing_spaces(8, ELEVB8, 3) + cj.trailing_spaces(8, ELEVB9, 3) + cj.trailing_spaces(8, ELEVB10, 3) + \
        "\n" + "| ELEVB_FR: Fraction of subbasin area within elevation band" + \
        "\n" + cj.trailing_spaces(8, ELEVB_FR1, 3) + cj.trailing_spaces(8, ELEVB_FR2, 3) + cj.trailing_spaces(8, ELEVB_FR3, 3) + cj.trailing_spaces(8, ELEVB_FR4, 3) + cj.trailing_spaces(8, ELEVB_FR5, 3) + cj.trailing_spaces(8, ELEVB_FR6, 3) + cj.trailing_spaces(8, ELEVB_FR7, 3) + cj.trailing_spaces(8, ELEVB_FR8, 3) + cj.trailing_spaces(8, ELEVB_FR9, 3) + cj.trailing_spaces(8, ELEVB_FR10, 3) + \
        "\n" + "| SNOEB: Initial snow water content in elevation band [mm]" + \
        "\n" + cj.trailing_spaces(8, SNOEB1, 1) + cj.trailing_spaces(8, SNOEB2, 1) + cj.trailing_spaces(8, SNOEB3, 1) + cj.trailing_spaces(8, SNOEB4, 1) + cj.trailing_spaces(8, SNOEB5, 1) + cj.trailing_spaces(8, SNOEB6, 1) + cj.trailing_spaces(8, SNOEB7, 1) + cj.trailing_spaces(8, SNOEB8, 1) + cj.trailing_spaces(8, SNOEB9, 1) + cj.trailing_spaces(8, SNOEB10, 1) + \
        "\n" + cj.trailing_spaces(16, PLAPS, 3) + "    | PLAPS : Precipitation lapse rate [mm/km]" + \
        "\n" + cj.trailing_spaces(16, TLAPS, 3) + "    | TLAPS : Temperature lapse rate [deg C/km]" + \
        "\n" + cj.trailing_spaces(16, SNO_SUB, 3) + "    | SNO_SUB : Initial snow water content [mm]" + \
        "\n" + "Tributary Channels" + \
        "\n" + cj.trailing_spaces(16, CH_L1, 3) + "    | CH_L1 : Longest tributary channel length [km]" + \
        "\n" + cj.trailing_spaces(16, CH_S1, 3) + "    | CH_S1 : Average slope of tributary channel [m/m]" + \
        "\n" + cj.trailing_spaces(16, CH_W1, 3) + "    | CH_W1 : Average width of tributary channel [m]" + \
        "\n" + cj.trailing_spaces(16, CH_K1, 3) + "    | CH_K1 : Effective hydraulic conductivity in tributary channel [mm/hr]" + \
        "\n" + cj.trailing_spaces(16, CH_N1, 3) + "    | CH_N1 : Manning's 'n' value for the tributary channels" + \
        "\n" + "Impoundments" + \
        "\n" + cj.get_filename(int(SUBBASIN), int(0), "pnd") + "       | PNDFILE: name of subbasin impoundment file" + \
        "\n" + "Consumptive Water Use" + \
        "\n" + cj.get_filename(int(SUBBASIN), int(0), "wus") + "       | WUSFILE: name of subbasin water use file" + \
        "\n" + "Climate Change" + \
        "\n" + cj.trailing_spaces(16, CO2, 3) + "    | CO2 : Carbon dioxide concentration [ppmv]" + \
        "\n" + "| RFINC:  Climate change monthly rainfall adjustment (January - June)" + \
        "\n" + cj.trailing_spaces(8, RFINC1, 3) +	cj.trailing_spaces(8, RFINC2, 3) +	cj.trailing_spaces(8, RFINC3, 3) +	cj.trailing_spaces(8, RFINC4, 3) +	cj.trailing_spaces(8, RFINC5, 3) +	cj.trailing_spaces(8, RFINC6, 3) + \
        "\n" + "| RFINC:  Climate change monthly rainfall adjustment (July - December)" + \
        "\n" + cj.trailing_spaces(8, RFINC7, 3) +	cj.trailing_spaces(8, RFINC8, 3) +	cj.trailing_spaces(8, RFINC9, 3) +	cj.trailing_spaces(8, RFINC10, 3) +	cj.trailing_spaces(8, RFINC11, 3) +	cj.trailing_spaces(8, RFINC12, 3) + \
        "\n" + "| TMPINC: Climate change monthly temperature adjustment (January - June)" + \
        "\n" + cj.trailing_spaces(8, TMPINC1, 3) +	cj.trailing_spaces(8, TMPINC2, 3) +	cj.trailing_spaces(8, TMPINC3, 3) +	cj.trailing_spaces(8, TMPINC4, 3) +	cj.trailing_spaces(8, TMPINC5, 3) +	cj.trailing_spaces(8, TMPINC6, 3) + \
        "\n" + "| TMPINC: Climate change monthly temperature adjustment (July - December)" + \
        "\n" + cj.trailing_spaces(8, TMPINC7, 3) +	cj.trailing_spaces(8, TMPINC8, 3) +	cj.trailing_spaces(8, TMPINC9, 3) +	cj.trailing_spaces(8, TMPINC10, 3) +	cj.trailing_spaces(8, TMPINC11, 3) +	cj.trailing_spaces(8, TMPINC12, 3) + \
        "\n" + "| RADINC: Climate change monthly radiation adjustment (January - June)" + \
        "\n" + cj.trailing_spaces(8, RADINC1, 3) +	cj.trailing_spaces(8, RADINC2, 3) +	cj.trailing_spaces(8, RADINC3, 3) +	cj.trailing_spaces(8, RADINC4, 3) +	cj.trailing_spaces(8, RADINC5, 3) +	cj.trailing_spaces(8, RADINC6, 3) + \
        "\n" + "| RADINC: Climate change monthly radiation adjustment (July - December)" + \
        "\n" + cj.trailing_spaces(8, RADINC7, 3) +	cj.trailing_spaces(8, RADINC8, 3) +	cj.trailing_spaces(8, RADINC9, 3) +	cj.trailing_spaces(8, RADINC10, 3) +	cj.trailing_spaces(8, RADINC11, 3) +	cj.trailing_spaces(8, RADINC12, 3) + \
        "\n" + "| HUMINC: Climate change monthly humidity adjustment (January - June)" + \
        "\n" + cj.trailing_spaces(8, HUMINC1, 3) +	cj.trailing_spaces(8, HUMINC2, 3) +	cj.trailing_spaces(8, HUMINC3, 3) +	cj.trailing_spaces(8, HUMINC4, 3) +	cj.trailing_spaces(8, HUMINC5, 3) +	cj.trailing_spaces(8, HUMINC6, 3) + \
        "\n" + "| HUMINC: Climate change monthly humidity adjustment (July - December)" + \
        "\n" + cj.trailing_spaces(8, HUMINC7, 3) +	cj.trailing_spaces(8, HUMINC8, 3) +	cj.trailing_spaces(8, HUMINC9, 3) +	cj.trailing_spaces(8, HUMINC10, 3) +	cj.trailing_spaces(8, HUMINC11, 3) +	cj.trailing_spaces(8, HUMINC12, 3) + \
        "\n" + "| HRU data" + \
        "\n" + cj.trailing_spaces(16, HRUTOT, 0) + "    | HRUTOT : Total number of HRUs modeled in subbasin" + \
        "\n" + \
        "\n" + "HRU: Depressional Storage/Pothole" + \
        "\n" + \
        "\n" + "Floodplain" + \
        "\n" + \
        "\n" + "HRU: Riparian" + \
        "\n" + \
        "\n" + "HRU: General" + hru_files_in_sub + \
        "\n"

    fileName = cj.get_filename(int(SUBBASIN), int(0), "sub")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, sub_file)
    #print fileName
