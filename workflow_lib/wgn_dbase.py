
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt
import ogr, osr

def transform_point_coordinates(point_x, point_y, output_epsg, input_epsg = 4326):
    """
    function to transform the ponts to projection of the dem before calculating distance
    """
    # create a geometry from coordinates
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(point_x, point_y)

    # create coordinate transformation
    inSpatialRef = osr.SpatialReference()
    inSpatialRef.ImportFromEPSG(input_epsg)

    outSpatialRef = osr.SpatialReference()
    outSpatialRef.ImportFromEPSG(output_epsg)

    coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)
    # transform point
    point.Transform(coordTransform)
    return point.GetX(), point.GetY()

def get_distance(x1, y1, z1, x2, y2, z2, epsg_):
    """
    The distance units must be the same, elevation is not used and can be removed from arguments
    """
    x2_, y2_ = transform_point_coordinates(x2, y2, epsg_)
    x1_, y1_ = transform_point_coordinates(x1, y1, epsg_)
    #distance = ((x2_ - x1_)**2 + (y2_ - y1_)**2)**0.5
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

#print variables.ProjMDB
#print variables.QSWAT_MDB

transform_epsg = int(cj.read_from(variables.path + "/epsg_code.tmp~")[0])

subbasins = cj.extract_table_from_mdb(variables.ProjMDB, 'Watershed', variables.path + "\\watershed.tmp~")
wgnrgn = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'wgnrng', variables.path + "\\wgnrgn.tmp~")
WGEN_user = cj.extract_table_from_mdb(variables.QSWAT_MDB, 'WGEN_user', variables.path + "\\WGEN_user.tmp~")

wgn_defaults={}
SubWgn_defaults={}

for record in wgnrgn: # Getting a list of parameter names for wgn and their defaults
    if record.split(",")[0].strip(" ") != "":
        wgn_defaults[record.split(",")[0].strip("\[").strip("\]")] = record.split(",")[3]

#wgn_defaults.pop("ALPHA_BF_D")

count_up_fields = ["TMPMX", "TMPMN", "TMPSTDMX", "TMPSTDMN", "PCPMM", "PCPSTD", "PCPSKW", "PR_W1", "PR_W2", "PCPD", "RAINHHMX", "SOLARAV", "DEWPT", "WNDAV"]

for field in count_up_fields:   #removing the non numbered field-keys fo later numbering
    wgn_defaults.pop(field)
    for numbering in range (1,13):
        wgn_defaults[field + str(numbering)] = 0

"""
# here we commit to table the parameters for the basin to a row in the table wgn
"""
wgn = mdt.mdb_with_ops(variables.ProjMDB)
wgn.clear_table("wgn")
wgn.clear_table("SubWgn")

for subbasin in subbasins:    # getting field values from from watershed table
    wgn_defaults["OID"] = subbasin.split(",")[0]
    SubWgn_defaults["ObjectID"] = int(subbasin.split(",")[0])

    wgn_defaults["SUBBASIN"] = subbasin.split(",")[3]
    SubWgn_defaults["Subbasin"] = int(subbasin.split(",")[3])

    current_lat = float(subbasin.split(",")[11])
    current_lon = float(subbasin.split(",")[12])
    current_elev = float(subbasin.split(",")[13])/111
    
    distances_dict = {}
    distances_only_list = []
    
    for user_gen in WGEN_user:
        # Calculate distances from all stations to the current station using the wgen_user table
        # Here we store the distance in a list and dictionary as key for station records. Later, we can calculate minimum distance from list and get station records from dictionary.
        # WARNING: The calculation is based on decimal degrees and not metres but also depends on what is in the Lat and Lon fields. You need to make sure it is consistent.
        try:
            gen_station_lat = float(user_gen.split(",")[2])
            gen_station_lon = float(user_gen.split(",")[3])
            gen_st_elev = float(user_gen.split(",")[4])/111
        except:
            print "Error Reading from WGEN_user table: Check and try again"
            sys.exit()

        total_distance = get_distance(gen_station_lat, gen_station_lon, gen_st_elev, current_lat, current_lon, current_elev, transform_epsg)
        #if int(subbasin.split(",")[3]) == 10:
        #    print str(total_distance) + " --> " + (user_gen.split(",")[1])
        if total_distance in distances_only_list:
            continue
        else:
            distances_only_list.append(total_distance)
            distances_dict[str(total_distance)] = user_gen


    # Now, we get the station in WGEN_user, for the current subbasin.
    station = distances_dict[str(min(distances_only_list))].split(",")[1]

    SubWgn_defaults["Station"] = station
    SubWgn_defaults["MinDist"] = float(min(distances_only_list))
    SubWgn_defaults["MinRec"] = int(float(distances_dict[str(min(distances_only_list))].split(",")[0]))
    SubWgn_defaults["OrderID"] = None
    SubWgn_defaults["WGN_Dbase"] = "WGEN_user"

    wgn.insert_row("SubWgn", SubWgn_defaults, True)

    wgn_defaults["STATION"] = distances_dict[str(min(distances_only_list))].split(",")[1]
    wgn_defaults["WLATITUDE"] = distances_dict[str(min(distances_only_list))].split(",")[2]
    wgn_defaults["WLONGITUDE"] = distances_dict[str(min(distances_only_list))].split(",")[3]
    wgn_defaults["WELEV"] = distances_dict[str(min(distances_only_list))].split(",")[4]
    wgn_defaults["RAIN_YRS"] = distances_dict[str(min(distances_only_list))].split(",")[5]
    wgn_defaults["TMPMX1"] = distances_dict[str(min(distances_only_list))].split(",")[6]
    wgn_defaults["TMPMX2"] = distances_dict[str(min(distances_only_list))].split(",")[7]
    wgn_defaults["TMPMX3"] = distances_dict[str(min(distances_only_list))].split(",")[8]
    wgn_defaults["TMPMX4"] = distances_dict[str(min(distances_only_list))].split(",")[9]
    wgn_defaults["TMPMX5"] = distances_dict[str(min(distances_only_list))].split(",")[10]
    wgn_defaults["TMPMX6"] = distances_dict[str(min(distances_only_list))].split(",")[11]
    wgn_defaults["TMPMX7"] = distances_dict[str(min(distances_only_list))].split(",")[12]
    wgn_defaults["TMPMX8"] = distances_dict[str(min(distances_only_list))].split(",")[13]
    wgn_defaults["TMPMX9"] = distances_dict[str(min(distances_only_list))].split(",")[14]
    wgn_defaults["TMPMX10"] = distances_dict[str(min(distances_only_list))].split(",")[15]
    wgn_defaults["TMPMX11"] = distances_dict[str(min(distances_only_list))].split(",")[16]
    wgn_defaults["TMPMX12"] = distances_dict[str(min(distances_only_list))].split(",")[17]
    wgn_defaults["TMPMN1"] = distances_dict[str(min(distances_only_list))].split(",")[18]
    wgn_defaults["TMPMN2"] = distances_dict[str(min(distances_only_list))].split(",")[19]
    wgn_defaults["TMPMN3"] = distances_dict[str(min(distances_only_list))].split(",")[20]
    wgn_defaults["TMPMN4"] = distances_dict[str(min(distances_only_list))].split(",")[21]
    wgn_defaults["TMPMN5"] = distances_dict[str(min(distances_only_list))].split(",")[22]
    wgn_defaults["TMPMN6"] = distances_dict[str(min(distances_only_list))].split(",")[23]
    wgn_defaults["TMPMN7"] = distances_dict[str(min(distances_only_list))].split(",")[24]
    wgn_defaults["TMPMN8"] = distances_dict[str(min(distances_only_list))].split(",")[25]
    wgn_defaults["TMPMN9"] = distances_dict[str(min(distances_only_list))].split(",")[26]
    wgn_defaults["TMPMN10"] = distances_dict[str(min(distances_only_list))].split(",")[27]
    wgn_defaults["TMPMN11"] = distances_dict[str(min(distances_only_list))].split(",")[28]
    wgn_defaults["TMPMN12"] = distances_dict[str(min(distances_only_list))].split(",")[29]
    wgn_defaults["TMPSTDMX1"] = distances_dict[str(min(distances_only_list))].split(",")[30]
    wgn_defaults["TMPSTDMX2"] = distances_dict[str(min(distances_only_list))].split(",")[31]
    wgn_defaults["TMPSTDMX3"] = distances_dict[str(min(distances_only_list))].split(",")[32]
    wgn_defaults["TMPSTDMX4"] = distances_dict[str(min(distances_only_list))].split(",")[33]
    wgn_defaults["TMPSTDMX5"] = distances_dict[str(min(distances_only_list))].split(",")[34]
    wgn_defaults["TMPSTDMX6"] = distances_dict[str(min(distances_only_list))].split(",")[35]
    wgn_defaults["TMPSTDMX7"] = distances_dict[str(min(distances_only_list))].split(",")[36]
    wgn_defaults["TMPSTDMX8"] = distances_dict[str(min(distances_only_list))].split(",")[37]
    wgn_defaults["TMPSTDMX9"] = distances_dict[str(min(distances_only_list))].split(",")[38]
    wgn_defaults["TMPSTDMX10"] = distances_dict[str(min(distances_only_list))].split(",")[39]
    wgn_defaults["TMPSTDMX11"] = distances_dict[str(min(distances_only_list))].split(",")[40]
    wgn_defaults["TMPSTDMX12"] = distances_dict[str(min(distances_only_list))].split(",")[41]
    wgn_defaults["TMPSTDMN1"] = distances_dict[str(min(distances_only_list))].split(",")[42]
    wgn_defaults["TMPSTDMN2"] = distances_dict[str(min(distances_only_list))].split(",")[43]
    wgn_defaults["TMPSTDMN3"] = distances_dict[str(min(distances_only_list))].split(",")[44]
    wgn_defaults["TMPSTDMN4"] = distances_dict[str(min(distances_only_list))].split(",")[45]
    wgn_defaults["TMPSTDMN5"] = distances_dict[str(min(distances_only_list))].split(",")[46]
    wgn_defaults["TMPSTDMN6"] = distances_dict[str(min(distances_only_list))].split(",")[47]
    wgn_defaults["TMPSTDMN7"] = distances_dict[str(min(distances_only_list))].split(",")[48]
    wgn_defaults["TMPSTDMN8"] = distances_dict[str(min(distances_only_list))].split(",")[49]
    wgn_defaults["TMPSTDMN9"] = distances_dict[str(min(distances_only_list))].split(",")[50]
    wgn_defaults["TMPSTDMN10"] = distances_dict[str(min(distances_only_list))].split(",")[51]
    wgn_defaults["TMPSTDMN11"] = distances_dict[str(min(distances_only_list))].split(",")[52]
    wgn_defaults["TMPSTDMN12"] = distances_dict[str(min(distances_only_list))].split(",")[53]
    wgn_defaults["PCPMM1"] = distances_dict[str(min(distances_only_list))].split(",")[54]
    wgn_defaults["PCPMM2"] = distances_dict[str(min(distances_only_list))].split(",")[55]
    wgn_defaults["PCPMM3"] = distances_dict[str(min(distances_only_list))].split(",")[56]
    wgn_defaults["PCPMM4"] = distances_dict[str(min(distances_only_list))].split(",")[57]
    wgn_defaults["PCPMM5"] = distances_dict[str(min(distances_only_list))].split(",")[58]
    wgn_defaults["PCPMM6"] = distances_dict[str(min(distances_only_list))].split(",")[59]
    wgn_defaults["PCPMM7"] = distances_dict[str(min(distances_only_list))].split(",")[60]
    wgn_defaults["PCPMM8"] = distances_dict[str(min(distances_only_list))].split(",")[61]
    wgn_defaults["PCPMM9"] = distances_dict[str(min(distances_only_list))].split(",")[62]
    wgn_defaults["PCPMM10"] = distances_dict[str(min(distances_only_list))].split(",")[63]
    wgn_defaults["PCPMM11"] = distances_dict[str(min(distances_only_list))].split(",")[64]
    wgn_defaults["PCPMM12"] = distances_dict[str(min(distances_only_list))].split(",")[65]
    wgn_defaults["PCPSTD1"] = distances_dict[str(min(distances_only_list))].split(",")[66]
    wgn_defaults["PCPSTD2"] = distances_dict[str(min(distances_only_list))].split(",")[67]
    wgn_defaults["PCPSTD3"] = distances_dict[str(min(distances_only_list))].split(",")[68]
    wgn_defaults["PCPSTD4"] = distances_dict[str(min(distances_only_list))].split(",")[69]
    wgn_defaults["PCPSTD5"] = distances_dict[str(min(distances_only_list))].split(",")[70]
    wgn_defaults["PCPSTD6"] = distances_dict[str(min(distances_only_list))].split(",")[71]
    wgn_defaults["PCPSTD7"] = distances_dict[str(min(distances_only_list))].split(",")[72]
    wgn_defaults["PCPSTD8"] = distances_dict[str(min(distances_only_list))].split(",")[73]
    wgn_defaults["PCPSTD9"] = distances_dict[str(min(distances_only_list))].split(",")[74]
    wgn_defaults["PCPSTD10"] = distances_dict[str(min(distances_only_list))].split(",")[75]
    wgn_defaults["PCPSTD11"] = distances_dict[str(min(distances_only_list))].split(",")[76]
    wgn_defaults["PCPSTD12"] = distances_dict[str(min(distances_only_list))].split(",")[77]
    wgn_defaults["PCPSKW1"] = distances_dict[str(min(distances_only_list))].split(",")[78]
    wgn_defaults["PCPSKW2"] = distances_dict[str(min(distances_only_list))].split(",")[79]
    wgn_defaults["PCPSKW3"] = distances_dict[str(min(distances_only_list))].split(",")[80]
    wgn_defaults["PCPSKW4"] = distances_dict[str(min(distances_only_list))].split(",")[81]
    wgn_defaults["PCPSKW5"] = distances_dict[str(min(distances_only_list))].split(",")[82]
    wgn_defaults["PCPSKW6"] = distances_dict[str(min(distances_only_list))].split(",")[83]
    wgn_defaults["PCPSKW7"] = distances_dict[str(min(distances_only_list))].split(",")[84]
    wgn_defaults["PCPSKW8"] = distances_dict[str(min(distances_only_list))].split(",")[85]
    wgn_defaults["PCPSKW9"] = distances_dict[str(min(distances_only_list))].split(",")[86]
    wgn_defaults["PCPSKW10"] = distances_dict[str(min(distances_only_list))].split(",")[87]
    wgn_defaults["PCPSKW11"] = distances_dict[str(min(distances_only_list))].split(",")[88]
    wgn_defaults["PCPSKW12"] = distances_dict[str(min(distances_only_list))].split(",")[89]
    wgn_defaults["PR_W11"] = distances_dict[str(min(distances_only_list))].split(",")[90]
    wgn_defaults["PR_W12"] = distances_dict[str(min(distances_only_list))].split(",")[91]
    wgn_defaults["PR_W13"] = distances_dict[str(min(distances_only_list))].split(",")[92]
    wgn_defaults["PR_W14"] = distances_dict[str(min(distances_only_list))].split(",")[93]
    wgn_defaults["PR_W15"] = distances_dict[str(min(distances_only_list))].split(",")[94]
    wgn_defaults["PR_W16"] = distances_dict[str(min(distances_only_list))].split(",")[95]
    wgn_defaults["PR_W17"] = distances_dict[str(min(distances_only_list))].split(",")[96]
    wgn_defaults["PR_W18"] = distances_dict[str(min(distances_only_list))].split(",")[97]
    wgn_defaults["PR_W19"] = distances_dict[str(min(distances_only_list))].split(",")[98]
    wgn_defaults["PR_W110"] = distances_dict[str(min(distances_only_list))].split(",")[99]
    wgn_defaults["PR_W111"] = distances_dict[str(min(distances_only_list))].split(",")[100]
    wgn_defaults["PR_W112"] = distances_dict[str(min(distances_only_list))].split(",")[101]
    wgn_defaults["PR_W21"] = distances_dict[str(min(distances_only_list))].split(",")[102]
    wgn_defaults["PR_W22"] = distances_dict[str(min(distances_only_list))].split(",")[103]
    wgn_defaults["PR_W23"] = distances_dict[str(min(distances_only_list))].split(",")[104]
    wgn_defaults["PR_W24"] = distances_dict[str(min(distances_only_list))].split(",")[105]
    wgn_defaults["PR_W25"] = distances_dict[str(min(distances_only_list))].split(",")[106]
    wgn_defaults["PR_W26"] = distances_dict[str(min(distances_only_list))].split(",")[107]
    wgn_defaults["PR_W27"] = distances_dict[str(min(distances_only_list))].split(",")[108]
    wgn_defaults["PR_W28"] = distances_dict[str(min(distances_only_list))].split(",")[109]
    wgn_defaults["PR_W29"] = distances_dict[str(min(distances_only_list))].split(",")[110]
    wgn_defaults["PR_W210"] = distances_dict[str(min(distances_only_list))].split(",")[111]
    wgn_defaults["PR_W211"] = distances_dict[str(min(distances_only_list))].split(",")[112]
    wgn_defaults["PR_W212"] = distances_dict[str(min(distances_only_list))].split(",")[113]
    wgn_defaults["PCPD1"] = distances_dict[str(min(distances_only_list))].split(",")[114]
    wgn_defaults["PCPD2"] = distances_dict[str(min(distances_only_list))].split(",")[115]
    wgn_defaults["PCPD3"] = distances_dict[str(min(distances_only_list))].split(",")[116]
    wgn_defaults["PCPD4"] = distances_dict[str(min(distances_only_list))].split(",")[117]
    wgn_defaults["PCPD5"] = distances_dict[str(min(distances_only_list))].split(",")[118]
    wgn_defaults["PCPD6"] = distances_dict[str(min(distances_only_list))].split(",")[119]
    wgn_defaults["PCPD7"] = distances_dict[str(min(distances_only_list))].split(",")[120]
    wgn_defaults["PCPD8"] = distances_dict[str(min(distances_only_list))].split(",")[121]
    wgn_defaults["PCPD9"] = distances_dict[str(min(distances_only_list))].split(",")[122]
    wgn_defaults["PCPD10"] = distances_dict[str(min(distances_only_list))].split(",")[123]
    wgn_defaults["PCPD11"] = distances_dict[str(min(distances_only_list))].split(",")[124]
    wgn_defaults["PCPD12"] = distances_dict[str(min(distances_only_list))].split(",")[125]
    wgn_defaults["RAINHHMX1"] = distances_dict[str(min(distances_only_list))].split(",")[126]
    wgn_defaults["RAINHHMX2"] = distances_dict[str(min(distances_only_list))].split(",")[127]
    wgn_defaults["RAINHHMX3"] = distances_dict[str(min(distances_only_list))].split(",")[128]
    wgn_defaults["RAINHHMX4"] = distances_dict[str(min(distances_only_list))].split(",")[129]
    wgn_defaults["RAINHHMX5"] = distances_dict[str(min(distances_only_list))].split(",")[130]
    wgn_defaults["RAINHHMX6"] = distances_dict[str(min(distances_only_list))].split(",")[131]
    wgn_defaults["RAINHHMX7"] = distances_dict[str(min(distances_only_list))].split(",")[132]
    wgn_defaults["RAINHHMX8"] = distances_dict[str(min(distances_only_list))].split(",")[133]
    wgn_defaults["RAINHHMX9"] = distances_dict[str(min(distances_only_list))].split(",")[134]
    wgn_defaults["RAINHHMX10"] = distances_dict[str(min(distances_only_list))].split(",")[135]
    wgn_defaults["RAINHHMX11"] = distances_dict[str(min(distances_only_list))].split(",")[136]
    wgn_defaults["RAINHHMX12"] = distances_dict[str(min(distances_only_list))].split(",")[137]
    wgn_defaults["SOLARAV1"] = distances_dict[str(min(distances_only_list))].split(",")[138]
    wgn_defaults["SOLARAV2"] = distances_dict[str(min(distances_only_list))].split(",")[139]
    wgn_defaults["SOLARAV3"] = distances_dict[str(min(distances_only_list))].split(",")[140]
    wgn_defaults["SOLARAV4"] = distances_dict[str(min(distances_only_list))].split(",")[141]
    wgn_defaults["SOLARAV5"] = distances_dict[str(min(distances_only_list))].split(",")[142]
    wgn_defaults["SOLARAV6"] = distances_dict[str(min(distances_only_list))].split(",")[143]
    wgn_defaults["SOLARAV7"] = distances_dict[str(min(distances_only_list))].split(",")[144]
    wgn_defaults["SOLARAV8"] = distances_dict[str(min(distances_only_list))].split(",")[145]
    wgn_defaults["SOLARAV9"] = distances_dict[str(min(distances_only_list))].split(",")[146]
    wgn_defaults["SOLARAV10"] = distances_dict[str(min(distances_only_list))].split(",")[147]
    wgn_defaults["SOLARAV11"] = distances_dict[str(min(distances_only_list))].split(",")[148]
    wgn_defaults["SOLARAV12"] = distances_dict[str(min(distances_only_list))].split(",")[149]
    wgn_defaults["DEWPT1"] = distances_dict[str(min(distances_only_list))].split(",")[150]
    wgn_defaults["DEWPT2"] = distances_dict[str(min(distances_only_list))].split(",")[151]
    wgn_defaults["DEWPT3"] = distances_dict[str(min(distances_only_list))].split(",")[152]
    wgn_defaults["DEWPT4"] = distances_dict[str(min(distances_only_list))].split(",")[153]
    wgn_defaults["DEWPT5"] = distances_dict[str(min(distances_only_list))].split(",")[154]
    wgn_defaults["DEWPT6"] = distances_dict[str(min(distances_only_list))].split(",")[155]
    wgn_defaults["DEWPT7"] = distances_dict[str(min(distances_only_list))].split(",")[156]
    wgn_defaults["DEWPT8"] = distances_dict[str(min(distances_only_list))].split(",")[157]
    wgn_defaults["DEWPT9"] = distances_dict[str(min(distances_only_list))].split(",")[158]
    wgn_defaults["DEWPT10"] = distances_dict[str(min(distances_only_list))].split(",")[159]
    wgn_defaults["DEWPT11"] = distances_dict[str(min(distances_only_list))].split(",")[160]
    wgn_defaults["DEWPT12"] = distances_dict[str(min(distances_only_list))].split(",")[161]
    wgn_defaults["WNDAV1"] = distances_dict[str(min(distances_only_list))].split(",")[162]
    wgn_defaults["WNDAV2"] = distances_dict[str(min(distances_only_list))].split(",")[163]
    wgn_defaults["WNDAV3"] = distances_dict[str(min(distances_only_list))].split(",")[164]
    wgn_defaults["WNDAV4"] = distances_dict[str(min(distances_only_list))].split(",")[165]
    wgn_defaults["WNDAV5"] = distances_dict[str(min(distances_only_list))].split(",")[166]
    wgn_defaults["WNDAV6"] = distances_dict[str(min(distances_only_list))].split(",")[167]
    wgn_defaults["WNDAV7"] = distances_dict[str(min(distances_only_list))].split(",")[168]
    wgn_defaults["WNDAV8"] = distances_dict[str(min(distances_only_list))].split(",")[169]
    wgn_defaults["WNDAV9"] = distances_dict[str(min(distances_only_list))].split(",")[170]
    wgn_defaults["WNDAV10"] = distances_dict[str(min(distances_only_list))].split(",")[171]
    wgn_defaults["WNDAV11"] = distances_dict[str(min(distances_only_list))].split(",")[172]
    wgn_defaults["WNDAV12"] = distances_dict[str(min(distances_only_list))].split(",")[173]

    try:
        wgn_defaults = cj.format_data_type(wgn_defaults, wgnrgn)
        wgn.insert_row("wgn", wgn_defaults, True)
    except:
        list_to_pop = ["PR_W11", "PR_W12", "PR_W13", "PR_W14", "PR_W15", "PR_W16", "PR_W17", "PR_W18", "PR_W19", "PR_W110", "PR_W111", "PR_W112", "PR_W21", "PR_W22", "PR_W23", "PR_W24", "PR_W25", "PR_W26", "PR_W27", "PR_W28", "PR_W29", "PR_W210", "PR_W211", "PR_W212"]
        for field in list_to_pop:
            wgn_defaults.pop(field)

        wgn_defaults["PR_W1_1"] = distances_dict[str(min(distances_only_list))].split(",")[90]
        wgn_defaults["PR_W1_2"] = distances_dict[str(min(distances_only_list))].split(",")[91]
        wgn_defaults["PR_W1_3"] = distances_dict[str(min(distances_only_list))].split(",")[92]
        wgn_defaults["PR_W1_4"] = distances_dict[str(min(distances_only_list))].split(",")[93]
        wgn_defaults["PR_W1_5"] = distances_dict[str(min(distances_only_list))].split(",")[94]
        wgn_defaults["PR_W1_6"] = distances_dict[str(min(distances_only_list))].split(",")[95]
        wgn_defaults["PR_W1_7"] = distances_dict[str(min(distances_only_list))].split(",")[96]
        wgn_defaults["PR_W1_8"] = distances_dict[str(min(distances_only_list))].split(",")[97]
        wgn_defaults["PR_W1_9"] = distances_dict[str(min(distances_only_list))].split(",")[98]
        wgn_defaults["PR_W1_10"] = distances_dict[str(min(distances_only_list))].split(",")[99]
        wgn_defaults["PR_W1_11"] = distances_dict[str(min(distances_only_list))].split(",")[100]
        wgn_defaults["PR_W1_12"] = distances_dict[str(min(distances_only_list))].split(",")[101]
        wgn_defaults["PR_W2_1"] = distances_dict[str(min(distances_only_list))].split(",")[102]
        wgn_defaults["PR_W2_2"] = distances_dict[str(min(distances_only_list))].split(",")[103]
        wgn_defaults["PR_W2_3"] = distances_dict[str(min(distances_only_list))].split(",")[104]
        wgn_defaults["PR_W2_4"] = distances_dict[str(min(distances_only_list))].split(",")[105]
        wgn_defaults["PR_W2_5"] = distances_dict[str(min(distances_only_list))].split(",")[106]
        wgn_defaults["PR_W2_6"] = distances_dict[str(min(distances_only_list))].split(",")[107]
        wgn_defaults["PR_W2_7"] = distances_dict[str(min(distances_only_list))].split(",")[108]
        wgn_defaults["PR_W2_8"] = distances_dict[str(min(distances_only_list))].split(",")[109]
        wgn_defaults["PR_W2_9"] = distances_dict[str(min(distances_only_list))].split(",")[110]
        wgn_defaults["PR_W2_10"] = distances_dict[str(min(distances_only_list))].split(",")[111]
        wgn_defaults["PR_W2_11"] = distances_dict[str(min(distances_only_list))].split(",")[112]
        wgn_defaults["PR_W2_12"] = distances_dict[str(min(distances_only_list))].split(",")[113]

        wgn_defaults = cj.format_data_type(wgn_defaults, wgnrgn)
        wgn.insert_row("wgn", wgn_defaults, True)

wgn.disconnect()
