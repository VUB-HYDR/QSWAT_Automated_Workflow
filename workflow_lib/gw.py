import init_file as variables
import cj_function_lib as cj
from datetime import datetime

gw_table = cj.extract_table_from_mdb(variables.ProjMDB, "gw", variables.path + "\\gw.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in gw_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')
    HRU_No = hru_record.split(",")[2].strip('"')
    Luse = hru_record.split(",")[3].strip('"')
    Soil = hru_record.split(",")[4].strip('"')
    Slope = hru_record.split(",")[5].strip('"')

    # Parameters
    SHALLST = hru_record.split(",")[6].strip('"')
    DEEPST = hru_record.split(",")[7].strip('"')
    GW_DELAY = hru_record.split(",")[8].strip('"')
    ALPHA_BF = hru_record.split(",")[9].strip('"')
    GWQMN = hru_record.split(",")[10].strip('"')
    GW_REVAP = hru_record.split(",")[11].strip('"')
    REVAPMN = hru_record.split(",")[12].strip('"')
    RCHRG_DP = hru_record.split(",")[13].strip('"')
    GWHT = hru_record.split(",")[14].strip('"')
    GW_SPYLD = hru_record.split(",")[15].strip('"')
    SHALLST_N = hru_record.split(",")[16].strip('"')
    GWSOLP = hru_record.split(",")[17].strip('"')
    HLIFE_NGW = hru_record.split(",")[18].strip('"')
    LAT_ORGN = hru_record.split(",")[19].strip('"')
    LAT_ORGP = hru_record.split(",")[20].strip('"')
    ALPHA_BF_D = hru_record.split(",")[21].strip('"')

    # Building String
    gw_file = " .gw file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + \
        DateAndTime + " " + SWAT_Vers + "\n       " + '{0:.4f}'.format(float(SHALLST)) + "    | SHALLST : Initial depth of water in the shallow aquifer [mm]" + "\n" + \
        "       " + '{0:.4f}'.format(float(DEEPST)) + "    | DEEPST : Initial depth of water in the deep aquifer [mm]" + "\n" + "         " + \
        '{0:.4f}'.format(float(GW_DELAY)) + "    | GW_DELAY : Groundwater delay [days]" + "\n" + "          " + '{0:.4f}'.format(float(ALPHA_BF)) + "    | ALPHA_BF : Baseflow alpha factor [days]" + \
        "\n"+ cj.trailing_spaces(int(16), GWQMN, int(4)) + "    | GWQMN : Threshold depth of water in the shallow aquifer required for return flow to occur [mm]" + \
        "\n"+ cj.trailing_spaces(int(16), GW_REVAP, int(4)) + "    | GW_REVAP : Groundwater" + ' "revap" '+ "coefficient" + \
        "\n"+ cj.trailing_spaces(int(16), REVAPMN, int(4)) + "    | REVAPMN: Threshold depth of water in the shallow aquifer for " + '"revap"' +" to occur [mm]" + \
        "\n"+ cj.trailing_spaces(int(16), RCHRG_DP, int(4)) + "    | RCHRG_DP : Deep aquifer percolation fraction" + \
        "\n"+ cj.trailing_spaces(int(16), GWHT, int(4)) + "    | GWHT : Initial groundwater height [m]" + \
        "\n"+ cj.trailing_spaces(int(16), GW_SPYLD, int(4)) + "    | GW_SPYLD : Specific yield of the shallow aquifer [m3/m3]" + \
        "\n"+ cj.trailing_spaces(int(16), SHALLST_N, int(4)) + "    | SHALLST_N : Initial concentration of nitrate in shallow aquifer [mg N/l]" + \
        "\n"+ cj.trailing_spaces(int(16), GWSOLP, int(4)) + "    | GWSOLP : Concentration of soluble phosphorus in groundwater contribution to streamflow from subbasin [mg P/l]" + \
        "\n"+ cj.trailing_spaces(int(16), HLIFE_NGW, int(4)) + "    | HLIFE_NGW : Half-life of nitrate in the shallow aquifer [days]" + \
        "\n"+ cj.trailing_spaces(int(16), LAT_ORGN, int(4)) + "    | LAT_ORGN : Organic N in the base flow [mg/L]" + \
        "\n"+ cj.trailing_spaces(int(16), LAT_ORGP, int(4)) + "    | LAT_ORGP : Organic P in the base flow [mg/L]" + \
        "\n"+ cj.trailing_spaces(int(16), ALPHA_BF_D, int(4)) + "    | ALPHA_BF_D : Baseflow alpha factor for deep aquifer [days]" + "\n"

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "gw")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, gw_file)
    #print fileName

