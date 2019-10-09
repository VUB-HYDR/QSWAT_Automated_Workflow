namelist_string = '''"""------------------QSWAT Workflow v1.5.8 Settings File---------------"""

# Project Identification
Project_Name     = "{NAME}"
Model_2_namelist = False        # True = get settings from existing model 
                                # False = get model from current settings

"""---------------------------   File Names  --------------------------"""
# Raster files (Should be projected with the same projection)
Topography         = "{DEM}"
Soils              = "{SOIL}"
Land_Use           = "{LANDUSE}"


# LookUp Files
soil_lookup        = "{SOIL_LOOKUP}"
landuse_lookup     = "{LANDUSE_LOOKUP}"

# Database table files
Usersoil           = "{USERSOIL}"
WGEN_user          = "{WGEN}"

# Shape Files
Outlet             = "{OUTLET}" # it should have same format as in the example

# Weather stationinformation files
Precipitation      = "pcp.txt"
Temperature        = "tmp.txt"
Rel_Humidity       = "hmd.txt"
Solar_Radiation    = "slr.txt"
Wind               = "wnd.txt"


"""---------------------------  Project Options  ----------------------"""
# Watershed Deliniation (1 = Cells)
WS_thresholds_type    = {WS_THRES_TYPE}            
WS_threshold          = {WS_THRES_VAL}
OUT_Snap_threshold    = {OUT_SNAP}                # metres 
Burn_in_shape         = "{BURN_IN_SHAPE}"                 # leave as "" if none


#  -------------------  HRU Definition  ------------------
Slope_classes         = "{SLOPE_CLASSES}"

# HRU creation method   (1 = Dominant landuse, soil, slope , 2 = Dominant HRU,
#                        3 = Filter by Area,                 4 = Target Number of HRUs,
#                        5 = Filter by landuse, soil, slope)

HRU_creation_method   = {HRU_METHOD}

# Thresholds           (1 = Total Area , 2 = Percent)
HRU_thresholds_type   = {HRU_THRES_TYPE}

HRU_thres_LandUse     = {HRU_THRES_LU}             # Only used if HRU_creation_method 5 is selected
HRU_thres_Soil        = {HRU_THRES_SOIL}             #        can be set to "" if 5 is not selected
HRU_thres_Slope       = {HRU_THRES_SLOPE}

Target_Value          = {HRU_TARGET}           # used if HRU_creation_method 3 and 4 are selected


# Routing and ET and infiltration
ET_method             = {ET_METHOD}           # 1 = Priestley-Taylor, 2 = Penman-Monteith,   3 = Hargreaves,        (4 = Observed - Not supported Currently)
Routing_method        = {ROUTING_METHOD}           # 1 = Muskingum,        2 = Variable Storage
Routing_timestep      = {ROUTING_TS}           # 1 = Daily,            2 = Hourly
Rainfall_timestep     = {RAINFALL_TS}           # 1 = Daily,            2 = Sub-hourly timestep (works with Green & Ampt infiltration)
Run_off_method        = {RUNOFF_METHOD}           # 1 = SCS Curve Number, 2 = Green & Ampt


# model run settings
Model_Run_period      = "{MODEL_RUN_PERIOD}"# e.g. "1975 - 1980". period to run the simulation from file.cio,
                                     # leave as "" to run whole period where weather data is available
Warm_up_period        = {WARM_UP}            # the number of years for running the model without printing output
timestep              = 0            # timestep for printing results: 0 = monthly, 1 = daily 3 = yearly

cal_file              = "{CAL_FILE}"           # a model.in file (format of swatcup) with parameters for the calibrated model
                                     # leave as "" if there is no file to be used.
calibrate              = False       # set to "True" to perform calibration, "False" to skip calibration
make_figures           = False        # set to "True" to create maps, "False" to skip map creation

# Log progress or not? If yes, you will not see updates
log                   = False        # True or False
"""---------------------------  Settings End  -----------------------"""
'''
