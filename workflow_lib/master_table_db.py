
import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt

master = mdt.mdb_with_ops(variables.ProjMDB)

master_dictionary = {}

master_dictionary["WorkDir"] = variables.ProjDir
master_dictionary["OutputGDB"] = variables.ProjMDB
master_dictionary["RasterGDB"] = ""
master_dictionary["SwatGDB"] = "{0}\QSWATRef2012.mdb".format(variables.ProjDir)
master_dictionary["WshdGrid"] = ""
master_dictionary["ClipDemGrid"] = ""
master_dictionary["SoilOption"] = "name"
master_dictionary["NumLuClasses"] = 0
master_dictionary["DoneWSDDel"] = 1
master_dictionary["DoneSoilLand"] = 1
master_dictionary["DoneWeather"] = 1
master_dictionary["DoneModelSetup"] = 1
master_dictionary["OID"] = 1
master_dictionary["MGT1_Checked"] = 1
master_dictionary["ArcSWAT_V_Create"] = ""
master_dictionary["ArcSWAT_V_Curr"] = "2012.10.19"
master_dictionary["AccessExePath"] = ""
master_dictionary["DoneModelRun"] = 1

master.clear_table("MasterProgress")
master.insert_row("MasterProgress", master_dictionary, True)
master.disconnect()
