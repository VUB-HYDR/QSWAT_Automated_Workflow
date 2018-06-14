#import sys, os, zipfile
#import cj_function_lib as cj
#import mdbtools as mdt
#path = os.path.dirname(__file__)
#root = path.replace("mdbtoascii", "")
#sys.path.append(root)
#
#import settings
#
#print "____________________________________________________________________________\nPreparing Project...\n"
#
#project_name = settings.Project_Name
#
#proj4, is_proj = cj.get_proj4_from(root + "/" + project_name + "/Source/crop/" + settings.Land_Use)
#
#print proj4
#print is_proj

import cj_function_lib as cj

number = cj.trailing_zeros(5, "0.000001", 2)

print number

filec = cj.read_from("WGEN_user.csv")
for line in filec:
    for part in line.split(","):
        text = cj._removeNonAscii(part)
        #for i in range (10000):
            #cj.update_status(str(i))
        print text