import init_file as variables
import cj_function_lib as cj
from datetime import datetime

pnd_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "pnd", variables.path + "\\pnd.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in pnd_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')

    # Parameters
    PND_FR          = hru_record.split(",")[2].strip('"')
    PND_PSA         = hru_record.split(",")[3].strip('"')
    PND_PVOL        = hru_record.split(",")[4].strip('"')

    PND_ESA         = hru_record.split(",")[5].strip('"')
    PND_EVOL        = hru_record.split(",")[6].strip('"')
    PND_VOL         = hru_record.split(",")[7].strip('"')
    PND_SED         = hru_record.split(",")[8].strip('"')
    PND_NSED        = hru_record.split(",")[9].strip('"')
    PND_K           = hru_record.split(",")[10].strip('"')
    IFLOD1          = hru_record.split(",")[11].strip('"')
    IFLOD2          = hru_record.split(",")[12].strip('"')
    NDTARG          = hru_record.split(",")[13].strip('"')
    PSETLP1         = hru_record.split(",")[14].strip('"')
    PSETLP2         = hru_record.split(",")[15].strip('"')
    NSETLP1         = hru_record.split(",")[16].strip('"')
    NSETLP2         = hru_record.split(",")[17].strip('"')
    CHLAP           = hru_record.split(",")[18].strip('"')
    SECCIP          = hru_record.split(",")[19].strip('"')
    PND_NO3         = hru_record.split(",")[20].strip('"')
    PND_SOLP        = hru_record.split(",")[21].strip('"')
    PND_ORGN        = hru_record.split(",")[22].strip('"')
    PND_ORGP        = hru_record.split(",")[23].strip('"')
    PND_D50         = hru_record.split(",")[47].strip('"')
    IPND1           = hru_record.split(",")[24].strip('"')
    IPND2           = hru_record.split(",")[25].strip('"')

    WET_FR          = hru_record.split(",")[26].strip('"')
    WET_NSA         = hru_record.split(",")[27].strip('"')
    WET_NVOL        = hru_record.split(",")[28].strip('"')
    WET_MXSA        = hru_record.split(",")[29].strip('"')
    WET_MXVOL       = hru_record.split(",")[30].strip('"')
    WET_VOL         = hru_record.split(",")[31].strip('"')
    WET_SED         = hru_record.split(",")[32].strip('"')
    WET_NSED        = hru_record.split(",")[33].strip('"')
    WET_K           = hru_record.split(",")[34].strip('"')
    PSETLW1         = hru_record.split(",")[35].strip('"')
    PSETLW2         = hru_record.split(",")[36].strip('"')
    NSETLW1         = hru_record.split(",")[37].strip('"')
    NSETLW2         = hru_record.split(",")[38].strip('"')
    CHLAW           = hru_record.split(",")[39].strip('"')
    SECCIW          = hru_record.split(",")[40].strip('"')
    WET_NO3         = hru_record.split(",")[41].strip('"')
    WET_SOLP        = hru_record.split(",")[42].strip('"')
    WET_ORGN        = hru_record.split(",")[43].strip('"')
    WET_ORGP        = hru_record.split(",")[44].strip('"')
    PNDEVCOEFF      = hru_record.split(",")[45].strip('"')
    WETEVCOEFF      = hru_record.split(",")[46].strip('"')

    # Building String
    pnd_file = " .Pnd file Subbasin: " + SubBasin + " " + DateAndTime + " " + SWAT_Vers + \
        "\nPond inputs:" + \
        "\n           " + '{0:.3f}'.format(float(PND_FR)) + "    | PND_FR : Fraction of subbasin area that drains into ponds. The value for PND_FR should be between 0.0 and 1.0. If PND_FR = 1.0, the pond is at the outlet of the subbasin on the main channel" + \
        "\n           " + '{0:.3f}'.format(float(PND_PSA)) + "    | PND_PSA: Surface area of ponds when filled to principal spillway [ha]" + \
        "\n          " + '{0:.3f}'.format(float(PND_PVOL)) + "    | PND_PVOL: Volume of water stored in ponds when filled to the principal spillway [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(PND_ESA)) + "    | PND_ESA: Surface area of ponds when filled to emergency spillway [ha]" + \
        "\n          " + '{0:.3f}'.format(float(PND_EVOL)) + "    | PND_EVOL: Volume of water stored in ponds when filled to the emergency spillway [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(PND_VOL)) + "    | PND_VOL: Initial volume of water in ponds [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(PND_SED)) + "    | PND_SED: Initial sediment concentration in pond water [mg/l]" + \
        "\n           " + '{0:.3f}'.format(float(PND_NSED)) + "    | PND_NSED: Normal sediment concentration in pond water [mg/l]" + \
        "\n           " + '{0:.3f}'.format(float(PND_K)) + "    | PND_K: Hydraulic conductivity through bottom of ponds [mm/hr]." + \
        "\n               0    | IFLOD1: Beginning month of non-flood season" + \
        "\n               0    | IFLOD2: Ending month of non-flood season" + \
        "\n           " + '{0:.3f}'.format(float(NDTARG)) + "    | NDTARG: Number of days needed to reach target storage from current pond storage" + \
        "\n          " + '{0:.3f}'.format(float(PSETLP1)) + "    | PSETLP1: Phosphorus settling rate in pond for months IPND1 through IPND2 [m/year]" + \
        "\n          " + '{0:.3f}'.format(float(PSETLP2)) + "    | PSETLP2: Phosphorus settling rate in pond for months other than IPND1-IPND2 [m/year]" + \
        "\n           " + '{0:.3f}'.format(float(NSETLP1)) + "    | NSETLP1: Initial dissolved oxygen concentration in the reach [mg O2/l]" + \
        "\n           " + '{0:.3f}'.format(float(NSETLP2)) + "    | NSETLP2: Initial dissolved oxygen concentration in the reach [mg O2/l]" + \
        "\n           " + '{0:.3f}'.format(float(CHLAP)) + "    | CHLAP: Chlorophyll a production coefficient for ponds [ ] " + \
        "\n           " + '{0:.3f}'.format(float(SECCIP)) + "    | SECCIP: Water clarity coefficient for ponds [m]" + \
        "\n           " + '{0:.3f}'.format(float(PND_NO3)) + "    | PND_NO3: Initial concentration of NO3-N in pond [mg N/l]" + \
        "\n           " + '{0:.3f}'.format(float(PND_SOLP)) + "    | PND_SOLP: Initial concentration of soluble P in pond [mg P/L]" + \
        "\n           " + '{0:.3f}'.format(float(PND_ORGN)) + "    | PND_ORGN: Initial concentration of organic N in pond [mg N/l]" + \
        "\n           " + '{0:.3f}'.format(float(PND_ORGP)) + "    | PND_ORGP: Initial concentration of organic P in pond [mg P/l]" + \
        "\n           " + '{0:.3f}'.format(float(PND_D50)) + "    | PND_D50: Median particle diameter of sediment [um]" + \
        "\n               " + '{0:.0f}'.format(float(IPND1)) + "    | IPND1: Beginning month of mid-year nutrient settling " + '"season"' + \
        "\n               " + '{0:.0f}'.format(float(IPND2)) + "    | IPND2: Ending month of mid-year nutrient settling " + '"season"' + \
        "\nWetland inputs:" + \
        "\n           " + '{0:.3f}'.format(float(WET_FR)) + "    | WET_FR : Fraction of subbasin area that drains into wetlands" + \
        "\n           " + '{0:.3f}'.format(float(WET_NSA)) + "    | WET_NSA: Surface area of wetlands at normal water level [ha]" + \
        "\n           " + '{0:.3f}'.format(float(WET_NVOL)) + "    | WET_NVOL: Volume of water stored in wetlands when filled to normal water level [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(WET_MXSA)) + "    | WET_MXSA: Surface area of wetlands at maximum water level [ha]" + \
        "\n           " + '{0:.3f}'.format(float(WET_MXVOL)) + "    | WET_MXVOL: Volume of water stored in wetlands when filled to maximum water level [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(WET_VOL)) + "    | WET_VOL: Initial volume of water in wetlands [104 m3]" + \
        "\n           " + '{0:.3f}'.format(float(WET_SED)) + "    | WET_SED: Initial sediment concentration in wetland water [mg/l]" + \
        "\n           " + '{0:.3f}'.format(float(WET_NSED)) + "    | WET_NSED: Normal sediment concentration in wetland water [mg/l]" + \
        "\n           " + '{0:.3f}'.format(float(WET_K)) + "    | WET_K: Hydraulic conductivity of bottom of wetlands [mm/hr]" + \
        "\n           " + '{0:.3f}'.format(float(PSETLW1)) + "    | PSETLW1: Phosphorus settling rate in wetland for months IPND1 through IPND2 [m/year]" + \
        "\n           " + '{0:.3f}'.format(float(PSETLW2)) + "    | PSETLW2: Phosphorus settling rate in wetlands for months other than IPND1-IPND2 [m/year]" + \
        "\n           " + '{0:.3f}'.format(float(NSETLW1)) + "    | NSETLW1: Nitrogen settling rate in wetlands for months IPND1 through IPND2 [m/year]" + \
        "\n           " + '{0:.3f}'.format(float(NSETLW2)) + "    | NSETLW2: Nitrogen settling rate in wetlands for months other than IPND1-IPND2 [m/year]" + \
        "\n           " + '{0:.3f}'.format(float(CHLAW)) + "    | CHLAW: Chlorophyll a production coefficient for wetlands [ ]" + \
        "\n           " + '{0:.3f}'.format(float(SECCIW)) + "    | SECCIW: Water clarity coefficient for wetlands [m]" + \
        "\n           " + '{0:.3f}'.format(float(WET_NO3)) + "    | WET_NO3: Initial concentration of NO3-N in wetland [mg N/l]" + \
        "\n           " + '{0:.3f}'.format(float(WET_SOLP)) + "    | WET_SOLP: Initial concentration of soluble P in wetland [mg P/l]" + \
        "\n           " + '{0:.3f}'.format(float(WET_ORGN)) + "    | WET_ORGN: Initial concentration of organic N in wetland [mg N/l]" + \
        "\n           " + '{0:.3f}'.format(float(WET_ORGP)) + "    | WET_ORGP: Initial concentration of organic P in wetland [mg P/l]" + \
        "\n           " + '{0:.3f}'.format(float(PNDEVCOEFF)) + "    | PNDEVCOEFF: Actual pond evaporation is equal to the potential evaporation times the pond evaporation coefficient" + \
        "\n           " + '{0:.3f}'.format(float(WETEVCOEFF)) + "    | WETEVCOEFF: Actual wetland evaporation is equal to the potential evaporation times the wetland evaporation coefficient." + \
        "\nDETENTION POND FILE:\n" + \
        "\nWET POND FILE:" + \
        "\n" + \
        "\nRETENTION-IRRIGATION BASIN FILE:" + \
        "\n" + \
        "\nSEDIMENTATION-FILTRATION BASIN:" + \
        "\n\n"

    fileName = cj.get_filename(int(SubBasin), int(0), "pnd")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, pnd_file)
    #print fileName

