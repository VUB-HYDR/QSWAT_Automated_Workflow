"""------------------  QSWAT Workflow 1.5 Settings File---------------"""
# Project Identification
Project_Name 	 = "working_example"

"""---------------------------  File Names  --------------------------"""
# Raster files (Should be projected with the same projection)
Topography		 = "dem"
Soils		 	 = "soilmap"
Land_Use		 = "roblandusenew"
#Irrigation		 = ""

# LookUp Files
soil_lookup		 = "soil_lookup.csv"
landuse_lookup	 = "landuse_lookup.csv"
#
Usersoil		 = "usersoil.csv"
WGEN_user		 = "WGEN_Robit.csv"

# Shape Files
Outlet			 = "drawoutlets.shp"  # IT SHOULD HAVE FIELDS AS IN EXAMPLE

# Weather forks
Precipitation	 = "pcpRobStation.txt"
Temperature		 = "tmpRobStation.txt"
Rel_Humidity	 = "rhumRobStation.txt"
Solar_Radiation	 = "solRobStation.txt"
Wind			 = "windRobStation.txt"

"""---------------------------  Project Options  ---------------------"""
# Watershed Deliniation (1 = Cells)
WS_thresholds_type	 = 1            
WS_threshold 		 = 992
OUT_Snap_threshold	 = 300 			# metres 
Burn_in_shape        = ""           # leave as "" if none; note that the format should be as
                                            #              used for the GUI, else, it will be skipped

#  -------------  HRU Definition  -------------
Slope_classes	     = "0, 10, 50, 9999"


# HRU creation method  (1 = Dominant landuse, soil, slope , 	2 = Dominant HRU,
#						3 = Filter by Area, 	4 = Target Number of HRUs,
#						5 = Filter by landuse, soil, slope)

HRU_creation_method = 3

# Thresholds (1 = Total Area , 2 = Percent)
HRU_thresholds_type	 = 1

HRU_thres_Soil 		 = 10                # Only used if HRU_creation_method 5 is selected
HRU_thres_LandUse 	 = 12               #         can be set to "" if 5 is not selected
HRU_thres_Slope 	 = 7

Target_Value         = 10               # used if HRU_creation_method 3 and 4 are selected



# Log progress or not? If yes, you will not see updates
log                  = False # True or False

"""---------------------------  Settings End  -----------------------"""





