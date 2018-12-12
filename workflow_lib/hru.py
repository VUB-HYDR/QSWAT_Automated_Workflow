import init_file as variables
import cj_function_lib as cj
from datetime import datetime

hru_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "hru", variables.path + "\\hru.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in hru_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')
    HRU_No = hru_record.split(",")[2].strip('"')
    Luse = hru_record.split(",")[3].strip('"')
    Soil = hru_record.split(",")[4].strip('"')
    Slope = hru_record.split(",")[5].strip('"')

    # Parameters
    HRU_FR = hru_record.split(",")[6].strip('"')
    HRU_SLP = hru_record.split(",")[8].strip('"')
    SLSUBBSN = cj.get_slsbbsn(HRU_SLP)
    OV_N = hru_record.split(",")[9].strip('"')
    LAT_TTIME = hru_record.split(",")[10].strip('"')
    LAT_SED = hru_record.split(",")[11].strip('"')
    SLSOIL = hru_record.split(",")[12].strip('"')
    CANMX = hru_record.split(",")[13].strip('"')
    ESCO = hru_record.split(",")[14].strip('"')
    EPCO = hru_record.split(",")[15].strip('"')
    RSDIN = hru_record.split(",")[16].strip('"')
    ERORGN = hru_record.split(",")[17].strip('"')
    ERORGP = hru_record.split(",")[18].strip('"')
    POT_FR = hru_record.split(",")[19].strip('"')
    FLD_FR = hru_record.split(",")[20].strip('"')
    RIP_FR = hru_record.split(",")[21].strip('"')

    POT_TILE = hru_record.split(",")[22].strip('"')
    POT_VOLX = hru_record.split(",")[23].strip('"')
    POT_VOL = hru_record.split(",")[24].strip('"')
    POT_NSED = hru_record.split(",")[25].strip('"')
    POT_NO3L = hru_record.split(",")[26].strip('"')
    DEP_IMP = hru_record.split(",")[27].strip('"')

    EVPOT = hru_record.split(",")[29].strip('"')
    DIS_STREAM = hru_record.split(",")[28].strip('"')
    CF = hru_record.split(",")[30].strip('"')
    CFH = hru_record.split(",")[31].strip('"')
    CFDEC = hru_record.split(",")[32].strip('"')
    SED_CON = hru_record.split(",")[33].strip('"')
    ORGN_CON = hru_record.split(",")[34].strip('"')
    ORGP_CON = hru_record.split(",")[35].strip('"')
    SOLN_CON = hru_record.split(",")[36].strip('"')
    SOLP_CON = hru_record.split(",")[37].strip('"')

    RE = hru_record.split(",")[38].strip('"')
    SDRAIN = hru_record.split(",")[39].strip('"')
    DRAIN_CO = hru_record.split(",")[40].strip('"')
    PC = hru_record.split(",")[41].strip('"')
    LATKSATF = hru_record.split(",")[42].strip('"')

    POT_SOLP = hru_record.split(",")[43].strip('"')
    POT_K = hru_record.split(",")[44].strip('"')
    N_REDUC = hru_record.split(",")[45].strip('"')
    N_LAG = hru_record.split(",")[46].strip('"')
    N_LN = hru_record.split(",")[47].strip('"')
    N_LNCO = hru_record.split(",")[48].strip('"')
    SURLAG = hru_record.split(",")[49].strip('"')
    R2ADJ = hru_record.split(",")[50].strip('"')

    # Building String
    hru_file = " .hru file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + cj.trailing_spaces(int(16), HRU_FR, int(7)) + "    | HRU_FR : Fraction of subbasin area contained in HRU" + \
        "\n" + cj.trailing_spaces(int(16), SLSUBBSN, 3) + "    | SLSUBBSN : Average slope length [m]" + \
        "\n" + cj.trailing_spaces(int(16), HRU_SLP, 3) + "    | HRU_SLP : Average slope stepness [m/m]" + \
        "\n" + cj.trailing_spaces(int(16), OV_N, 3) + "    | OV_N : Manning's " + '"n"' + " value for overland flow" + \
        "\n" + cj.trailing_spaces(int(16), LAT_TTIME, 3) + "    | LAT_TTIME : Lateral flow travel time [days]" + \
        "\n" + cj.trailing_spaces(int(16), LAT_SED, 3) + "    | LAT_SED : Sediment concentration in lateral flow and groundwater flow [mg/l]" + \
        "\n" + cj.trailing_spaces(int(16), SLSOIL, 3) + "    | SLSOIL : Slope length for lateral subsurface flow [m]" + \
        "\n" + cj.trailing_spaces(int(16), CANMX, 3) + "    | CANMX : Maximum canopy storage [mm]" + \
        "\n" + cj.trailing_spaces(int(16), ESCO, 3) + "    | ESCO : Soil evaporation compensation factor" + \
        "\n" + cj.trailing_spaces(int(16), EPCO, 3) + "    | EPCO : Plant uptake compensation factor" + \
        "\n" + cj.trailing_spaces(int(16), RSDIN, 3) + "    | RSDIN : Initial residue cover [kg/ha]" + \
        "\n" + cj.trailing_spaces(int(16), ERORGN, 3) + "    | ERORGN : Organic N enrichment ratio" + \
        "\n" + cj.trailing_spaces(int(16), ERORGP, 3) + "    | ERORGP : Organic P enrichment ratio" + \
        "\n" + cj.trailing_spaces(int(16), POT_FR, 3) + "    | POT_FR : Fraction of HRU are that drains into pothole" + \
        "\n" + cj.trailing_spaces(int(16), FLD_FR, 3) + "    | FLD_FR : Fraction of HRU that drains into floodplain" + \
        "\n" + cj.trailing_spaces(int(16), RIP_FR, 3) + "    | RIP_FR : Fraction of HRU that drains into riparian zone" + \
        "\nSpecial HRU: Pothole" + \
        "\n" + cj.trailing_spaces(int(16), POT_TILE, 3) + "    | POT_TILE : Average daily outflow to main channel from tile flow (depth [mm] over entire HRU)" + \
        "\n" + cj.trailing_spaces(int(16), POT_VOLX, 3) + "    | POT_VOLX : Maximum volume of water stored in the pothole (depth [mm] over entire HRU)" + \
        "\n" + cj.trailing_spaces(int(16), POT_VOL, 3) + "    | POT_VOL : Initial volume of water stored in the pothole (depth [mm] over entire HRU)" + \
        "\n" + cj.trailing_spaces(int(16), POT_NSED, 3) + "    | POT_NSED : Normal sediment concentration in pothole [mg/l]" + \
        "\n" + cj.trailing_spaces(int(16), POT_NO3L, 3) + "    | POT_NO3L : Nitrate decay rate in pothole [1/day]" + \
        "\n" + cj.trailing_spaces(int(16), DEP_IMP, 0) + "    | DEP_IMP : Depth to impervious layer in soil profile [mm]" + \
        "\n" + \
        "\n" + \
        "\n" + \
        "\n" + cj.trailing_spaces(int(16), EVPOT, 1) + "    | EVPOT: Pothole evaporation coefficient" + \
        "\n" + cj.trailing_spaces(int(16), DIS_STREAM, 1) + "    | DIS_STREAM: Average distance to stream [m]" + \
        "\n" + cj.trailing_spaces(int(16), CF, 1) + "    | CF: Decomposition response to soil temperature and moisture" + \
        "\n" + cj.trailing_spaces(int(16), CFH, 1) + "    | CFH: Maximum humification rate" + \
        "\n" + cj.trailing_spaces(int(16), CFDEC, 3) + "    | CFDEC: Undistrurbed soil turnover rate under optimum soil water and temperature" + \
        "\n" + cj.trailing_spaces(int(16), SED_CON, 1) + "    | SED_CON: Sediment concentration in runoff, after urban BMP is applied" + \
        "\n" + cj.trailing_spaces(int(16), ORGN_CON, 1) + "    | ORGN_CON: Organic nitrogen concentration in runoff, after urban BMP is applied" + \
        "\n" + cj.trailing_spaces(int(16), ORGP_CON, 1) + "    | ORGP_CON: Organic phosphorus concentration in runoff, after urban BMP is applied" + \
        "\n" + cj.trailing_spaces(int(16), SOLN_CON, 1) + "    | SOLN_CON: Soluble nitrogen concentration un runoff, after urban BMP is applied" + \
        "\n" + cj.trailing_spaces(int(16), SOLP_CON, 1) + "    | SOLP_CON: Soluble phosphorus concentration in runoff, after urban BMP is applied" + \
        "\n" + cj.trailing_spaces(int(16), POT_SOLP, 1) + "    | POT_SOLP: Soluble P loss rate in the pothole" + \
        "\n" + cj.trailing_spaces(int(16), POT_K, 1) + "    | POT_K: Hydraulic conductivity of soil surface of  pothole" + \
        "\n" + cj.trailing_spaces(int(16), N_REDUC, 1) + "    | N_REDUC: Nitrogen uptake reduction factor not currently used" + \
        "\n" + cj.trailing_spaces(int(16), N_LAG, 1) + "    | N_LAG: Lag coefficient for calculating nitrate concentration in subsurface drains" + \
        "\n" + cj.trailing_spaces(int(16), N_LN, 1) + "    | N_LN: Power function exponent for calculating nitrate concentration in subsurface drains" + \
        "\n" + cj.trailing_spaces(int(16), N_LNCO, 1) + "    | N_LNCO: Coefficient for power function for calculating nitrate concentration in subsurface drains" + \
        "\n" + cj.trailing_spaces(int(16), SURLAG, 1) + "    | SURLAG: Surface runoff lag time in the HRU (days)" + \
        "\n" + cj.trailing_spaces(int(16), R2ADJ, 1) + "    | R2ADJ: Curve number retention parameter adjustment factor to adjust surface runoff for flat slopes" + \
        "\n"

    sdr_file = " .sdr file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + cj.trailing_spaces(int(10), RE, 2) + "    | RE: Effective radius of drains (mm)" + \
        "\n" + cj.trailing_spaces(int(10), SDRAIN, 2) + "    | SDRAIN: Distance bwtween two drain tubes or tiles (mm)" + \
        "\n" + cj.trailing_spaces(int(10), DRAIN_CO, 2) + "    | DRAIN_CO: Drainage coefficient (mm/day)" + \
        "\n" + cj.trailing_spaces(int(10), PC, 2) + "    | PC: Pump capacity (def pump cap - 1.042mm/hr or 25mm/day)" + \
        "\n" + cj.trailing_spaces(int(10), LATKSATF, 2) + \
        "    | LATKSATF: Multiplication factor to determine conk(j1,j) from sol_k(j1,k) for HRU\n"

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "hru")
    fileName_sdr = cj.get_filename(int(SubBasin), int(HRU_No), "sdr")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, hru_file)
    cj.write_to(variables.DefaultSimDir +
                "TxtInOut\\" + fileName_sdr, sdr_file)
    # print fileName
