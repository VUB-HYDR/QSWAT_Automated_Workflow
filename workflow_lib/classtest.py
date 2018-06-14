
import os
import mdbtools as mdt

pwd = os.getcwd()
print pwd
haha = mdt.mdb_with_ops("UpperBN_complete.mdb")

haha.connect()

#diction = {}
#
#diction["ID"] = 3
#
#diction["NO"] = 5
#
#diction["MSG"] = "hahaha"
#
#import sys
##sys.exit()
##haha.clear_table("test")
##haha.insert_row("test", diction, True)
#
#fields = ["SNAM","SOIL_ID"]
#
#print ",".join(fields)
#
#haha.get_values("FAO_soils",fields)
#
#print haha.columns
haha.create_table("another_test_2", "Order", "Text")
haha.add_field("another_test_2", "Additional", "FLOAT")


haha.disconnect()
