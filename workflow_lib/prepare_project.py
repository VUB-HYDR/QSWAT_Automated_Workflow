import sys, os, zipfile, glob, shutil, re
import cj_function_lib as cj
import mdbtools as mdt
path = os.getcwd()

root = path.replace("workflow_lib", "")#[0:-1]
sys.path.insert(0, root)

current_root = sys.argv[1] + "/model"
cj.create_directory(current_root)

import namelist

def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def copyshape(infile, outbase, outdir):
    basename = infile[0:-3] + '*'
    for filename in glob.iglob(basename):
        suffix = os.path.splitext(filename)[1]
        outfile = os.path.join(outdir, outbase + suffix)
        shutil.copy(filename, outfile)

print "____________________________________________________________________________\nPreparing Project...\n"

project_name = namelist.Project_Name
cj.create_directory(os.path.join(root, project_name))

cj.create_directory(os.path.join(current_root, project_name, "Scenarios", "Default", "TablesIn"))
cj.create_directory(os.path.join(current_root, project_name, "Scenarios", "Default", "TablesOut"))
cj.create_directory(os.path.join(current_root, project_name, "Scenarios", "Default", "TxtInOut"))
cj.create_directory(os.path.join(current_root, project_name, "Source", "crop"))
cj.create_directory(os.path.join(current_root, project_name, "Source", "soil", "soilmap"))
cj.create_directory(os.path.join(current_root, project_name, "Watershed", "Grid"))
cj.create_directory(os.path.join(current_root, project_name, "Watershed", "Shapes"))
cj.create_directory(os.path.join(current_root, project_name, "Watershed", "Tables"))
cj.create_directory(os.path.join(current_root, project_name, "Watershed", "temp"))
cj.create_directory(os.path.join(current_root, project_name, "Watershed", "Text"))
cj.create_directory(os.path.join(current_root, project_name, "Weather"))

# Here we copy database files
print "\t> Getting Databases..."

cj.copy_file(root + "/workflow_lib/DefaultProject.mdb", current_root + "/" + project_name + "/" + project_name + ".mdb")
cj.copy_file(root + "/workflow_lib/QSWATRef2012.mdb", current_root + "/" +  project_name + "/" + "QSWATRef2012.mdb")

# put placeholders
print "\t> Extracting placeholders..."
with zipfile.ZipFile(root + "/workflow_lib/placeholdingtiffs.zip","r") as zip_ref:
    zip_ref.extractall(current_root + "/" + project_name + "/Source/")
with zipfile.ZipFile(root + "/workflow_lib/placeholdingshapes.zip","r") as zip_ref:
    zip_ref.extractall(current_root + "/" + project_name + "/Watershed/Shapes/")

print "\t> Getting tiff from dem\t\t\t: " + namelist.Topography
# copy dem as tiff 
cj.convert_raster(sys.argv[1] + "/Data/rasters/" + namelist.Topography, current_root + "/" + project_name + "/Source/dem.tif")

print "\t> Getting landuse and soil maps..."
if os.path.isdir(os.path.join(sys.argv[1], "Data/rasters/", namelist.Soils)):
    cj.copytree(os.path.join(sys.argv[1], "Data/rasters/", namelist.Soils), current_root + "/" + project_name + "/Source/soil/{0}/".format(namelist.Soils))
else:
    cj.copy_file(os.path.join(sys.argv[1], "Data/rasters/", namelist.Soils), os.path.join(current_root, project_name, "Source", "soil", namelist.Soils))

if os.path.isdir(os.path.join(sys.argv[1], "Data/rasters/", namelist.Land_Use)):
    cj.copytree(os.path.join(sys.argv[1], "Data/rasters/", namelist.Land_Use), os.path.join(current_root, project_name, "Source", "crop", namelist.Land_Use))
else:
    cj.copy_file(os.path.join(sys.argv[1], "Data/rasters/", namelist.Land_Use), os.path.join(current_root, project_name, "Source", "crop", namelist.Land_Use))

if not namelist.Burn_in_shape == "":
    burn_in_shape = sys.argv[1] + "/Data/shapes/" + namelist.Burn_in_shape
    if os.path.isfile(burn_in_shape):
        copyshape(burn_in_shape, namelist.Burn_in_shape[0:-4], current_root + "/" + project_name + "/Source/")
    else: 
        print("\t! Error: the specified burn-in file was not found, check that it exists and try again.")

print "\t> Getting outlet shape file\t\t: {0}".format(namelist.Outlet)
outletshapefile = os.path.join(sys.argv[1], "Data", "shapes", namelist.Outlet)

if os.path.isfile(outletshapefile):
    copyshape(outletshapefile, "outlet", current_root + "/" + project_name + "/Watershed/Shapes/")
    copyshape(outletshapefile, "outlet_sel", current_root + "/" + project_name + "/Watershed/Shapes/")
    copyshape(outletshapefile, "outlet_sel_snap", current_root + "/" + project_name + "/Watershed/Shapes/")
else: 
    print("\t! Error: either No outletshape file was specified, or it does not exist.")

print("\t> Getting database tables \t\t: {0}".format(os.path.join(sys.argv[1], "Data", "tables")))

# Here we set lookup tables, usersoil and WGEN_user in the Ref and Project Databases
soil_lu       = cj.read_from(os.path.join(sys.argv[1], "Data", "tables", namelist.soil_lookup))
landuse_lu    = cj.read_from(os.path.join(sys.argv[1], "Data", "tables", namelist.landuse_lookup))
WGEN_data     = cj.read_from(os.path.join(sys.argv[1], "Data", "tables", namelist.WGEN_user))
usersoil_data = cj.read_from(os.path.join(sys.argv[1], "Data", "tables", namelist.Usersoil))

print("\t> Configuring databasses \t\t: {0}.mdb & QSWATRef2012.mdb".format(project_name))
prj_dbase = mdt.mdb_with_ops(os.path.join(current_root, project_name, project_name + ".mdb"))
ref_dbase = mdt.mdb_with_ops(os.path.join(current_root, project_name, "QSWATRef2012.mdb"))

# how to remove existing table if any?
try:
   # prj_dbase.delete_table("landuse_lookup")
    prj_dbase.delete_table("hru")
except:
    pass
try:
    prj_dbase.delete_table("soil_lookup")
except:
    pass

prj_dbase.clear_table ("landuse_lookup")
prj_dbase.clear_table("soil_lookup")

try:
    prj_dbase.create_table("landuse_lookup", "LANDUSE_ID", "INTEGER")
except:
    pass

try:
    prj_dbase.add_field("landuse_lookup", "SWAT_CODE", "TEXT")
except:
    pass

try:
    prj_dbase.create_table("soil_lookup", "SOIL_ID", "INTEGER")
except:
    pass
try:
    prj_dbase.add_field("soil_lookup", "SNAM", "TEXT")
except:
    pass

soil_lu_row = {}
for i in range (1, len(soil_lu)):
    soil_lu_row["SOIL_ID"] = soil_lu[i].split(",")[0].strip("\n").strip('"')
    soil_lu_row["SNAM"] = soil_lu[i].split(",")[1].strip("\n").strip('"')

    prj_dbase.insert_row("soil_lookup", soil_lu_row, True)

landuse_lu_row = {}
for i in range (1, len(landuse_lu)):
    landuse_lu_row["LANDUSE_ID"] = landuse_lu[i].split(",")[0].strip("\n").strip('"')
    landuse_lu_row["SWAT_CODE"] = landuse_lu[i].split(",")[1].strip("\n").strip('"')

    prj_dbase.insert_row("landuse_lookup", landuse_lu_row, True)

usersoil_table = {}
wgen_user = {}

wgen_headers = WGEN_data[0].split(",")
usersoil_headers = usersoil_data[0].split(",")

ref_dbase.clear_table("WGEN_user")
ref_dbase.clear_table("usersoil")

import re
for line in WGEN_data:
    if (line.split(",")[1] == 'STATION') or (line.split(",")[1] == 'OBJECTID'):
        continue
    for i in range(0,len(wgen_headers)):
        try:
            wgen_user[WGEN_data[0].split(",")[i].strip(" ")] = cj._removeNonAscii(line.split(",")[i])
        except:
            print "\t\t! Your WGEN_user table may have one or more non-ascii characters: convert it at http://utils.paranoiaworks.org/diacriticsremover/"
    ref_dbase.insert_row("WGEN_user", wgen_user, True)  

for line in usersoil_data:
    if line.split(",")[1] == 'MUID':
        continue
    for i in range(0,len(usersoil_headers)):
        usersoil_table[usersoil_data[0].split(",")[i].strip("\xef\xbb\xbf")] = line.split(",")[i]
    ref_dbase.insert_row("usersoil", usersoil_table, True)

ref_dbase.disconnect()
prj_dbase.disconnect()

# Get projection info for the project file
proj4, is_proj = cj.get_proj4_from(current_root + "/" + project_name + "/Source/crop/" + namelist.Land_Use)

if not is_proj:
    print("\t\t! Warning: makesure your land use map is projected.")

xmin, ymax, xmax, ymin = cj.get_extents(current_root + "/" + project_name + "/Source/dem.tif")
epsg_code, srs_id, prj_name = cj.get_auth(current_root + "/" + project_name + "/Source/dem.tif")
soil_epsg_code, soil_srs_id, soil_prj_name = cj.get_auth(os.path.join(current_root, project_name, "Source", "crop", namelist.Land_Use))

cj.write_to("epsg_code.tmp~", "{0}".format(epsg_code))

projlist = proj4.split(" ")

proj4_dic = {}
for item in projlist:
    if (item == '+no_defs') or (item == ''):
        continue
    else:
        proj4_dic[item.split("=")[0]] = item.split("=")[1]

## Here we replace the text inside the project file
project_file_list = cj.read_from(root + "/workflow_lib/template.qgs")
project_file_string = ""
for line in project_file_list:
    project_file_string += line

new_pj_string = project_file_string.replace('<slopeBands type="QString">[0, 9999]</slopeBands>', '<slopeBands type="QString">[' + namelist.Slope_classes + ']</slopeBands>')
new_pj_string = new_pj_string.replace('<threshold type="int">0000</threshold>', '<threshold type="int">' + str(namelist.WS_threshold) + '</threshold>')
new_pj_string = new_pj_string.replace('<snapThreshold type="int">000</snapThreshold>', '<snapThreshold type="int">' + str(namelist.OUT_Snap_threshold) + '</snapThreshold>')
new_pj_string = new_pj_string.replace('default_project_name', project_name)

if namelist.HRU_creation_method == 1:
    new_pj_string = new_pj_string.replace('<isMultiple type="int">1</isMultiple>', '<isMultiple type="int">0</isMultiple>')
if namelist.HRU_creation_method == 2:
    new_pj_string = new_pj_string.replace('<isDominantHRU type="int">0</isDominantHRU>', '<isDominantHRU type="int">1</isDominantHRU>')
    new_pj_string = new_pj_string.replace('<isMultiple type="int">1</isMultiple>', '<isMultiple type="int">0</isMultiple>')
if namelist.HRU_creation_method == 3:
    new_pj_string = new_pj_string.replace('<areaVal type="int">0</areaVal>', '<areaVal type="int">' + str(namelist.Target_Value) + '</areaVal>')
    new_pj_string = new_pj_string.replace('<isArea type="int">0</isArea>', '<isArea type="int">1</isArea>')
if namelist.HRU_creation_method == 4:
    new_pj_string = new_pj_string.replace('<isTarget type="int">0</isTarget>', '<isTarget type="int">1</isTarget>')
    new_pj_string = new_pj_string.replace('<targetVal type="int">0</targetVal>', '<targetVal type="int">' + str(namelist.Target_Value) + '</targetVal>')
if namelist.HRU_creation_method == 5:
    new_pj_string = new_pj_string.replace('<landuseVal type="int">0</landuseVal>', '<landuseVal type="int">' + str(namelist.HRU_thres_LandUse) + '</landuseVal>')
    new_pj_string = new_pj_string.replace('<soilVal type="int">0</soilVal>', '<soilVal type="int">' + str(namelist.HRU_thres_Soil) + '</soilVal>')
    new_pj_string = new_pj_string.replace('<slopeVal type="int">0</slopeVal>', '<slopeVal type="int">' + str(namelist.HRU_thres_Slope) + '</slopeVal>')

if namelist.HRU_thresholds_type == 1:
    new_pj_string = new_pj_string.replace('<isArea type="int">0</isArea>', '<isArea type="int">1</isArea>')
if not namelist.Burn_in_shape == "":
    pass
    #new_pj_string = new_pj_string.replace('<burn type="QString"></burn>', '<burn type="QString">Source\\' + namelist.Burn_in_shape + '</burn>')

new_pj_string = new_pj_string.replace('Landuses (Landuse)', 'Landuses (' + str(namelist.Land_Use.split(".")[0]) + ')')
if os.path.isdir(current_root + "/" + project_name + "/Source/crop/" + namelist.Land_Use):
    new_pj_string = new_pj_string.replace('crop/landuse/hdr.adf', 'crop/' + str(namelist.Land_Use) + '/hdr.adf')
    new_pj_string = new_pj_string.replace('crop\\landuse\\hdr.adf', 'crop\\' + str(namelist.Land_Use) + '\\hdr.adf')    
else:
    new_pj_string = new_pj_string.replace('crop/landuse/hdr.adf', 'crop/' + str(namelist.Land_Use))        
    new_pj_string = new_pj_string.replace('crop\\landuse\\hdr.adf', 'crop\\' + str(namelist.Land_Use))        

if os.path.isdir(current_root + "/" + project_name + "/Source/soil/" + namelist.Soils):
    new_pj_string = new_pj_string.replace('soil/soilmap/hdr.adf', 'soil/' + str(namelist.Soils) + '/hdr.adf')
    new_pj_string = new_pj_string.replace('soil\\soilmap\\hdr.adf', 'soil\\' + str(namelist.Soils) + '\\hdr.adf')    
else:
    new_pj_string = new_pj_string.replace('soil/soilmap/hdr.adf', 'soil/' + str(namelist.Soils))        
    new_pj_string = new_pj_string.replace('soil\\soilmap\\hdr.adf', 'soil\\' + str(namelist.Soils)) 

new_pj_string = new_pj_string.replace('Landuses__Landuse', 'Landuses__' + str(namelist.Land_Use).split(".")[0])
new_pj_string = new_pj_string.replace('soilmap', '' + str(namelist.Soils).split(".")[0])

# set projection info
new_pj_string = new_pj_string.replace('<proj4>default_proj4</proj4>', '<proj4>' + proj4 + '</proj4>')
new_pj_string = new_pj_string.replace('<projectionacronym>default_projection_acr</projectionacronym>', '<projectionacronym>' + proj4_dic["+proj"] + '</projectionacronym>')
new_pj_string = new_pj_string.replace('<geographicflag>default_flag</geographicflag>', '<geographicflag>' + is_proj + '</geographicflag>')

# set canvas extents
try:
    new_pj_string = new_pj_string.replace('<xmin>300000</xmin>', '<xmin>' + str(xmin) + '</xmin>')
    new_pj_string = new_pj_string.replace('<xmax>350000</xmax>', '<xmax>' + str(xmax) + '</xmax>')
    new_pj_string = new_pj_string.replace('<ymin>1200000</ymin>', '<ymin>' + str(ymin) + '</ymin>')
    new_pj_string = new_pj_string.replace('<ymax>1250000</ymax>', '<ymax>' + str(ymax) + '</ymax>')
except:
    pass

try:
    new_pj_string = new_pj_string.replace('<ellipsoidacronym>default_elipsoid_acr</ellipsoidacronym>', '<ellipsoidacronym>' + proj4_dic["+ellps"] + '</ellipsoidacronym>')
except:
    new_pj_string = new_pj_string.replace('<ellipsoidacronym>default_el_acronym</ellipsoidacronym>', '<ellipsoidacronym>' + '</ellipsoidacronym>')

if not prj_name is None:
    new_pj_string = new_pj_string.replace('<description></description>', '<description>' + prj_name + '</description>')

new_pj_string = new_pj_string.replace('<authid>prj_authid</authid>', '<authid>EPSG:' + epsg_code + '</authid>')
new_pj_string = new_pj_string.replace('<srid>prj_sr_id</srid>', '<srid>' + str(epsg_code) + '</srid>')
new_pj_string = new_pj_string.replace('<srsid>prj_srs_id</srsid>', '<srsid>' + srs_id + '</srsid>')
new_pj_string = new_pj_string.replace('EPSG:prj_authid', 'EPSG:' + epsg_code)
new_pj_string = new_pj_string.replace('EPSG:soil_authid', 'EPSG:' + soil_epsg_code)
new_pj_string = new_pj_string.replace('default_project_name', project_name)

dem_stats = cj.get_raster_stats(current_root + "/" + project_name + "/Source/dem.tif")

new_pj_string = new_pj_string.replace('<item alpha="255" value="376" label="376 - 1671" color="#0a640a"/>', '<item alpha="255" value="' + str(dem_stats['min']) + '" label="' + str(int(dem_stats['min'])) + ' - ' + str(int(((float(dem_stats['mean']) - float(dem_stats['min']))/2) + float(dem_stats['min']))) + '" color="#0a640a"/>')
new_pj_string = new_pj_string.replace('<item alpha="255" value="2318" label="1671 - 2966" color="#997d19"/>', '<item alpha="255" value="' + str(dem_stats['mean']) + '" label="' + str(int(((float(dem_stats['mean']) - float(dem_stats['min']))/2) + float(dem_stats['min']))) + ' - ' + str(int(((float(dem_stats['max']) - float(dem_stats['mean']))/2) + float(dem_stats['mean']))) + '" color="#997d19"/>')
new_pj_string = new_pj_string.replace('<item alpha="255" value="4261" label="2966 - 4261" color="#ffffff"/>', '<item alpha="255" value="' + str(dem_stats['max']) + '" label="' + str(int(((float(dem_stats['max']) - float(dem_stats['mean']))/2) + float(dem_stats['mean']))) + ' - ' + str(int(dem_stats['max'])) + '" color="#ffffff"/>')

cj.write_to(current_root + "/" + project_name + ".qgs", new_pj_string)

# Copying Weather Files
print "\t> Getting Weather Data.."
cj.copytree(sys.argv[1] + "/Data/Weather/", current_root + "/" + project_name + "/Weather/")

print "\t> Finnished...\n____________________________________________________________________________"
