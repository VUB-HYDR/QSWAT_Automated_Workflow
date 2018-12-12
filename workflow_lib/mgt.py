import init_file as variables
import cj_function_lib as cj
from datetime import datetime
import pandas as pd

mgt_table1 = cj.extract_table_from_mdb(
    variables.ProjMDB, "mgt1", variables.path + "\\mgt1.tmp~")
mgt_table2_unsorted = cj.extract_table_from_mdb(
    variables.ProjMDB, "mgt2", variables.path + "\\mgt2.tmp~")
now = datetime.now()

mgt_table_lol = []
for u in mgt_table2_unsorted:
    mgt_table_lol.append(u.split(","))

df = pd.DataFrame.from_records(mgt_table_lol)
df[0] = df[0].astype(int)
df2 = df.sort_values([0], ascending=True)
mgt_table2 = df2.values.tolist()



DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for hru_record in mgt_table1:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')
    HRU_No = hru_record.split(",")[2].strip('"')
    Luse = hru_record.split(",")[3].strip('"')
    Soil = hru_record.split(",")[4].strip('"')
    Slope = hru_record.split(",")[5].strip('"')

    # Parameters
    IGRO = hru_record.split(",")[6].strip('"')
    #PLANT_ID = hru_record.split(",")[7].strip('"')
    PLANT_ID = 0    
    LAI_INIT = hru_record.split(",")[8].strip('"')
    BIO_INIT = hru_record.split(",")[9].strip('"')
    PHU_PLT = hru_record.split(",")[10].strip('"')

    BIOMIX = hru_record.split(",")[11].strip('"')
    CN2 = hru_record.split(",")[12].strip('"')
    USLE_P = hru_record.split(",")[13].strip('"')
    BIO_MIN = hru_record.split(",")[14].strip('"')
    FILTERW = hru_record.split(",")[15].strip('"')

    IURBAN = hru_record.split(",")[16].strip('"')
    URBLU = hru_record.split(",")[17].strip('"')

    IRRSC = hru_record.split(",")[18].strip('"')
    IRRNO = hru_record.split(",")[19].strip('"')
    FLOWMIN = hru_record.split(",")[20].strip('"')
    DIVMAX = hru_record.split(",")[21].strip('"')
    FLOWFR = hru_record.split(",")[22].strip('"')

    DDRAIN = hru_record.split(",")[23].strip('"')
    TDRAIN = hru_record.split(",")[24].strip('"')
    GDRAIN = hru_record.split(",")[25].strip('"')

    NROT = hru_record.split(",")[26].strip('"')

    # Building String
    op_schedule = ""   # Here we make the operation schedule based on the land use properties from mgt2 table in the database
    for record in mgt_table2:
        if (int(SubBasin) == int(record[1].strip('"'))) and (int(HRU_No) == int(record[2].strip('"'))):
            if int(record[11].strip('"')) == int(1):   # if it is planting, add the line for planting from database table
                op_schedule += cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    cj.trailing_spaces(5, record[13].strip('"'), 0) + cj.trailing_spaces(20, record[12].strip('"'), 5) + cj.trailing_spaces(7, record[15].strip('"'), 2) + \
                    cj.trailing_spaces(12, record[16].strip('"'), 5) + cj.trailing_spaces(5, record[17].strip('"'), 2) + \
                    cj.trailing_spaces(7, record[18].strip('"'), 2) + cj.trailing_spaces(6, record[19].strip('"'), 2)
            
            if int(record[11].strip('"')) == int(2):   # 
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    cj.trailing_spaces(9, record[63].strip('"'), 0) + cj.trailing_spaces(16, record[20].strip('"'), 5) + \
                    cj.trailing_spaces(7, record[51].strip('"'), 2) + cj.trailing_spaces(12, record[52].strip('"'), 5) + \
                    cj.trailing_spaces(5, record[53].strip('"'), 2) + cj.trailing_spaces(25, record[64].strip('"'), 0)
            
            if int(record[11].strip('"')) == int(3):   # 
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    cj.trailing_spaces(5, record[21].strip('"'), 0) + cj.trailing_spaces(20, record[22].strip('"'), 5) + \
                    cj.trailing_spaces(7, record[23].strip('"'), 2)

            if int(record[11].strip('"')) == int(4):   # 
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    "" + \
                    cj.trailing_spaces(5, record[24].strip('"'), 0) + cj.trailing_spaces(20, record[25].strip('"'), 5) + \
                    cj.trailing_spaces(7, record[49].strip('"'), 2)

            if int(record[11].strip('"')) == int(5):   # if it is strip croppng, add the line for strip cropping from database table
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    "" + \
                    cj.trailing_spaces(25, record[19].strip('"'), 5)

            if int(record[11].strip('"')) == int(6):   
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    cj.trailing_spaces(5, record[26].strip('"'), 0) + cj.trailing_spaces(20, record[19].strip('"'), 5)

            if int(record[11].strip('"')) == int(7):   # if it is strip croppng, add the line for strip cropping from database table
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    "" + \
                    cj.trailing_spaces(9, record[50].strip('"'), 0) + cj.trailing_spaces(16, record[27].strip('"'), 5) + cj.trailing_spaces(7, record[28].strip('"'), 2)

            if int(record[11].strip('"')) == int(8):   # if it is strip croppng, add the line for strip cropping from database table
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    ""
            if int(record[11].strip('"')) == int(9):   # if it is strip croppng, add the line for strip cropping from database table
                op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                    "" + \
                    cj.trailing_spaces(5, record[29].strip('"'), 0) + cj.trailing_spaces(4, record[30].strip('"'), 0) + cj.trailing_spaces(16, record[31].strip('"'), 5) + \
                    cj.trailing_spaces(7, record[32].strip('"'), 2) + cj.trailing_spaces(12, record[33].strip('"'), 5)

            if int(record[11].strip('"')) == int(10):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(5, record[34].strip('"'), 0) + cj.trailing_spaces(4, record[64].strip('"'), 0) + cj.trailing_spaces(16, record[35].strip('"'), 5) + \
                        cj.trailing_spaces(7, record[54].strip('"'), 2) + cj.trailing_spaces(12, record[55].strip('"'), 5) + cj.trailing_spaces(5, record[56].strip('"'), 2) + \
                        cj.trailing_spaces(25, record[66].strip('"'), 0) 

            if int(record[11].strip('"')) == int(11):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(5, record[36].strip('"'), 0) + cj.trailing_spaces(20, record[37].strip('"'), 5) + cj.trailing_spaces(7, record[38].strip('"'), 2) + \
                        cj.trailing_spaces(12, record[39].strip('"'), 5) + cj.trailing_spaces(5, record[40].strip('"'), 2) + \
                        cj.trailing_spaces(7, record[41].strip('"'), 2)

            if int(record[11].strip('"')) == int(12):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(25, record[42].strip('"'), 5) + cj.trailing_spaces(7, record[43].strip('"'), 2)

            if int(record[11].strip('"')) == int(13):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(5, record[44].strip('"'), 0)

            if int(record[11].strip('"')) == int(14):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(5, record[45].strip('"'), 0) + cj.trailing_spaces(4, record[46].strip('"'), 0) + cj.trailing_spaces(3, record[47].strip('"'), 0) + \
                        cj.trailing_spaces(13, record[48].strip('"'), 4)

            if int(record[11].strip('"')) == int(15):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(5, record[57].strip('"'), 0) + cj.trailing_spaces(4, record[58].strip('"'), 0) + cj.trailing_spaces(3, record[59].strip('"'), 0) + \
                        cj.trailing_spaces(13, record[60].strip('"'), 4)

            if int(record[11].strip('"')) == int(16):   # if it is strip croppng, add the line for strip cropping from database table
                    op_schedule += "\n" + cj.trailing_spaces(15, record[10].strip('"'), 3) + cj.trailing_spaces(3, record[11].strip('"'), 0) + \
                        "" + \
                        cj.trailing_spaces(25, record[61].strip('"'), 5)


    op_schedule += '\n' + cj.trailing_spaces(18, '17', 0)


    mgt_file = " .mgt file Watershed HRU:" + WshedHRU + " Subbasin:" + SubBasin + " HRU:" + HRU_No + " Luse:" + Luse + " Soil: " + Soil + " Slope: " + Slope + " " + DateAndTime + " " + SWAT_Vers + \
        "\n               0    | NMGT:Management code" + \
        "\nInitial Plant Growth Parameters" + \
        "\n" + cj.trailing_spaces(16, IGRO, 0) + "    | IGRO: Land cover status: 0-none growing; 1-growing" + \
        "\n" + cj.trailing_spaces(16, PLANT_ID, 0) + "    | PLANT_ID: Land cover ID number (IGRO = 1)" + \
        "\n" + cj.trailing_spaces(16, LAI_INIT, 2) + "    | LAI_INIT: Initial leaf are index (IGRO = 1)" + \
        "\n" + cj.trailing_spaces(16, BIO_INIT, 2) + "    | BIO_INIT: Initial biomass (kg/ha) (IGRO = 1)" + \
        "\n" + cj.trailing_spaces(16, PHU_PLT, 2) + "    | PHU_PLT: Number of heat units to bring plant to maturity (IGRO = 1)" + \
        "\nGeneral Management Parameters" + \
        "\n" + cj.trailing_spaces(16, BIOMIX, 2) + "    | BIOMIX: Biological mixing efficiency" +  \
        "\n" + cj.trailing_spaces(16, CN2, 2) + "    | CN2: Initial SCS CN II value" + \
        "\n" + cj.trailing_spaces(16, USLE_P, 2) + "    | USLE_P: USLE support practice factor" + \
        "\n" + cj.trailing_spaces(16, BIO_MIN, 2) + "    | BIO_MIN: Minimum biomass for grazing (kg/ha)" + \
        "\n" + cj.trailing_spaces(16, FILTERW, 3) + "    | FILTERW: width of edge of field filter strip (m)" + \
        "\nUrban Management Parameters" +  \
        "\n" + cj.trailing_spaces(16, IURBAN, 0) + "    | IURBAN: urban simulation code, 0-none, 1-USGS, 2-buildup/washoff" + \
        "\n" + cj.trailing_spaces(16, URBLU, 0) + "    | URBLU: urban land type" + \
        "\nIrrigation Management Parameters" + \
        "\n" + cj.trailing_spaces(16, IRRSC, 0) + "    | IRRSC: irrigation code" + \
        "\n" + cj.trailing_spaces(16, IRRNO, 0) + "    | IRRNO: irrigation source location" + \
        "\n" + cj.trailing_spaces(16, FLOWMIN, 3) + "    | FLOWMIN: min in-stream flow for irr diversions (m^3/s)" + \
        "\n" + cj.trailing_spaces(16, DIVMAX, 3) + "    | DIVMAX: max irrigation diversion from reach (+mm/-10^4m^3)" + \
        "\n" + cj.trailing_spaces(16, FLOWFR, 3) + "    | FLOWFR: : fraction of flow allowed to be pulled for irr" + \
        "\nTile Drain Management Parameters" + \
        "\n" + cj.trailing_spaces(16, DDRAIN, 3) + "    | DDRAIN: depth to subsurface tile drain (mm)" + \
        "\n" + cj.trailing_spaces(16, TDRAIN, 3) + "    | TDRAIN: time to drain soil to field capacity (hr)" + \
        "\n" + cj.trailing_spaces(16, GDRAIN, 3) + "    | GDRAIN: drain tile lag time (hr)" + \
        "\nManagement Operations:" + \
        "\n" + cj.trailing_spaces(16, NROT, 0) + "    | NROT: number of years of rotation" + \
        "\nOperation Schedule:" + \
        "\n" + op_schedule

    fileName = cj.get_filename(int(SubBasin), int(HRU_No), "mgt")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, mgt_file)
    #print fileName
