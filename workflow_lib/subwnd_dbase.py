
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB

if not os.path.isfile(variables.wnd_file_txt):
    pass
else:
    subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
    wnd_stations = cj.read_from(variables.wnd_file_txt)

    #wnd_fields = ["ID", "NAME", "LAT", "LONG", "ELEVATION"]
    wnd_values = {}

    # initialising the dictionary
    #for field in wnd_fields:
    #    wnd_values[field] = 0

    wnd = mdt.mdb_with_ops(variables.ProjMDB)
    wnd.connect()
    wnd.create_table("wnd", "[ID]", "INTEGER")
    wnd.add_field("wnd","[NAME]", "TEXT")
    wnd.add_field("wnd","[LAT]", "FLOAT")
    wnd.add_field("wnd","[LONG]", "FLOAT")
    wnd.add_field("wnd","[ELEVATION]", "FLOAT")

    wnd.clear_table("wnd") # in case the table was there and there are records already, we recalculate.



    for i in range (1,len(wnd_stations)):   # the square brackets are used to escape reserved column names
        wnd_values["[ID]"] = int(wnd_stations[i].strip("\n").split(",")[0].strip("'"))
        wnd_values["[NAME]"] = str(wnd_stations[i].strip("\n").split(",")[1].strip("'"))
        wnd_values["[LAT]"] = float(wnd_stations[i].strip("\n").split(",")[2].strip("'"))
        wnd_values["[LONG]"] = float(wnd_stations[i].strip("\n").split(",")[3].strip("'"))
        wnd_values["[ELEVATION]"] = float(wnd_stations[i].strip("\n").split(",")[4].strip("'"))

        wnd.insert_row("wnd", wnd_values, True)

    wnd_data = cj.extract_table_from_mdb(variables.ProjMDB, 'wnd', variables.path + "\\wnd_data.tmp~")


    wnd.create_table("SubWnd", "[ObjectID]", "INTEGER")
    wnd.add_field("SubWnd","[Subbasin]", "INTEGER")
    wnd.add_field("SubWnd","[MinDist]", "FLOAT")
    wnd.add_field("SubWnd","[MinRec]", "INTEGER")
    wnd.add_field("SubWnd","[Station]", "TEXT")
    wnd.add_field("SubWnd","[OrderID]", "INTEGER")
    wnd.add_field("SubWnd","[TimeStep]", "INTEGER")

    wnd.clear_table("SubWnd")

    SubWnd_defaults={}

    """
    # here we commit to table the parameters for the basin to a row in the table wgn
    """
    SubWnd = mdt.mdb_with_ops(variables.ProjMDB)
    SubWnd.clear_table("SubWnd")

    OID = 0
    OrderID = 0
    done_stations_list = []
    done_stations_dict = {}

    for subbasin in subbasins:    # getting field values from from watershed table
        OID += 1

        SubWnd_defaults["ObjectID"] = subbasin.split(",")[0]
        SubWnd_defaults["Subbasin"] = int(subbasin.split(",")[3])

        current_lat = float(subbasin.split(",")[11])
        current_lon = float(subbasin.split(",")[12])

        distances_dict = {}
        distances_only_list = []

        for wnd_record in wnd_data:
            # Calculate distances from all stations to the current station using the wgen_user table
            # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
            # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
            wnd_station_lat = float(wnd_record.split(",")[2])
            wnd_station_lon = float(wnd_record.split(",")[3])

            total_distance = get_distance(wnd_station_lat, wnd_station_lon, current_lat, current_lon)

            if total_distance in distances_only_list:
                continue
            else:
                distances_only_list.append(total_distance)
                distances_dict[str(total_distance)] = wnd_record

        # Now, we get the station in wnd, for the current subbasin.
        station = distances_dict[str(min(distances_only_list))].split(",")[1]
            #this part takes care of OrderID field 

        if not station in done_stations_list:
            done_stations_list.append(station)
            OrderID += 1

            done_stations_dict[station] = OrderID

        for key in done_stations_dict:
            if key == station:
                Sub_OrderID =  int(done_stations_dict[key])


        SubWnd_defaults["Station"] = station
        SubWnd_defaults["MinDist"] = float(min(distances_only_list))
        SubWnd_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
        SubWnd_defaults["OrderID"] = Sub_OrderID
        SubWnd_defaults["TimeStep"] = 0

        SubWnd.insert_row("SubWnd", SubWnd_defaults, True)
#SubWnd.disconnect()
#wnd.disconnect()
