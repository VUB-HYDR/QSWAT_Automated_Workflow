import init_file as variables
import cj_function_lib as cj
from datetime import datetime

fert_table = cj.extract_table_from_mdb(variables.QSWAT_MDB, "fert", variables.path + "\\fert.tmp~")

fert = ""

for fert_line in fert_table:
    fert += cj.trailing_spaces(4, fert_line.split(",")[1], 0) + cj.string_trailing_spaces(9, fert_line.split(",")[2]) + cj.trailing_spaces(8, fert_line.split(",")[3], 3) + cj.trailing_spaces(8, fert_line.split(",")[4], 3) + cj.trailing_spaces(8, fert_line.split(",")[5], 3) + cj.trailing_spaces(8, fert_line.split(",")[6], 3) + cj.trailing_spaces(8, fert_line.split(",")[7], 3) + cj.trailing_spaces(4, fert_line.split(",")[8], 2) + "E+00" + cj.trailing_spaces(4, fert_line.split(",")[9], 2)+ "E+00" + cj.trailing_spaces(8, fert_line.split(",")[10], 3) + "\n"

fileName = "fert.dat"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, fert)
#print fileName

