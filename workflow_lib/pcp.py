"""
This Module creates pcp file
"""
import cj_function_lib as cj
import mdbtools as mdb
import init_file as variables
from datetime import datetime
import calendar

class station:
    def __init__(self, pcp_line):
        self.name = pcp_line.split(",")[1]
        self.elev = pcp_line.split(",")[4]
        self.lon = pcp_line.split(",")[3]
        self.lat = pcp_line.split(",")[2]
        self.data_list = self.get_data()

    def get_data(self):
        self.data = cj.read_from(variables.WeatherDIR + self.name + ".txt")
        return  self.data


stations_dict = {}
stations_list = []
station_nr = []

used_stations = cj.extract_table_from_mdb(variables.ProjMDB, "SubPcp", variables.path + "\\subpcp.tmp~")
all_stations = cj.extract_table_from_mdb(variables.ProjMDB, "pcp", variables.path + "\\pcp.tmp~")

count = 0
for station_line in used_stations:
    if not station_line.split(",")[4] in stations_list:
        for pcp_file_line in all_stations:
            if station_line.split(",")[4] == pcp_file_line.split(",")[1]:
                count += 1
                stations_list.append(station_line.split(",")[4])
                station_nr.append(count)
                stations_dict[str(count)] = station(pcp_file_line)

# making header

pcp_string = "Station  "


for key in range(1,len(stations_list) + 1):
    pcp_string += stations_dict[str(key)].name + ","

pcp_string += "\nLati   "

for key in range(1,len(stations_list) + 1):
    pcp_string += cj.trailing_spaces(5, stations_dict[str(key)].lat, 1)

pcp_string += "\nLong   "

for key in range(1,len(stations_list) + 1):
    pcp_string += cj.trailing_spaces(5, stations_dict[str(key)].lon, 1)

pcp_string += "\nElev   "

for key in range(1,len(stations_list) + 1):
    pcp_string += cj.trailing_spaces(5, stations_dict[str(key)].elev, 0)

pcp_string += "\n"

current_year = int(stations_dict["1"].data_list[0][0:4])
end_day = cj.get_days_in_year(current_year)
IDAF = end_day
current_day = 0
start_year = current_year

for i in range(1, len(stations_dict["1"].data_list)):
    line = ""
    current_day += 1

    if current_day <= end_day:
        datecode = str(current_year) + cj.trailing_zeros(3, current_day, 0)
        #print datecode
    else:
        current_day = 1
        current_year += 1
        end_day = cj.get_days_in_year(current_year)
        datecode = str(current_year) + cj.trailing_zeros(3, current_day, 0)
        #print end_day

    for sta_nr in station_nr:
        rec = cj.trailing_zeros(5, stations_dict[str(sta_nr)].data_list[i], 1)
        line += rec

    line = datecode + line + "\n"
    pcp_string += line

end_year = current_year
IDAL = end_day

cj.write_to(variables.path +"\\cio_config.tmp~", str(start_year) + "\n" + str(end_year) + "\n" + str((end_year - start_year) + 1) + \
    "\n" + str(IDAF) + "\n" + str(IDAL) + "\n\n" + str(len(stations_list)))

cj.write_to(variables.DefaultSimDir + "TxtInOut\\pcp1.pcp", pcp_string)
