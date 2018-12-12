import init_file as variables
import cj_function_lib as cj
from datetime import datetime

wus_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "wus", variables.path + "\\wus.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

for sub_record in wus_table:
    # Hru ID
    SubBasin = sub_record.split(",")[1].strip('"')

    # Parameters
    WUPND1 = cj.trailing_spaces(10, sub_record.split(",")[2].strip('"'), 1)
    WUPND2 = cj.trailing_spaces(10, sub_record.split(",")[3].strip('"'), 1)
    WUPND3 = cj.trailing_spaces(10, sub_record.split(",")[4].strip('"'), 1)
    WUPND4 = cj.trailing_spaces(10, sub_record.split(",")[5].strip('"'), 1)
    WUPND5 = cj.trailing_spaces(10, sub_record.split(",")[6].strip('"'), 1)
    WUPND6 = cj.trailing_spaces(10, sub_record.split(",")[7].strip('"'), 1)
    WUPND7 = cj.trailing_spaces(10, sub_record.split(",")[8].strip('"'), 1)
    WUPND8 = cj.trailing_spaces(10, sub_record.split(",")[9].strip('"'), 1)
    WUPND9 = cj.trailing_spaces(10, sub_record.split(",")[10].strip('"'), 1)
    WUPND10 = cj.trailing_spaces(10, sub_record.split(",")[11].strip('"'), 1)
    WUPND11 = cj.trailing_spaces(10, sub_record.split(",")[12].strip('"'), 1)
    WUPND12 = cj.trailing_spaces(10, sub_record.split(",")[13].strip('"'), 1)
    WURCH1 = cj.trailing_spaces(10, sub_record.split(",")[14].strip('"'), 1)
    WURCH2 = cj.trailing_spaces(10, sub_record.split(",")[15].strip('"'), 1)
    WURCH3 = cj.trailing_spaces(10, sub_record.split(",")[16].strip('"'), 1)
    WURCH4 = cj.trailing_spaces(10, sub_record.split(",")[17].strip('"'), 1)
    WURCH5 = cj.trailing_spaces(10, sub_record.split(",")[18].strip('"'), 1)
    WURCH6 = cj.trailing_spaces(10, sub_record.split(",")[19].strip('"'), 1)
    WURCH7 = cj.trailing_spaces(10, sub_record.split(",")[20].strip('"'), 1)
    WURCH8 = cj.trailing_spaces(10, sub_record.split(",")[21].strip('"'), 1)
    WURCH9 = cj.trailing_spaces(10, sub_record.split(",")[22].strip('"'), 1)
    WURCH10 = cj.trailing_spaces(10, sub_record.split(",")[23].strip('"'), 1)
    WURCH11 = cj.trailing_spaces(10, sub_record.split(",")[24].strip('"'), 1)
    WURCH12 = cj.trailing_spaces(10, sub_record.split(",")[25].strip('"'), 1)
    WUSHAL1 = cj.trailing_spaces(10, sub_record.split(",")[26].strip('"'), 1)
    WUSHAL2 = cj.trailing_spaces(10, sub_record.split(",")[27].strip('"'), 1)
    WUSHAL3 = cj.trailing_spaces(10, sub_record.split(",")[28].strip('"'), 1)
    WUSHAL4 = cj.trailing_spaces(10, sub_record.split(",")[29].strip('"'), 1)
    WUSHAL5 = cj.trailing_spaces(10, sub_record.split(",")[30].strip('"'), 1)
    WUSHAL6 = cj.trailing_spaces(10, sub_record.split(",")[31].strip('"'), 1)
    WUSHAL7 = cj.trailing_spaces(10, sub_record.split(",")[32].strip('"'), 1)
    WUSHAL8 = cj.trailing_spaces(10, sub_record.split(",")[33].strip('"'), 1)
    WUSHAL9 = cj.trailing_spaces(10, sub_record.split(",")[34].strip('"'), 1)
    WUSHAL10 = cj.trailing_spaces(10, sub_record.split(",")[35].strip('"'), 1)
    WUSHAL11 = cj.trailing_spaces(10, sub_record.split(",")[36].strip('"'), 1)
    WUSHAL12 = cj.trailing_spaces(10, sub_record.split(",")[37].strip('"'), 1)
    WUDEEP1 = cj.trailing_spaces(10, sub_record.split(",")[38].strip('"'), 1)
    WUDEEP2 = cj.trailing_spaces(10, sub_record.split(",")[39].strip('"'), 1)
    WUDEEP3 = cj.trailing_spaces(10, sub_record.split(",")[40].strip('"'), 1)
    WUDEEP4 = cj.trailing_spaces(10, sub_record.split(",")[41].strip('"'), 1)
    WUDEEP5 = cj.trailing_spaces(10, sub_record.split(",")[42].strip('"'), 1)
    WUDEEP6 = cj.trailing_spaces(10, sub_record.split(",")[43].strip('"'), 1)
    WUDEEP7 = cj.trailing_spaces(10, sub_record.split(",")[44].strip('"'), 1)
    WUDEEP8 = cj.trailing_spaces(10, sub_record.split(",")[45].strip('"'), 1)
    WUDEEP9 = cj.trailing_spaces(10, sub_record.split(",")[46].strip('"'), 1)
    WUDEEP10 = cj.trailing_spaces(10, sub_record.split(",")[47].strip('"'), 1)
    WUDEEP11 = cj.trailing_spaces(10, sub_record.split(",")[48].strip('"'), 1)
    WUDEEP12 = cj.trailing_spaces(10, sub_record.split(",")[49].strip('"'), 1)

    # Building String
    wus_file = " .wus file Subbasin: " + SubBasin + " " + DateAndTime + " " + SWAT_Vers + \
        "\n" + \
        "\n" + \
        "\n" + WUPND1 + WUPND2 + WUPND3 + WUPND4 + WUPND5 + WUPND6 + \
        "\n" + WUPND7 + WUPND8 + WUPND9 + WUPND10 + WUPND11 + WUPND12 + \
        "\n" + WURCH1 + WURCH2 + WURCH3 + WURCH4 + WURCH5 + WURCH6 + \
        "\n" + WURCH7 + WURCH8 + WURCH9 + WURCH10 + WURCH11 + WURCH12 + \
        "\n" + WUSHAL1 + WUSHAL2 + WUSHAL3 + WUSHAL4 + WUSHAL5 + WUSHAL6 + \
        "\n" + WUSHAL7 + WUSHAL8 + WUSHAL9 + WUSHAL10 + WUSHAL11 + WUSHAL12 + \
        "\n" + WUDEEP1 + WUDEEP2 + WUDEEP3 + WUDEEP4 + WUDEEP5 + WUDEEP6 + \
        "\n" + WUDEEP7 + WUDEEP8 + WUDEEP9 + WUDEEP10 + WUDEEP11 + WUDEEP12 + \
        "\n"

    fileName = cj.get_filename(int(SubBasin), int(0), "wus")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, wus_file)
    # print fileName
