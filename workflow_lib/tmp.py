"""
This Module creates tmp file
"""
import cj_function_lib as cj
import mdbtools as mdb
import init_file as variables
from datetime import datetime
import calendar

class station:
    def __init__(self, tmp_line):
        self.name = tmp_line.split(",")[1]
        self.elev = tmp_line.split(",")[4]
        self.lon = tmp_line.split(",")[3]
        self.lat = tmp_line.split(",")[2]
        self.data_list = self.get_data()

    def get_data(self):
        self.data = cj.read_from(variables.WeatherDIR + self.name + ".txt")
        return  self.data


stations_dict = {}
stations_list = []
station_nr = []

used_stations = cj.extract_table_from_mdb(variables.ProjMDB, "SubTmp", variables.path + "\\subtmp.tmp~")
all_stations = cj.extract_table_from_mdb(variables.ProjMDB, "tmp", variables.path + "\\tmp.tmp~")

count = 0
for station_line in used_stations:
    if not station_line.split(",")[4] in stations_list:
        for tmp_file_line in all_stations:
            if station_line.split(",")[4] == tmp_file_line.split(",")[1]:
                count += 1
                stations_list.append(station_line.split(",")[4])
                station_nr.append(count)
                stations_dict[str(count)] = station(tmp_file_line)

# making header

tmp_string = "Station  "

for key in range(1,len(stations_list) + 1):
    tmp_string += stations_dict[str(key)].name + ","

tmp_string += "\nLati   "

for key in range(1,len(stations_list) + 1):
    tmp_string += cj.trailing_spaces(10, stations_dict[str(key)].lat, 1)

tmp_string += "\nLong   "

for key in range(1,len(stations_list) + 1):
    tmp_string += cj.trailing_spaces(10, stations_dict[str(key)].lon, 1)

tmp_string += "\nElev   "

for key in range(1,len(stations_list) + 1):
    tmp_string += cj.trailing_spaces(10, stations_dict[str(key)].elev, 0)

tmp_string += "\n"

current_tear = int(stations_dict["1"].data_list[0][0:4])
end_day = cj.get_days_in_year(current_tear)
current_day = 0

for i in range(1, len(stations_dict["1"].data_list)):
    line = ""
    current_day += 1

    if current_day <= end_day:
        datecode = str(current_tear) + cj.trailing_zeros(3, current_day, 0)
        #print datecode
    else:
        current_day = 1
        current_tear += 1
        end_day = cj.get_days_in_year(current_tear)
        datecode = str(current_tear) + cj.trailing_zeros(3, current_day, 0)
        #print end_day

    for sta_nr in station_nr:
        rec = ("000.0" if cj.trailing_zeros(5, stations_dict[str(sta_nr)].data_list[i].split(",")[0], 1) == "-00.0" else cj.trailing_zeros(5, stations_dict[str(sta_nr)].data_list[i].split(",")[0], 1)) + ("000.0" if cj.trailing_zeros(5, stations_dict[str(sta_nr)].data_list[i].split(",")[1], 1) == "-00.0" else cj.trailing_zeros(5, stations_dict[str(sta_nr)].data_list[i].split(",")[1], 1))
        line += rec

    line = datecode + line + "\n"
    tmp_string += line

cj.write_to(variables.DefaultSimDir + "TxtInOut\\tmp1.tmp", tmp_string)
