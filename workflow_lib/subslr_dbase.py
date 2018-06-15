
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB


if not os.path.isfile(variables.slr_file_txt):
    pass
else:
    subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
    slr_stations = cj.read_from(variables.slr_file_txt)

    #slr_fields = ["ID", "NAME", "LAT", "LONG", "ELEVATION"]
    slr_values = {}

    # initialising the dictionary
    #for field in slr_fields:
    #    slr_values[field] = 0

    slr = mdt.mdb_with_ops(variables.ProjMDB)
    slr.connect()
    try:
        slr.create_table("SubSlr", "ObjectID", "INTEGER")
    except:
        pass
    try:
        slr.add_field("SubSlr", "Subbasin", "INTEGER")
        slr.add_field("SubSlr", "MinDist", "FLOAT")
        slr.add_field("SubSlr", "MinRec", "INTEGER")
        slr.add_field("SubSlr", "Station", "TEXT")
        slr.add_field("SubSlr", "OrderID", "INTEGER")
        slr.add_field("SubSlr", "TimeStep", "INTEGER")
    except:
        pass
        
    slr.clear_table("slr")

    for i in range (1,len(slr_stations)):   # the square brackets are used to escape reserved column names
        slr_values["[ID]"] = int(slr_stations[i].strip("\n").split(",")[0].strip("'"))
        slr_values["[NAME]"] = str(slr_stations[i].strip("\n").split(",")[1].strip("'"))
        slr_values["[LAT]"] = float(slr_stations[i].strip("\n").split(",")[2].strip("'"))
        slr_values["[LONG]"] = float(slr_stations[i].strip("\n").split(",")[3].strip("'"))
        slr_values["[ELEVATION]"] = float(slr_stations[i].strip("\n").split(",")[4].strip("'"))

        slr.insert_row("slr", slr_values, True)

    slr_data = cj.extract_table_from_mdb(variables.ProjMDB, 'slr', variables.path + "\\slr_data.tmp~")

    SubSlr_defaults={}

    """
    # here we commit to table the parameters for the basin to a row in the table wgn
    """
    SubSlr = mdt.mdb_with_ops(variables.ProjMDB)
    SubSlr.clear_table("SubSlr")

    OID = 0
    OrderID = 0
    done_stations_list = []
    done_stations_dict = {}

    for subbasin in subbasins:    # getting field values from from watershed table
        OID += 1

        SubSlr_defaults["ObjectID"] = subbasin.split(",")[0]
        SubSlr_defaults["Subbasin"] = subbasin.split(",")[3]

        current_lat = float(subbasin.split(",")[11])
        current_lon = float(subbasin.split(",")[12])

        distances_dict = {}
        distances_only_list = []

        for slr_record in slr_data:
            # Calculate distances from all stations to the current station using the wgen_user table
            # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
            # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
            slr_station_lat = float(slr_record.split(",")[2])
            slr_station_lon = float(slr_record.split(",")[3])

            total_distance = get_distance(slr_station_lat, slr_station_lon, current_lat, current_lon)

            if total_distance in distances_only_list:
                continue
            else:
                distances_only_list.append(total_distance)
                distances_dict[str(total_distance)] = slr_record

        # Now, we get the station in slr, for the current subbasin.
        station = distances_dict[str(min(distances_only_list))].split(",")[1]
            #this part takes care of OrderID field 

        if not station in done_stations_list:
            done_stations_list.append(station)
            OrderID += 1

            done_stations_dict[station] = OrderID

        for key in done_stations_dict:
            if key == station:
                Sub_OrderID =  int(done_stations_dict[key])


        SubSlr_defaults["Station"] = station
        SubSlr_defaults["MinDist"] = float(min(distances_only_list))
        SubSlr_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
        SubSlr_defaults["OrderID"] = Sub_OrderID
        SubSlr_defaults["TimeStep"] = 0

        SubSlr.insert_row("SubSlr", SubSlr_defaults, True)

#Slr.disconnect()
#SubSlr.disconnect()
