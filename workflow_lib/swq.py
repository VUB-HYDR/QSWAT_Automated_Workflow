import init_file as variables
import cj_function_lib as cj
from datetime import datetime

swq_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "swq", variables.path + "\\swq.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in swq_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')

    # Parameters
    RS1         = hru_record.split(",")[2].strip('"')
    RS2         = hru_record.split(",")[3].strip('"')
    RS3         = hru_record.split(",")[4].strip('"')
    RS4         = hru_record.split(",")[5].strip('"')
    RS5         = hru_record.split(",")[6].strip('"')
    RS6         = hru_record.split(",")[7].strip('"')
    RS7         = hru_record.split(",")[8].strip('"')
    RK1         = hru_record.split(",")[9].strip('"')
    RK2         = hru_record.split(",")[10].strip('"')
    RK3         = hru_record.split(",")[11].strip('"')
    RK4         = hru_record.split(",")[12].strip('"')
    RK5         = hru_record.split(",")[13].strip('"')
    RK6         = hru_record.split(",")[14].strip('"')
    BC1         = hru_record.split(",")[15].strip('"')
    BC2         = hru_record.split(",")[16].strip('"')
    BC3         = hru_record.split(",")[17].strip('"')
    BC4         = hru_record.split(",")[18].strip('"')
    CHPST_REA   = hru_record.split(",")[19].strip('"')
    CHPST_VOL   = hru_record.split(",")[20].strip('"')
    CHPST_KOC   = hru_record.split(",")[21].strip('"')
    CHPST_STL   = hru_record.split(",")[22].strip('"')
    CHPST_RSP   = hru_record.split(",")[23].strip('"')
    CHPST_MIX   = hru_record.split(",")[24].strip('"')
    SEDPST_CONC = hru_record.split(",")[25].strip('"')
    SEDPST_REA  = hru_record.split(",")[26].strip('"')
    SEDPST_BRY  = hru_record.split(",")[27].strip('"')
    SEDPST_ACT  = hru_record.split(",")[28].strip('"')

    # Building String
    swq_file = " .Swq file Subbasin: " + SubBasin + " " + DateAndTime + " " + SWAT_Vers + \
        "\nNutrient (QUAL2E parameters)" + \
        "\n           " + '{0:.3f}'.format(float(RS1)) + "    | RS1:   Local algal settling rate in the reach at 20 degC [m/day]" + \
        "\n           " + '{0:.3f}'.format(float(RS2)) + "    | RS2:   Benthic (sediment) source rate for dissolved phosphorus in the reach at 20 degC [mg dissolved P/[m2.day]]" + \
        "\n           " + '{0:.3f}'.format(float(RS3)) + "    | RS3:   Benthic source rate for NH4-N in the reach at 20 degC [mg NH4-N/[m2.day]]" + \
        "\n           " + '{0:.3f}'.format(float(RS4)) + "    | RS4:   Rate coefficient for organic N settling in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RS5)) + "    | RS5: Organic phosphorus settling rate in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RS6)) + "    | RS6: Rate coefficient for settling of arbitrary non-conservative constituent in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RS7)) + "    | RS7:   Benthic source rate for arbitrary non-conservative constituent in the reach at 20 degC [mg ANC/[m2.day]]" + \
        "\n           " + '{0:.3f}'.format(float(RK1)) + "    | RK1:   Carbonaceous biological oxygen demand deoxygenation rate coefficient in the reach at 20 degC [day-1]" + \
        "\n          " + '{0:.3f}'.format(float(RK2)) + "    | RK2:   Oxygen reaeration rate in accordance with Fickian diffusion in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RK3)) + "    | RK3:   Rate of loss of carbonaceous biological oxygen demand due to settling in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RK4)) + "    | RK4:   Benthic oxygen demand rate in the reach at 20 degC [mg O2/[m2.day]]" + \
        "\n           " + '{0:.3f}'.format(float(RK5)) + "    | RK5:   Coliform die-off rate in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(RK6)) + "    | RK6:   Decay rate for arbitrary non-conservative constituent in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(BC1)) + "    | BC1:   Rate constant for biological oxidation of NH4 to NO2 in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(BC2)) + "    | BC2:   Rate constant for biological oxidation of NO2 to NO3 in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(BC3)) + "    | BC3:   Rate constant for hydrolysis of organic N to NH4 in the reach at 20 degC [day-1]" + \
        "\n           " + '{0:.3f}'.format(float(BC4)) + "    | BC4:   Rate constant for mineralization of organic P to dissolved P in the reach at 20 degC [day-1]" + \
        "\nPesticide Parameters:" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_REA)) + "    | CHPST_REA: Pesticide reaction coefficient in reach [day-1]" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_VOL)) + "    | CHPST_VOL: Pesticide volatilization coefficient in reach [m/day]" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_KOC)) + "    | CHPST_KOC: Pesticide partition coefficient between water and air in reach [m3/day]" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_STL)) + "    | CHPST_STL: Settling velocity for pesticide sorbed to sediment [m/day]" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_RSP)) + "    | CHPST_RSP: Resuspension velocity for pesticide sorbed to sediment [m/day]" + \
        "\n      " + '{0:.8f}'.format(float(CHPST_MIX)) + "    | CHPST_MIX: Mixing velocity (diffusion/dispersion) for pesticide in reach [m/day]" + \
        "\n      " + '{0:.8f}'.format(float(SEDPST_CONC)) + "    | SEDPST_CONC: Initial pesticide concentration in reach bed sediment [mg/m3 sediment]" + \
        "\n      " + '{0:.8f}'.format(float(SEDPST_REA)) + "    | SEDPST_REA: Pesticide reaction coefficient in reach bed sediment [day-1]" + \
        "\n      " + '{0:.8f}'.format(float(SEDPST_BRY)) + "    | SEDPST_BRY: Pesticide burial velocity in reach bed sediment [m/day]" + \
        "\n      " + '{0:.8f}'.format(float(SEDPST_ACT)) + "    | SEDPST_ACT: Depth of active sediment layer for pesticide [m]\n"

    fileName = cj.get_filename(int(SubBasin), int(int(0)), "swq")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, swq_file)
    #print fileName

