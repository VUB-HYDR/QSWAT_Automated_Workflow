
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB

if not os.path.isfile(variables.hmd_file_txt):
    pass
else:
    subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
    hmd_stations = cj.read_from(variables.hmd_file_txt)

    #hmd_fields = ["ID", "NAME", "LAT", "LONG", "ELEVATION"]
    hmd_values = {}

    # initialising the dictionary
    #for field in hmd_fields:
    #    hmd_values[field] = 0

    hmd = mdt.mdb_with_ops(variables.ProjMDB)
    hmd.connect()
    hmd.create_table("hmd", "[ID]", "INTEGER")
    hmd.add_field("hmd","[NAME]", "TEXT")
    hmd.add_field("hmd","[LAT]", "FLOAT")
    hmd.add_field("hmd","[LONG]", "FLOAT")
    hmd.add_field("hmd","[ELEVATION]", "FLOAT")

    hmd.clear_table("hmd") # in case the table was there and there are records already, we recalculate.

    for i in range (1,len(hmd_stations)):   # the square brackets are used to escape reserved column names
        hmd_values["[ID]"] = int(hmd_stations[i].strip("\n").split(",")[0].strip("'"))
        hmd_values["[NAME]"] = str(hmd_stations[i].strip("\n").split(",")[1].strip("'"))
        hmd_values["[LAT]"] = float(hmd_stations[i].strip("\n").split(",")[2].strip("'"))
        hmd_values["[LONG]"] = float(hmd_stations[i].strip("\n").split(",")[3].strip("'"))
        hmd_values["[ELEVATION]"] = float(hmd_stations[i].strip("\n").split(",")[4].strip("'"))

        hmd.insert_row("hmd", hmd_values, True)

    Hmd_data = cj.extract_table_from_mdb(variables.ProjMDB, 'hmd', variables.path + "\\hmd_data.tmp~")


    hmd.create_table("SubHmd", "[ObjectID]", "INTEGER")
    hmd.add_field("SubHmd","[Subbasin]", "INTEGER")
    hmd.add_field("SubHmd","[MinDist]", "FLOAT")
    hmd.add_field("SubHmd","[MinRec]", "INTEGER")
    hmd.add_field("SubHmd","[Station]", "TEXT")
    hmd.add_field("SubHmd","[OrderID]", "INTEGER")
    hmd.add_field("SubHmd","[TimeStep]", "INTEGER")

    hmd.clear_table("SubHmd")

    SubHmd_defaults={}

    """
    # here we commit to table the parameters for the basin to a row in the table wgn
    """
    SubHmd = mdt.mdb_with_ops(variables.ProjMDB)
    SubHmd.clear_table("SubHmd")

    OID = 0
    OrderID = 0
    done_stations_list = []
    done_stations_dict = {}

    for subbasin in subbasins:    # getting field values from from watershed table
        OID += 1

        SubHmd_defaults["ObjectID"] = subbasin.split(",")[0]
        SubHmd_defaults["Subbasin"] = int(subbasin.split(",")[3])

        current_lat = float(subbasin.split(",")[11])
        current_lon = float(subbasin.split(",")[12])

        distances_dict = {}
        distances_only_list = []

        for Hmd_record in Hmd_data:
            # Calculate distances from all stations to the current station using the wgen_user table
            # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
            # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
            Hmd_station_lat = float(Hmd_record.split(",")[2])
            Hmd_station_lon = float(Hmd_record.split(",")[3])

            total_distance = get_distance(Hmd_station_lat, Hmd_station_lon, current_lat, current_lon)

            if total_distance in distances_only_list:
                continue
            else:
                distances_only_list.append(total_distance)
                distances_dict[str(total_distance)] = Hmd_record

        # Now, we get the station in Hmd, for the current subbasin.
        station = distances_dict[str(min(distances_only_list))].split(",")[1]
            #this part takes care of OrderID field 

        if not station in done_stations_list:
            done_stations_list.append(station)
            OrderID += 1

            done_stations_dict[station] = OrderID

        for key in done_stations_dict:
            if key == station:
                Sub_OrderID =  int(done_stations_dict[key])


        SubHmd_defaults["Station"] = station
        SubHmd_defaults["MinDist"] = float(min(distances_only_list))
        SubHmd_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
        SubHmd_defaults["OrderID"] = Sub_OrderID
        SubHmd_defaults["TimeStep"] = 0

        SubHmd.insert_row("SubHmd", SubHmd_defaults, True)
#SubHmd.disconnect()
#hmd.disconnect()


