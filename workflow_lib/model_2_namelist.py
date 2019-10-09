'''
Author      : Celray James CHAWANDA (celray.chawanda@outlook.com)
Institution : Vrije Universiteit Brussel (VUB)

This script gets model information and creates from it a namelist
'''

import namelist
import os, sys
import mdbtools as mdt
import cj_function_lib
from namelist_template import namelist_string
from shutil import copytree
import ntpath

from init_file import ProjMDB, QSWAT_MDB, WeatherDIR, DefaultSimDir, ProjName, ProjDir, root

root = root.replace("model/", "")

def get_db_value(connection, table, column_name, row_number):
    '''
    Function to retrieve value specifying row and column
    '''
    connection.get_values(table)
    column_index = 0
    for col_n in connection.col_names:
        if col_n == column_name:
            break
        else:
            column_index += 1

    value = connection.columns[row_number - 1][column_index]
    return value

def report(string_):
    print("\t> {strng}".format(strng = string_))

# variables
shape_extensions = ("shp", "shx", "dbf", "prj")

print("creating namelist and data from model")

# create data directory structure
report("creating populating data directory structure")
dirs = ["weather", "tables", "shapes"]
for dir_name in dirs:
    if not os.path.isdir("{rt}Data/{dname}".format(rt = root, dname = dir_name)):
        os.makedirs("{rt}Data/{dname}".format(rt = root, dname = dir_name))

# copy rasters, shapefiles
all_shapes = cj_function_lib.list_files_from("{pjd}Watershed/Shapes".format(pjd = ProjDir), "*")
all_in_source = cj_function_lib.list_files_from("{pjd}Source".format(pjd = ProjDir), "*")

outlet_shape = None
dem_name = None

# # outlet
for s_file in all_shapes:
    if "_snap" in s_file:
        outlet_shape = ntpath.basename(s_file).split(".")[0]
        break
# # dem
for source_file in all_in_source:
    if "sd8.tif" in source_file:
        dem_name = ntpath.basename(source_file).replace("sd8", "")
        break

for sf_extension in shape_extensions:
    cj_function_lib.copy_file("{pjd}/Watershed/Shapes/{basename}.{sfe}".format(
        pjd = ProjDir, sfe = sf_extension, basename = outlet_shape),
        "{rt}Data/shapes/outlet.{sfe}".format(sfe = sf_extension, rt = root)
        )
    cj_function_lib.copy_file("{pjd}/Watershed/Shapes/{basename}.{sfe}".format(
        pjd = ProjDir, sfe = sf_extension, basename = "riv1"),
        "{rt}Data/shapes/riv1.{sfe}".format(sfe = sf_extension, rt = root)
        )

cj_function_lib.copy_file("{pjd}Source/{dem_n}".format(dem_n = dem_name, pjd = ProjDir), "{rt}Data/rasters/".format(rt = root))

# # soil and land use
soil_map_list = os.listdir("{pjd}Source/soil".format(pjd = ProjDir))
landuse_map_list = os.listdir("{pjd}Source/crop".format(pjd = ProjDir))

dir_soil = False
dir_landuse = False
soil_raster_name = None
landuse_raster_name = None

for sm_item in soil_map_list:
    if os.path.isdir("{pjd}Source/soil/{so}".format(so = sm_item, pjd = ProjDir)):
        dir_soil = True
        soil_raster_name = sm_item
        break
    if sm_item.endswith(".tif"):
        soil_raster_name = sm_item

for lm_item in landuse_map_list:
    if os.path.isdir("{pjd}Source/crop/{lu}".format(lu = lm_item, pjd = ProjDir)):
        dir_landuse = True
        landuse_raster_name = lm_item
        break
    if lm_item.endswith(".tif"):
        landuse_raster_name = lm_item

if not dir_soil:
    cj_function_lib.copy_file("{pjd}Source/soil/{so}".format(so = soil_raster_name, pjd = ProjDir), "{rt}Data/rasters/".format(rt = root))
else:
    if not os.path.isdir("{rt}Data/rasters/{soil_dir}".format(soil_dir = soil_raster_name, rt = root)):
        os.makedirs("{rt}Data/rasters/{soil_dir}".format(soil_dir = soil_raster_name, rt = root))
    s_copy_list = cj_function_lib.list_files_from("{pjd}Source/soil/{so}".format(so = soil_raster_name, pjd = ProjDir), "*")
    for s_c_item in s_copy_list:
        cj_function_lib.copy_file(s_c_item, "{rt}Data/rasters/{soil_dir}".format(soil_dir = soil_raster_name, rt = root))

if not dir_landuse:
    cj_function_lib.copy_file("{pjd}Source/crop/{so}".format(so = landuse_raster_name, pjd = ProjDir), "{rt}Data/rasters/".format(rt = root))
else:
    if not os.path.isdir("{rt}Data/rasters/{crop_dir}".format(crop_dir = landuse_raster_name, rt = root)):
        os.makedirs("{rt}Data/rasters/{crop_dir}".format(crop_dir = landuse_raster_name, rt = root))
    l_copy_list = cj_function_lib.list_files_from("{pjd}Source/crop/{lu}".format(lu = landuse_raster_name, pjd = ProjDir), "*")
    for l_c_item in l_copy_list:
        cj_function_lib.copy_file(l_c_item, "{rt}Data/rasters/{crop_dir}".format(crop_dir = landuse_raster_name, rt = root))

# # get thresholds and options
report("retrieving thresholds and model options")

project_string_list = cj_function_lib.read_from("{dir}model/{fn}.qgs".format(dir = root, fn = ProjName))
project_string = ""

for pj_line in project_string_list:
    project_string += pj_line

slope_classes = project_string.split('<slopeBands type="QString">[')[-1].split("]</slopeBands")[0]
ws_threshold = project_string.split('<threshold type="int">')[-1].split("</threshold>")[0]
snap_threshold = project_string.split('<snapThreshold type="int">')[-1].split("</snapThreshold>")[0]
is_multiple = project_string.split('<isMultiple type="int">')[-1].split("</isMultiple>")[0]
is_dominant_hru = project_string.split('<isDominantHRU type="int">')[-1].split("</isDominantHRU>")[0]
area_val = project_string.split('<areaVal type="int">')[-1].split("</areaVal>")[0]
is_area = project_string.split('<isArea type="int">')[-1].split("</isArea>")[0]
is_target = project_string.split('<isTarget type="int">')[-1].split("</isTarget>")[0]
target_val = project_string.split('<targetVal type="int">')[-1].split("</targetVal>")[0]
land_use_value = project_string.split('<landuseVal type="int">')[-1].split("</landuseVal>")[0]
soil_value = project_string.split('<soilVal type="int">')[-1].split("</soilVal>")[0]
slope_value = project_string.split('<slopeVal type="int">')[-1].split("</slopeVal>")[0]

land_use_lookup = project_string.split('<landuse>')[-1].split("</landuse>")[0]
land_use_lookup = land_use_lookup.split('<table type="QString">')[-1].split("</table>")[0]
soil_lookup = project_string.split('<soil>')[-1].split("</soil>")[0]
soil_lookup = soil_lookup.split('<table type="QString">')[-1].split("</table>")[0]


hru_creation_method = None
target_value = None

if is_multiple == "0":
    hru_creation_method = 1
elif (is_multiple == "0") and (is_dominant_hru == "1"):
    hru_creation_method = 2
elif is_area == "1":
    hru_creation_method = 3
    target_value = area_val
elif is_target == "1":
    hru_creation_method = 4
    target_value = target_val
elif (is_multiple == "1") and (is_dominant_hru == "0"):
    hru_creation_method = 5

# check parameter files
report("retrieving parameter file (model.in) if present")
if not os.path.isdir("{rt}/Data/parameters/".format(rt = root)):
    os.makedirs("{rt}/Data/parameters/".format(rt = root))

if not os.path.isfile("{txt_dir}TxtInOut/model.in".format(txt_dir = DefaultSimDir)):
    calibration_file = ""
else:
    calibration_file = "model.in"
    cj_function_lib.copy_file("{txt_dir}TxtInOut/model.in".format(txt_dir = DefaultSimDir), "{rt}/Data/parameters/model.in".format(rt = root))


# replace values in project string

if is_area == "0":
    is_area = 2

# get database data
pj_db = mdt.mdb_with_ops("{rt}model/{nm}/{nm}.mdb".format(rt = root, nm = ProjName))
rf_db = mdt.mdb_with_ops("{rt}model/{nm}/QSWATRef2012.mdb".format(rt = root, nm = ProjName))

pj_db.connect()
rf_db.connect()

pj_db.get_values(land_use_lookup)
land_lu_string = "LANDUSE_ID,SWAT_CODE\n"
for row in pj_db.columns:
    land_lu_string += "{code},{lu_c}\n".format(code = row[0], lu_c = row[1])
cj_function_lib.write_to("{rt}Data/tables/{fn}.csv".format(rt = root, fn = land_use_lookup), land_lu_string)

pj_db.get_values(soil_lookup)
soil_string = "SOIL_ID,SNAM\n"
for row in pj_db.columns:
    soil_string += "{code},{so_c}\n".format(code = row[0], so_c = row[1])
cj_function_lib.write_to("{rt}Data/tables/{fn}.csv".format(rt = root, fn = soil_lookup), soil_string)

rf_db.get_values("WGEN_user")
wgen_string = ','.join(rf_db.col_names) + "\n"
for row_ in rf_db.columns:
    str_row = [str(x) for x in row_]
    wgen_string += ','.join(str_row) + "\n"
cj_function_lib.write_to("{rt}Data/tables/{fn}.csv".format(rt = root, fn = "WGEN_user"), wgen_string)

rf_db.get_values("usersoil")
usersoil_string = ','.join(rf_db.col_names) + "\n"
for row_ in rf_db.columns:
    str_row = [str(x) for x in row_]
    usersoil_string += ','.join(str_row) + "\n"
cj_function_lib.write_to("{rt}Data/tables/{fn}.csv".format(rt = root, fn = "usersoil"), usersoil_string)

period = get_db_value(pj_db, "cio", "IYR", 1) + " - " + str(int(get_db_value(pj_db, "cio", "IYR", 1)) + int(get_db_value(pj_db, "cio", "NBYR", 1)) - 1)
nyskip = get_db_value(pj_db, "cio", "NYSKIP", 1)



ipet = get_db_value(pj_db, "bsn", "IPET", 1)
routing_method = get_db_value(pj_db, "bsn", "IRTE", 1)
if int(routing_method) == 0:
    routing_method = 2

ievent = get_db_value(pj_db, "bsn", "IEVENT", 1)

if int(ievent) == 0:
    rainfall_ts = 1
    runoff_method = 1
    routing_ts = 1
elif int(ievent) == 1:
    rainfall_ts = 1
    runoff_method = 2
    routing_ts = 1
elif int(ievent) == 2:
    rainfall_ts = 2
    runoff_method = 2
    routing_ts = 1
elif int(ievent) == 3:
    rainfall_ts = 2
    runoff_method = 2
    routing_ts = 2

namelist_string = namelist_string.format(
    ROUTING_METHOD = routing_method,
    ROUTING_TS = routing_ts,
    RAINFALL_TS = rainfall_ts,
    RUNOFF_METHOD = runoff_method,
    ET_METHOD = ipet + 1,
    NAME = ProjName,
    DEM = dem_name,
    SOIL = soil_raster_name,
    LANDUSE = landuse_raster_name,
    OUTLET = "outlet.shp",
    WS_THRES_TYPE = "1",
    WS_THRES_VAL = ws_threshold,
    OUT_SNAP = snap_threshold,
    BURN_IN_SHAPE = "" ,
    SLOPE_CLASSES = slope_classes,
    HRU_METHOD = hru_creation_method,
    HRU_THRES_TYPE = is_area,
    HRU_THRES_LU = land_use_value,
    HRU_THRES_SOIL = soil_value,
    HRU_THRES_SLOPE = slope_value,
    HRU_TARGET = target_value,
    SOIL_LOOKUP = soil_lookup + ".csv",
    LANDUSE_LOOKUP = land_use_lookup + ".csv",
    CAL_FILE = calibration_file,
    USERSOIL = "usersoil.csv",
    WGEN = "WGEN_user.csv",
    MODEL_RUN_PERIOD = period,
    WARM_UP = nyskip,
    )

pj_db.disconnect()
rf_db.disconnect()

name_list_id = 1
if not os.path.isdir("{rt}Data/old_namelists".format(rt = root)):
    os.makedirs("{rt}Data/old_namelists".format(rt = root))

nl_path = "{rt}Data/old_namelists/namelist_{fn}.py".format(rt = root, fn = name_list_id)

while os.path.isfile("{rt}Data/old_namelists/namelist_{fn}.py".format(rt = root, fn = name_list_id)):
    name_list_id += 1
    nl_path = "{rt}Data/old_namelists/namelist_{fn}.py".format(rt = root, fn = name_list_id)


cj_function_lib.copy_file("{rt}namelist.py".format(rt = root), nl_path)

cj_function_lib.write_to("{rt}{fn}.py".format(rt = root, fn = "namelist"), namelist_string)

# get weather info
report("preparing weather input data")

pcp_list = None
tmp_list = None
slr_list = None
hmd_list = None
wnd_list = None

if os.path.isfile("{def_dir}TxtInOut/pcp1.pcp".format(def_dir = DefaultSimDir)):
    pcp_list = cj_function_lib.read_from("{def_dir}/TxtInOut/pcp1.pcp".format(def_dir = DefaultSimDir))
if os.path.isfile("{def_dir}TxtInOut/slr.slr".format(def_dir = DefaultSimDir)):
    slr_list = cj_function_lib.read_from("{def_dir}/TxtInOut/slr.slr".format(def_dir = DefaultSimDir))
if os.path.isfile("{def_dir}TxtInOut/wnd.wnd".format(def_dir = DefaultSimDir)):
    wnd_list = cj_function_lib.read_from("{def_dir}/TxtInOut/wnd.wnd".format(def_dir = DefaultSimDir))
if os.path.isfile("{def_dir}TxtInOut/hmd.hmd".format(def_dir = DefaultSimDir)):
    hmd_list = cj_function_lib.read_from("{def_dir}/TxtInOut/hmd.hmd".format(def_dir = DefaultSimDir))
if os.path.isfile("{def_dir}TxtInOut/tmp1.tmp".format(def_dir = DefaultSimDir)):
    tmp_list = cj_function_lib.read_from("{def_dir}/TxtInOut/tmp1.tmp".format(def_dir = DefaultSimDir))
if os.path.isfile("{def_dir}TxtInOut/Tmp1.Tmp".format(def_dir = DefaultSimDir)):
    tmp_list = cj_function_lib.read_from("{def_dir}/TxtInOut/Tmp1.Tmp".format(def_dir = DefaultSimDir))

class station_data:
    def __init__(self, st_name):
        self.station_name = st_name
        self.start_date = None
        self.timeseries = []
        self.elevation = None
        self.latitude = None
        self.longitude = None

# # retrieve precipitation
if not pcp_list is None:
    if pcp_list[0].endswith(",\n"):
        pcp_list[0] = pcp_list[0][0:-2]
    pcp_station_list = pcp_list[0].strip("Station  ").strip("\n").split(",")
    wnd_station_list = []
    slr_station_list = []
    hmd_station_list = []
    pcp_lati_list = pcp_list[1].strip("Lati").strip("\n")
    pcp_long_list = pcp_list[2].strip("Long").strip("\n")
    pcp_elev_list = pcp_list[3].strip("Elev").strip("\n")

    for c_index in range(0,13):
        pcp_lati_list = pcp_lati_list.replace("  ", " ")
        pcp_long_list = pcp_long_list.replace("  ", " ")
        pcp_elev_list = pcp_elev_list.replace("  ", " ")

    pcp_lati_list = pcp_lati_list.split(" ")
    pcp_long_list = pcp_long_list.split(" ")
    pcp_elev_list = pcp_elev_list.split(" ")

    pcp_dictionary = {}

    slice_index = 1
    for p_station in pcp_station_list:
        if p_station == "":
            slice_index += 1
            continue
        pcp_dictionary[p_station] = station_data(p_station)
        pcp_dictionary[p_station].start_date = pcp_list[4][:4] + "0101"
        pcp_dictionary[p_station].elevation = pcp_elev_list[slice_index]
        pcp_dictionary[p_station].longitude = pcp_long_list[slice_index]
        pcp_dictionary[p_station].latitude = pcp_lati_list[slice_index]
        slice_index += 1

    for p_line in pcp_list:
        if p_line.startswith("Stat") or p_line.startswith("Lati") or p_line.startswith("Long") or p_line.startswith("Elev"):
            continue

        slice_marker = 7
        for p_stat in pcp_station_list:
            pcp_dictionary[p_stat].timeseries.append(str(float(p_line[slice_marker:slice_marker + 5].strip("\n"))))
            slice_marker += 5

    # write pcp files
    pcp_fork = "ID,NAME,LAT,LONG,ELEVATION\n"
    wnd_fork = "ID,NAME,LAT,LONG,ELEVATION\n"
    slr_fork = "ID,NAME,LAT,LONG,ELEVATION\n"
    hmd_fork = "ID,NAME,LAT,LONG,ELEVATION\n"
    station_count = 1
    for w_station in pcp_station_list:
        pcp_fork += "{id},{s_name},{lat},{lon},{elev}\n".format(id = station_count, s_name = w_station, lat = pcp_dictionary[w_station].latitude, lon = pcp_dictionary[w_station].longitude, elev =  pcp_dictionary[w_station].elevation)
        wnd_fork += "{id},{s_name},{lat},{lon},{elev}\n".format(id = station_count, s_name = "wnd_" + str(station_count), lat = pcp_dictionary[w_station].latitude, lon = pcp_dictionary[w_station].longitude, elev =  pcp_dictionary[w_station].elevation)
        slr_fork += "{id},{s_name},{lat},{lon},{elev}\n".format(id = station_count, s_name = "slr_" + str(station_count), lat = pcp_dictionary[w_station].latitude, lon = pcp_dictionary[w_station].longitude, elev =  pcp_dictionary[w_station].elevation)
        hmd_fork += "{id},{s_name},{lat},{lon},{elev}\n".format(id = station_count, s_name = "hmd_" + str(station_count), lat = pcp_dictionary[w_station].latitude, lon = pcp_dictionary[w_station].longitude, elev =  pcp_dictionary[w_station].elevation)
        st_ts_string =  "{0}\n".format(pcp_dictionary[w_station].start_date)

        wnd_station_list.append("wnd_" + str(station_count))
        slr_station_list.append("slr_" + str(station_count))
        hmd_station_list.append("hmd_" + str(station_count))

        for ts_value in pcp_dictionary[w_station].timeseries:
            st_ts_string += "{0}\n".format(ts_value)

        cj_function_lib.write_to("{rt}/Data/weather/{st_n}.txt".format(rt = root, st_n = w_station), st_ts_string)

        station_count += 1
    cj_function_lib.write_to("{rt}/Data/weather/pcp.txt".format(rt = root, st_n = w_station), pcp_fork)
    cj_function_lib.write_to("{rt}/Data/weather/wnd.txt".format(rt = root, st_n = w_station), wnd_fork)
    cj_function_lib.write_to("{rt}/Data/weather/slr.txt".format(rt = root, st_n = w_station), slr_fork)
    cj_function_lib.write_to("{rt}/Data/weather/hmd.txt".format(rt = root, st_n = w_station), hmd_fork)

# # retrieve wind
wnd_dictionary = {}
if not wnd_list is None:
    for w_station in wnd_station_list:
        wnd_dictionary[w_station] = station_data(w_station)
        wnd_dictionary[w_station].start_date = wnd_list[1][:4] + "0101"
        
    for w_line in wnd_list:
        if w_line.startswith("Input"):
            continue
        slice_marker = 7
        for w_stat in wnd_station_list:
            wnd_dictionary[w_stat].timeseries.append(str(float(w_line[slice_marker:slice_marker + 8].strip("\n"))))
            slice_marker += 8

    # write wind files
    for w_station in wnd_station_list:
        st_ts_string =  "{0}\n".format(wnd_dictionary[w_station].start_date)
        for ts_value in wnd_dictionary[w_station].timeseries:
            st_ts_string += "{0}\n".format(ts_value)

        cj_function_lib.write_to("{rt}/Data/weather/{st_n}.txt".format(rt = root, st_n = w_station), st_ts_string)

# # retrieve solar_radiation
slr_dictionary = {}
if not slr_list is None:
    for s_station in slr_station_list:
        slr_dictionary[s_station] = station_data(s_station)
        slr_dictionary[s_station].start_date = slr_list[1][:4] + "0101"

    for s_line in slr_list:
        if s_line.startswith("Input"):
            continue
        slice_marker = 7
        for s_stat in slr_station_list:
            slr_dictionary[s_stat].timeseries.append(str(float(s_line[slice_marker:slice_marker + 8].strip("\n"))))
            slice_marker += 8

    # write solar_radiation files
    for s_station in slr_station_list:
        st_ts_string =  "{0}\n".format(slr_dictionary[s_station].start_date)
        for ts_value in slr_dictionary[s_station].timeseries:
            st_ts_string += "{0}\n".format(ts_value)

        cj_function_lib.write_to("{rt}/Data/weather/{st_n}.txt".format(rt = root, st_n = s_station), st_ts_string)

# # retrieve humidity
hmd_dictionary = {}
if not hmd_list is None:
    for h_station in hmd_station_list:
        hmd_dictionary[h_station] = station_data(h_station)
        hmd_dictionary[h_station].start_date = hmd_list[1][:4] + "0101"

    for s_line in hmd_list:
        if s_line.startswith("Input"):
            continue
        slice_marker = 7
        for s_stat in hmd_station_list:
            hmd_dictionary[s_stat].timeseries.append(str(float(s_line[slice_marker:slice_marker + 8].strip("\n"))))
            slice_marker += 8

    # write retrieve humidity files
    for h_station in hmd_station_list:
        st_ts_string =  "{0}\n".format(hmd_dictionary[h_station].start_date)
        for ts_value in hmd_dictionary[h_station].timeseries:
            st_ts_string += "{0}\n".format(ts_value)

        cj_function_lib.write_to("{rt}/Data/weather/{st_n}.txt".format(rt = root, st_n = h_station), st_ts_string)


# # retrieve temperature
if not tmp_list is None:
    if tmp_list[0].endswith(",\n"):
        tmp_list[0] = tmp_list[0][0:-2]
    tmp_station_list = tmp_list[0].strip("Station  ").strip("\n").split(",")
    tmp_lati_list = tmp_list[1].strip("Lati").strip("\n")
    tmp_long_list = tmp_list[2].strip("Long").strip("\n")
    tmp_elev_list = tmp_list[3].strip("Elev").strip("\n")

    for c_index in range(0,13):
        tmp_lati_list = tmp_lati_list.replace("  ", " ")
        tmp_long_list = tmp_long_list.replace("  ", " ")
        tmp_elev_list = tmp_elev_list.replace("  ", " ")

    tmp_lati_list = tmp_lati_list.split(" ")
    tmp_long_list = tmp_long_list.split(" ")
    tmp_elev_list = tmp_elev_list.split(" ")

    tmp_dictionary = {}

    slice_index = 1
    for t_station in tmp_station_list:
        if t_station == "":
            slice_index += 1
            continue
        tmp_dictionary[t_station] = station_data(t_station)
        tmp_dictionary[t_station].start_date = tmp_list[4][:4] + "0101"
        tmp_dictionary[t_station].elevation = tmp_elev_list[slice_index]
        tmp_dictionary[t_station].longitude = tmp_long_list[slice_index]
        tmp_dictionary[t_station].latitude = tmp_lati_list[slice_index]
        slice_index += 1

    for p_line in tmp_list:
        if p_line.startswith("Stat") or p_line.startswith("Lati") or p_line.startswith("Long") or p_line.startswith("Elev"):
            continue

        slice_marker = 7
        for p_stat in tmp_station_list:
            tmp_dictionary[p_stat].timeseries.append((str(float(p_line[slice_marker:slice_marker + 5].strip("\n"))), str(float(p_line[slice_marker + 5:slice_marker + 10].strip("\n")))))
            slice_marker += 10

    # write tmp files
    tmp_fork = "ID,NAME,LAT,LONG,ELEVATION\n"
    station_count = 1
    for t_station in tmp_station_list:
        tmp_fork += "{id},{s_name},{lat},{lon},{elev}\n".format(id = station_count, s_name = t_station, lat = tmp_dictionary[t_station].latitude, lon = tmp_dictionary[t_station].longitude, elev =  tmp_dictionary[t_station].elevation)
        st_ts_string =  "{0}\n".format(tmp_dictionary[t_station].start_date)

        wnd_station_list.append("wnd_" + str(station_count))
        slr_station_list.append("slr_" + str(station_count))
        hmd_station_list.append("hmd_" + str(station_count))

        for ts_value in tmp_dictionary[t_station].timeseries:
            st_ts_string += "{0},{1}\n".format(ts_value[0], ts_value[1])

        cj_function_lib.write_to("{rt}/Data/weather/{st_n}.txt".format(rt = root, st_n = t_station), st_ts_string)

        station_count += 1
    cj_function_lib.write_to("{rt}/Data/weather/tmp.txt".format(rt = root, st_n = t_station), tmp_fork)

report("cleaning up...")

try:
    os.remove("{rt}namelist.pyc".format(rt = root))
except:
    pass

report("finished...")
