"""------------------  QSWAT Workflow 1.5 Settings File---------------"""
# Project Identification
Project_Name 	 = "blue_nile_qswat"

"""---------------------------  File Names  --------------------------"""
# Raster files (Should be projected with the same projection)
Topography		 = "blue_nile_32637_dem.tif"
Soils		 	 = "soilmap"
Land_Use		 = "global2009_lu_2P.tif"
#Irrigation		 = ""

# LookUp Files
soil_lookup		 = "soil_lookup.csv"
landuse_lookup	 = "landuse_lookup.csv"
#
Usersoil		 = "usersoil.csv"
WGEN_user		 = "WGEN_user.txt"

# Shape Files
Outlet			 = "outlet.shp"  # IT SHOULD HAVE FIELDS AS IN EXAMPLE

# Weather forks
Precipitation	 = "station_pcp.txt"
Temperature		 = "station_tmp.txt"
Rel_Humidity	 = "station_rh.txt"
Solar_Radiation	 = "station_slr.txt"
Wind			 = "station_wnd.txt"

"""---------------------------  Project Options  ---------------------"""
# Watershed Deliniation (1 = Cells)
WS_thresholds_type	 = 1            
WS_threshold 		 = 45000
OUT_Snap_threshold	 = 300 			# metres 
Burn_in_shape        = ""           # leave as "" if none; note that the format should be as
                                            #              used for the GUI, else, it will be skipped

#  -------------  HRU Definition  -------------
Slope_classes	     = "0, 7, 50, 9999"


# HRU creation method  (1 = Dominant landuse, soil, slope , 	2 = Dominant HRU,
#						3 = Filter by Area, 	4 = Target Number of HRUs,
#						5 = Filter by landuse, soil, slope)

HRU_creation_method = 5

# Thresholds (1 = Total Area , 2 = Percent)
HRU_thresholds_type	 = 2

HRU_thres_LandUse 	 = 12               # Only used if HRU_creation_method 5 is selected
HRU_thres_Soil 		 = 10               #         can be set to "" if 5 is not selected
HRU_thres_Slope 	 = 7

Target_Value         = 20               # used if HRU_creation_method 3 and 4 are selected



# Log progress or not? If yes, you will not see updates
log                  = False # True or False

"""---------------------------  Settings End  -----------------------"""





