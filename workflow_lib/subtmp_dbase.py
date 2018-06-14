
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB

if not os.path.isfile(variables.tmp_file_txt):
    pass
else:
    subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
    tmp_stations = cj.read_from(variables.tmp_file_txt)

    #tmp_fields = ["ID", "NAME", "LAT", "LONG", "ELEVATION"]
    tmp_values = {}

    # initialising the dictionary
    #for field in tmp_fields:
    #    tmp_values[field] = 0

    tmp = mdt.mdb_with_ops(variables.ProjMDB)
    tmp.connect()
    tmp.create_table("tmp", "[ID]", "INTEGER")
    tmp.add_field("tmp","[NAME]", "TEXT")
    tmp.add_field("tmp","[LAT]", "FLOAT")
    tmp.add_field("tmp","[LONG]", "FLOAT")
    tmp.add_field("tmp","[ELEVATION]", "FLOAT")

    tmp.clear_table("tmp") # in case the table was there and there are records already, we recalculate.


    for i in range (1,len(tmp_stations)):   # the square brackets are used to escape reserved column names
        tmp_values["[ID]"] = int(tmp_stations[i].strip("\n").split(",")[0].strip("'"))
        tmp_values["[NAME]"] = str(tmp_stations[i].strip("\n").split(",")[1].strip("'"))
        tmp_values["[LAT]"] = float(tmp_stations[i].strip("\n").split(",")[2].strip("'"))
        tmp_values["[LONG]"] = float(tmp_stations[i].strip("\n").split(",")[3].strip("'"))
        tmp_values["[ELEVATION]"] = float(tmp_stations[i].strip("\n").split(",")[4].strip("'"))

        tmp.insert_row("tmp", tmp_values, True)

    tmp_data = cj.extract_table_from_mdb(variables.ProjMDB, 'tmp', variables.path + "\\tmp_data.tmp~")

    SubTmp_defaults={}

    """
    # here we commit to table the parameters for the basin to a row in the table SubTmp
    """
    SubTmp = mdt.mdb_with_ops(variables.ProjMDB)
    SubTmp.clear_table("SubTmp")

    OID = 0
    OrderID = 0
    done_stations_list = []
    done_stations_dict = {}

    for subbasin in subbasins:    # getting field values from from watershed table
        OID += 1

        SubTmp_defaults["ObjectID"] = subbasin.split(",")[0]
        SubTmp_defaults["Subbasin"] = subbasin.split(",")[3]

        current_lat = float(subbasin.split(",")[11])
        current_lon = float(subbasin.split(",")[12])

        distances_dict = {}
        distances_only_list = []

        for tmp_record in tmp_data:
            # Calculate distances from all stations to the current station using the wgen_user table
            # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
            # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
            tmp_station_lat = float(tmp_record.split(",")[2])
            tmp_station_lon = float(tmp_record.split(",")[3])

            total_distance = get_distance(tmp_station_lat, tmp_station_lon, current_lat, current_lon)

            if total_distance in distances_only_list:
                continue
            else:
                distances_only_list.append(total_distance)
                distances_dict[str(total_distance)] = tmp_record

        # Now, we get the station in tmp, for the current subbasin.
        station = distances_dict[str(min(distances_only_list))].split(",")[1]
            #this part takes care of OrderID field 

        if not station in done_stations_list:
            done_stations_list.append(station)
            OrderID += 1

            done_stations_dict[station] = OrderID

        for key in done_stations_dict:
            if key == station:
                Sub_OrderID =  int(done_stations_dict[key])


        SubTmp_defaults["Station"] = station
        SubTmp_defaults["MinDist"] = float(min(distances_only_list))
        SubTmp_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
        SubTmp_defaults["OrderID"] = Sub_OrderID
        SubTmp_defaults["TimeStep"] = 0

        SubTmp.insert_row("SubTmp", SubTmp_defaults, True)
#tmp.disconnect()
#SubTmp.disconnect()
