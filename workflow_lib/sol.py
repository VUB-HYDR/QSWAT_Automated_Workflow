import init_file as variables
import cj_function_lib as cj
from datetime import datetime

Sol_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "Sol", variables.path + "\\Sol.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in Sol_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')
    HRU_No = hru_record.split(",")[2].strip('"')
    Luse = hru_record.split(",")[3].strip('"')
    Soil = hru_record.split(",")[4].strip('"')
    Slope = hru_record.split(",")[5].strip('"')

    # Parameters
    SNAM        = hru_record.split(",")[6].strip('"')
    NLAYERS     = hru_record.split(",")[7].strip('"')
    HYDGRP      = hru_record.split(",")[8].strip('"')
    SOL_ZMX     = hru_record.split(",")[9].strip('"')
    ANION_EXCL  = hru_record.split(",")[10].strip('"')
    SOL_CRK     = hru_record.split(",")[11].strip('"')
    TEXTURE     = hru_record.split(",")[12].strip('"')
    SOL_Z1      = hru_record.split(",")[13].strip('"')
    SOL_BD1     = hru_record.split(",")[14].strip('"')
    SOL_AWC1    = hru_record.split(",")[15].strip('"')
    SOL_K1      = hru_record.split(",")[16].strip('"')
    SOL_CBN1    = hru_record.split(",")[17].strip('"')
    CLAY1       = hru_record.split(",")[18].strip('"')
    SILT1       = hru_record.split(",")[19].strip('"')
    SAND1       = hru_record.split(",")[20].strip('"')
    ROCK1       = hru_record.split(",")[21].strip('"')
    SOL_ALB1    = hru_record.split(",")[22].strip('"')
    USLE_K1     = hru_record.split(",")[23].strip('"')
    SOL_EC1     = hru_record.split(",")[24].strip('"')
    SOL_Z2      = hru_record.split(",")[25].strip('"')
    SOL_BD2     = hru_record.split(",")[26].strip('"')
    SOL_AWC2    = hru_record.split(",")[27].strip('"')
    SOL_K2      = hru_record.split(",")[28].strip('"')
    SOL_CBN2    = hru_record.split(",")[29].strip('"')
    CLAY2       = hru_record.split(",")[30].strip('"')
    SILT2       = hru_record.split(",")[31].strip('"')
    SAND2       = hru_record.split(",")[32].strip('"')
    ROCK2       = hru_record.split(",")[33].strip('"')
    SOL_ALB2    = hru_record.split(",")[34].strip('"')
    USLE_K2     = hru_record.split(",")[35].strip('"')
    SOL_EC2     = hru_record.split(",")[36].strip('"')
    SOL_Z3      = hru_record.split(",")[37].strip('"')
    SOL_BD3     = hru_record.split(",")[38].strip('"')
    SOL_AWC3    = hru_record.split(",")[39].strip('"')
    SOL_K3      = hru_record.split(",")[40].strip('"')
    SOL_CBN3    = hru_record.split(",")[41].strip('"')
    CLAY3       = hru_record.split(",")[42].strip('"')
    SILT3       = hru_record.split(",")[43].strip('"')
    SAND3       = hru_record.split(",")[44].strip('"')
    ROCK3       = hru_record.split(",")[45].strip('"')
    SOL_ALB3    = hru_record.split(",")[46].strip('"')
    USLE_K3     = hru_record.split(",")[47].strip('"')
    SOL_EC3     = hru_record.split(",")[48].strip('"')
    SOL_Z4      = hru_record.split(",")[49].strip('"')
    SOL_BD4	    =	hru_record.split(",")[50].strip('"')
    SOL_AWC4	=	hru_record.split(",")[51].strip('"')
    SOL_K4	=	hru_record.split(",")[52].strip('"')
    SOL_CBN4	=	hru_record.split(",")[53].strip('"')
    CLAY4	=	hru_record.split(",")[54].strip('"')
    SILT4	=	hru_record.split(",")[55].strip('"')
    SAND4	=	hru_record.split(",")[56].strip('"')
    ROCK4	=	hru_record.split(",")[57].strip('"')
    SOL_ALB4	=	hru_record.split(",")[58].strip('"')
    USLE_K4	=	hru_record.split(",")[59].strip('"')
    SOL_EC4	=	hru_record.split(",")[60].strip('"')
    SOL_Z5	=	hru_record.split(",")[61].strip('"')
    SOL_BD5	=	hru_record.split(",")[62].strip('"')
    SOL_AWC5	=	hru_record.split(",")[63].strip('"')
    SOL_K5	=	hru_record.split(",")[64].strip('"')
    SOL_CBN5	=	hru_record.split(",")[65].strip('"')
    CLAY5	=	hru_record.split(",")[66].strip('"')
    SILT5	=	hru_record.split(",")[67].strip('"')
    SAND5	=	hru_record.split(",")[68].strip('"')
    ROCK5	=	hru_record.split(",")[69].strip('"')
    SOL_ALB5	=	hru_record.split(",")[70].strip('"')
    USLE_K5	=	hru_record.split(",")[71].strip('"')
    SOL_EC5	=	hru_record.split(",")[72].strip('"')
    SOL_Z6	=	hru_record.split(",")[73].strip('"')
    SOL_BD6	=	hru_record.split(",")[74].strip('"')
    SOL_AWC6	=	hru_record.split(",")[75].strip('"')
    SOL_K6	=	hru_record.split(",")[76].strip('"')
    SOL_CBN6	=	hru_record.split(",")[77].strip('"')
    CLAY6	=	hru_record.split(",")[78].strip('"')
    SILT6	=	hru_record.split(",")[79].strip('"')
    SAND6	=	hru_record.split(",")[80].strip('"')
    ROCK6	=	hru_record.split(",")[81].strip('"')
    SOL_ALB6	=	hru_record.split(",")[82].strip('"')
    USLE_K6	=	hru_record.split(",")[83].strip('"')
    SOL_EC6	=	hru_record.split(",")[84].strip('"')
    SOL_Z7	=	hru_record.split(",")[85].strip('"')
    SOL_BD7	=	hru_record.split(",")[86].strip('"')
    SOL_AWC7	=	hru_record.split(",")[87].strip('"')
    SOL_K7	=	hru_record.split(",")[88].strip('"')
    SOL_CBN7	=	hru_record.split(",")[89].strip('"')
    CLAY7	=	hru_record.split(",")[90].strip('"')
    SILT7	=	hru_record.split(",")[91].strip('"')
    SAND7	=	hru_record.split(",")[92].strip('"')
    ROCK7	=	hru_record.split(",")[93].strip('"')
    SOL_ALB7	=	hru_record.split(",")[94].strip('"')
    USLE_K7	=	hru_record.split(",")[95].strip('"')
    SOL_EC7	=	hru_record.split(",")[96].strip('"')
    SOL_Z8	=	hru_record.split(",")[97].strip('"')
    SOL_BD8	=	hru_record.split(",")[98].strip('"')
    SOL_AWC8	=	hru_record.split(",")[99].strip('"')
    SOL_K8	=	hru_record.split(",")[100].strip('"')
    SOL_CBN8	=	hru_record.split(",")[101].strip('"')
    CLAY8	=	hru_record.split(",")[102].strip('"')
    SILT8	=	hru_record.split(",")[103].strip('"')
    SAND8	=	hru_record.split(",")[104].strip('"')
    ROCK8	=	hru_record.split(",")[105].strip('"')
    SOL_ALB8	=	hru_record.split(",")[106].strip('"')
    USLE_K8	=	hru_record.split(",")[107].strip('"')
    SOL_EC8	=	hru_record.split(",")[108].strip('"')
    SOL_Z9	=	hru_record.split(",")[109].strip('"')
    SOL_BD9	=	hru_record.split(",")[110].strip('"')
    SOL_AWC9	=	hru_record.split(",")[111].strip('"')
    SOL_K9	=	hru_record.split(",")[112].strip('"')
    SOL_CBN9	=	hru_record.split(",")[113].strip('"')
    CLAY9	=	hru_record.split(",")[114].strip('"')
    SILT9	=	hru_record.split(",")[115].strip('"')
    SAND9	=	hru_record.split(",")[116].strip('"')
    ROCK9	=	hru_record.split(",")[117].strip('"')
    SOL_ALB9	=	hru_record.split(",")[118].strip('"')
    USLE_K9	=	hru_record.split(",")[119].strip('"')
    SOL_EC9	=	hru_record.split(",")[120].strip('"')
    SOL_Z10	=	hru_record.split(",")[121].strip('"')
    SOL_BD10	=	hru_record.split(",")[122].strip('"')
    SOL_AWC10	=	hru_record.split(",")[123].strip('"')
    SOL_K10	=	hru_record.split(",")[124].strip('"')
    SOL_CBN10	=	hru_record.split(",")[125].strip('"')
    CLAY10	=	hru_record.split(",")[126].strip('"')
    SILT10	=	hru_record.split(",")[127].strip('"')
    SAND10	=	hru_record.split(",")[128].strip('"')
    ROCK10	=	hru_record.split(",")[129].strip('"')
    SOL_ALB10	= hru_record.split(",")[130].strip('"')
    USLE_K10	= hru_record.split(",")[131].strip('"')
    SOL_EC10	= hru_record.split(",")[132].strip('"')
    SOL_CAL1	= hru_record.split(",")[133].strip('"')
    SOL_CAL2	= hru_record.split(",")[134].strip('"')
    SOL_CAL3	= hru_record.split(",")[135].strip('"')
    SOL_CAL4	= hru_record.split(",")[136].strip('"')
    SOL_CAL5	= hru_record.split(",")[137].strip('"')
    SOL_CAL6	= hru_record.split(",")[138].strip('"')
    SOL_CAL7	= hru_record.split(",")[139].strip('"')
    SOL_CAL8	= hru_record.split(",")[140].strip('"')
    SOL_CAL9	= hru_record.split(",")[141].strip('"')
    SOL_CAL10	= hru_record.split(",")[142].strip('"')
    SOL_PH1	=	hru_record.split(",")[143].strip('"')
    SOL_PH2	=	hru_record.split(",")[144].strip('"')
    SOL_PH3	=	hru_record.split(",")[145].strip('"')
    SOL_PH4	=	hru_record.split(",")[146].strip('"')
    SOL_PH5	=	hru_record.split(",")[147].strip('"')
    SOL_PH6	=	hru_record.split(",")[148].strip('"')
    SOL_PH7	=	hru_record.split(",")[149].strip('"')
    SOL_PH8	=	hru_record.split(",")[150].strip('"')
    SOL_PH9	=	hru_record.split(",")[151].strip('"')
    SOL_PH10	=	hru_record.split(",")[152].strip('"')

    # Building String
    Sol_file = " .Sol file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + \
        DateAndTime + " " + SWAT_Vers + \
        "\n Soil Name: " + SNAM + \
        "\n Soil Hydrologic Group: " + HYDGRP  + \
        "\n Maximum rooting depth(mm) :" + cj.trailing_spaces(8, int(float(SOL_ZMX)), 2) + \
        "\n Porosity fraction from which anions are excluded: " + '{0:.3f}'.format(float(ANION_EXCL)) + \
        "\n Crack volume potential of soil: " + '{0:.3f}'.format(float(SOL_CRK)) + \
        "\n Texture 1                : " + TEXTURE + \
        "\n Depth                [mm]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_Z1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_Z2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_Z3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_Z4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_Z5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_Z6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_Z7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_Z8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_Z9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_Z10, 2)) + 	\
        "\n Bulk Density Moist [g/cc]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_BD1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_BD2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_BD3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_BD4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_BD5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_BD6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_BD7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_BD8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_BD9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_BD10, 2)) + 	\
        "\n Ave. AW Incl. Rock Frag  :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_AWC1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_AWC2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_AWC3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_AWC4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_AWC5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_AWC6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_AWC7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_AWC8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_AWC9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_AWC10, 2)) + 	\
        "\n Ksat. (est.)      [mm/hr]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K1 == "0.0" else SOL_K1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K2 == "0.0" else SOL_K2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K3 == "0.0" else SOL_K3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K4 == "0.0" else SOL_K4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K5 == "0.0" else SOL_K5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K6 == "0.0" else SOL_K6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K7 == "0.0" else SOL_K7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K8 == "0.0" else SOL_K8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K9 == "0.0" else SOL_K9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, 0.01 if SOL_K10 == "0.0" else SOL_K10, 2)) + \
        "\n Organic Carbon [weight %]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_CBN1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_CBN2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_CBN3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_CBN4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_CBN5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_CBN6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_CBN7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_CBN8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_CBN9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_CBN10, 2)) + 	\
        "\n Clay           [weight %]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, CLAY1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, CLAY2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, CLAY3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, CLAY4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, CLAY5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, CLAY6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, CLAY7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, CLAY8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, CLAY9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, CLAY10, 2)) + 	\
        "\n Silt           [weight %]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SILT1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SILT2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SILT3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SILT4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SILT5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SILT6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SILT7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SILT8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SILT9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SILT10, 2)) + 	\
        "\n Sand           [weight %]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SAND1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SAND2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SAND3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SAND4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SAND5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SAND6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SAND7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SAND8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SAND9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SAND10, 2)) + 	\
        "\n Rock Fragments   [vol. %]:" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, ROCK1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, ROCK2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, ROCK3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, ROCK4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, ROCK5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, ROCK6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, ROCK7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, ROCK8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, ROCK9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, ROCK10, 2)) + 	\
        "\n Soil Albedo (Moist)      :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_ALB1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_ALB2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_ALB3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_ALB4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_ALB5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_ALB6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_ALB7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_ALB8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_ALB9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_ALB10, 2)) + 	\
        "\n Erosion K                :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, USLE_K1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, USLE_K2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, USLE_K3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, USLE_K4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, USLE_K5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, USLE_K6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, USLE_K7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, USLE_K8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, USLE_K9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, USLE_K10, 2)) + 	\
        "\n Salinity (EC, Form 5)    :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_EC1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_EC2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_EC3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_EC4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_EC5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_EC6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_EC7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_EC8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_EC9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_EC10, 2)) + 	\
        "\n Soil pH                  :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_PH1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_PH2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_PH3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_PH4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_PH5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_PH6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_PH7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_PH8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_PH9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_PH10, 2)) + 	\
        "\n Soil CACO3               :" + ("" if int(float(SOL_Z1)) == int(0) else cj.trailing_spaces(12, SOL_CAL1, 2)) + 	("" if int(float(SOL_Z2)) == int(0) else cj.trailing_spaces(12, SOL_CAL2, 2)) + 	("" if int(float(SOL_Z3)) == int(0) else cj.trailing_spaces(12, SOL_CAL3, 2)) + 	("" if int(float(SOL_Z4)) == int(0) else cj.trailing_spaces(12, SOL_CAL4, 2)) + 	("" if int(float(SOL_Z5)) == int(0) else cj.trailing_spaces(12, SOL_CAL5, 2)) + 	("" if int(float(SOL_Z6)) == int(0) else cj.trailing_spaces(12, SOL_CAL6, 2)) + 	("" if int(float(SOL_Z7)) == int(0) else cj.trailing_spaces(12, SOL_CAL7, 2)) + 	("" if int(float(SOL_Z8)) == int(0) else cj.trailing_spaces(12, SOL_CAL8, 2)) + 	("" if int(float(SOL_Z9)) == int(0) else cj.trailing_spaces(12, SOL_CAL9, 2)) + 	("" if int(float(SOL_Z10)) == int(0) else cj.trailing_spaces(12, SOL_CAL10, 2)) + 	\
        "\n                              \n"

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "sol")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, Sol_file)
    #print fileName

