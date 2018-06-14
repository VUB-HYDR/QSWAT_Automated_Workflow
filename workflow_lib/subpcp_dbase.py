
import sys, os

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

def get_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB


if not os.path.isfile(variables.pcp_file_txt):
    pass
else:
    subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
    pcp_stations = cj.read_from(variables.pcp_file_txt)

    #pcp_fields = ["ID", "NAME", "LAT", "LONG", "ELEVATION"]
    pcp_values = {}

    # initialising the dictionary
    #for field in pcp_fields:
    #    pcp_values[field] = 0

    pcp = mdt.mdb_with_ops(variables.ProjMDB)
    pcp.connect()
    pcp.clear_table("pcp")

    for i in range (1,len(pcp_stations)):   # the square brackets are used to escape reserved column names
        pcp_values["[ID]"] = int(pcp_stations[i].strip("\n").split(",")[0].strip("'"))
        pcp_values["[NAME]"] = str(pcp_stations[i].strip("\n").split(",")[1].strip("'"))
        pcp_values["[LAT]"] = float(pcp_stations[i].strip("\n").split(",")[2].strip("'"))
        pcp_values["[LONG]"] = float(pcp_stations[i].strip("\n").split(",")[3].strip("'"))
        pcp_values["[ELEVATION]"] = float(pcp_stations[i].strip("\n").split(",")[4].strip("'"))

        pcp.insert_row("pcp", pcp_values, True)

    pcp_data = cj.extract_table_from_mdb(variables.ProjMDB, 'pcp', variables.path + "\\pcp_data.tmp~")

    SubPcp_defaults={}

    """
    # here we commit to table the parameters for the basin to a row in the table wgn
    """
    SubPcp = mdt.mdb_with_ops(variables.ProjMDB)
    SubPcp.clear_table("SubPcp")

    OID = 0
    OrderID = 0
    done_stations_list = []
    done_stations_dict = {}

    for subbasin in subbasins:    # getting field values from from watershed table
        OID += 1

        SubPcp_defaults["ObjectID"] = subbasin.split(",")[0]
        SubPcp_defaults["Subbasin"] = subbasin.split(",")[3]

        current_lat = float(subbasin.split(",")[11])
        current_lon = float(subbasin.split(",")[12])

        distances_dict = {}
        distances_only_list = []

        for pcp_record in pcp_data:
            # Calculate distances from all stations to the current station using the wgen_user table
            # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
            # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
            pcp_station_lat = float(pcp_record.split(",")[2])
            pcp_station_lon = float(pcp_record.split(",")[3])

            total_distance = get_distance(pcp_station_lat, pcp_station_lon, current_lat, current_lon)

            if total_distance in distances_only_list:
                continue
            else:
                distances_only_list.append(total_distance)
                distances_dict[str(total_distance)] = pcp_record

        # Now, we get the station in pcp, for the current subbasin.
        station = distances_dict[str(min(distances_only_list))].split(",")[1]
            #this part takes care of OrderID field 

        if not station in done_stations_list:
            done_stations_list.append(station)
            OrderID += 1

            done_stations_dict[station] = OrderID

        for key in done_stations_dict:
            if key == station:
                Sub_OrderID =  int(done_stations_dict[key])


        SubPcp_defaults["Station"] = station
        SubPcp_defaults["MinDist"] = float(min(distances_only_list))
        SubPcp_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
        SubPcp_defaults["OrderID"] = Sub_OrderID
        SubPcp_defaults["TimeStep"] = 0

        SubPcp.insert_row("SubPcp", SubPcp_defaults, True)

#pcp.disconnect()
#SubPcp.disconnect()
