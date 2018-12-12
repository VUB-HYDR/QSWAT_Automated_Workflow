import init_file as variables
import cj_function_lib as cj
from datetime import datetime

from sys import exit


reach_table = cj.extract_table_from_mdb(variables.ProjMDB, "Reach", variables.path + "\\reach.tmp~")

fig_string = ""

class reach:
    def __init__(self, reach_number):
        self.number = reach_number
        self.order_number = None
        self.connects_to_reach = None
        self.receives_from = None   # a list from which the reach receives

reaches = []
number_of_subbasins = len(reach_table)
reach_dictionary = {}
sinks = []
sink_receive_info = {}

# Here we create a list of all reaches in the watershed
for counter in range (1, number_of_subbasins + 1):
    reaches.append(int(counter))

#here we obtain sinks (the reaches that take frome more than one reaches)
end_reach = None  # for future use
tmp_list = []
for to_node in reach_table:
    if int(to_node.split(",")[5]) in tmp_list:
        sinks.append(int(to_node.split(",")[5]))
    tmp_list.append(int(to_node.split(",")[5]))
    if int(to_node.split(",")[5]) == 0:
        end_reach = int((to_node.split(",")[4]))


for member in reaches:
    reach_dictionary[str(member)] = reach(member)

# here we get the reaches from which each sink receives
for sink in sinks:
    tmp = []
    for line in reach_table:
        if int(line.split(",")[5]) == sink:
            tmp.append(int(line.split(",")[4]))
            tmp.sort()
            reach_dictionary[str(sink)].receives_from = tmp

#for sink in sinks:
#    print "\n" + str(sink)
#    print reach_dictionary[str(sink)].receives_from

# here we start assigning the order numbers

count = number_of_subbasins
for item in reaches:
    if not (item in sinks):
        count += 1
        reach_dictionary[str(item)].order_number = count

max_events = count + (len(sinks) * 3)
#print max_events




# now we assign the order numbers for the reaches acting as sinks too.
reach_dictionary[str(end_reach)].order_number = int(max_events)

current_rank = int(max_events)
current_reach = end_reach

later_reaches_order = []
#kept_route = None
#

detour_reaches = []
last_time_reach = None #to prevent redundancy in the loop

#ranking end_reach
reach_dictionary[str(current_reach)].order_number = int(current_rank)

#ranking the other sinks
teyy = 0
while True:
    # if the to-node is not a sink, do not add to come back to it later in the loop
    #print reach_dictionary[str(current_reach)].receives_from
    #print sinks
    if reach_dictionary[str(current_reach)].receives_from[0] in sinks:
        #print "\tadding " + str(reach_dictionary[str(current_reach)].receives_from[0])
        detour_reaches.append(reach_dictionary[str(current_reach)].receives_from[0])
    else:
        pass

    if reach_dictionary[str(current_reach)].receives_from[1] in sinks:
        #print "\tmoving to " + str(reach_dictionary[str(current_reach)].receives_from[1])
        current_reach = reach_dictionary[str(current_reach)].receives_from[1]
        current_rank -= 3
        #print current_rank
        reach_dictionary[str(current_reach)].order_number = int(current_rank)
        later_reaches_order.append(reach_dictionary[str(current_reach)].number)
    elif not reach_dictionary[str(current_reach)].receives_from[1] in sinks:
        if detour_reaches == []:
            break
        current_reach = detour_reaches[0]
        #print detour_reaches
        #print "--------------------------------\n\tskipping to :" + str(current_reach)
        current_rank -= 3
        detour_reaches.remove(current_reach)
        reach_dictionary[str(current_reach)].order_number = int(current_rank)
        later_reaches_order.append(reach_dictionary[str(current_reach)].number)
        #print current_rank


# create the string for first part
for subb_nr in range(1, len(reach_table) + 1):
    fig_string += "subbasin       1" + cj.trailing_spaces(6, subb_nr, 0) + cj.trailing_spaces(6, subb_nr, 0) + "                              Subbasin: " + str(subb_nr) + \
        "\n          " + cj.trailing_zeros(5, subb_nr, 0) + "0000.sub\n"
#create string for second part
first_confluence_string = ""
for route in reaches:
    if route not in sinks:
        first_confluence_string += "route          2" + cj.trailing_spaces(6, reach_dictionary[str(route)].order_number, 0) + cj.trailing_spaces(6, route, 0) + cj.trailing_spaces(6, route, 0) + \
            "\n          " + cj.trailing_zeros(5, route, 0) + "0000.rte" + cj.trailing_zeros(5, route, 0) + "0000.swq\n"
        #reach_dictionary[str(route)]

# create a dictionary of reaches in accending order

#print later_reaches_order

# we make the ending of the fig.fig string
fig_bottom = "\nsaveconc      14" + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number, 0) + "     1     0" + \
    "\n          watout.dat" + \
    "\nfinish         0\n"



# now add ON TOP of this fig bottom
second_confluence_string = ""
for later_reach in later_reaches_order:
    #print "\n" + str(later_reach)
    ##print reach_dictionary[str(later_reach)].order_number - 2
    #print reach_dictionary[str(reach_dictionary[str(later_reach)].receives_from[0])].number
    #print reach_dictionary[str(reach_dictionary[str(later_reach)].receives_from[1])].number
    ##print str(reach_dictionary[str(later_reach)].order_number - 1)
    ##print str(reach_dictionary[str(later_reach)].order_number - 2)

	
    second_confluence_string = "add            5" + cj.trailing_spaces(6, str(reach_dictionary[str(later_reach)].order_number - 2), 0) + cj.trailing_spaces(6, later_reach, 0) + cj.trailing_spaces(6, reach_dictionary[str(reach_dictionary[str(later_reach)].receives_from[0])].order_number, 0) + \
        "\nadd            5" + cj.trailing_spaces(6, str(reach_dictionary[str(later_reach)].order_number - 1), 0) + cj.trailing_spaces(6, reach_dictionary[str(later_reach)].order_number - 2, 0) + cj.trailing_spaces(6, reach_dictionary[str(reach_dictionary[str(later_reach)].receives_from[1])].order_number, 0) + \
        "\nroute          2" + cj.trailing_spaces(6, reach_dictionary[str(later_reach)].order_number, 0) + cj.trailing_spaces(6, later_reach, 0) + cj.trailing_spaces(6, str(reach_dictionary[str(later_reach)].order_number - 1), 0) + \
        "\n          " + cj.trailing_zeros(5, later_reach, 0) + "0000.rte" + cj.trailing_zeros(5, later_reach, 0) + "0000.swq" + "\n" + second_confluence_string

# for the last confluence
last_confluence_string = "add            5" + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number - 2, 0) + cj.trailing_spaces(6, end_reach, 0) + cj.trailing_spaces(6, reach_dictionary[str(reach_dictionary[str(end_reach)].receives_from[0])].order_number, 0) + \
    "\nadd            5" + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number - 1, 0) + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number - 2, 0) + cj.trailing_spaces(6, reach_dictionary[str(reach_dictionary[str(end_reach)].receives_from[1])].order_number, 0) + \
    "\nroute          2" + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number, 0) + cj.trailing_spaces(6, end_reach, 0) + cj.trailing_spaces(6, reach_dictionary[str(end_reach)].order_number - 1, 0) + \
    "\n          " + cj.trailing_zeros(5, end_reach, 0) + "0000.rte" + cj.trailing_zeros(5, end_reach, 0) + "0000.swq"


# here we get the whole string and save to file
fig_string = fig_string + first_confluence_string + second_confluence_string + last_confluence_string + fig_bottom

fileName = "fig.fig"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, fig_string)




# Here we also generate the ATM file, I do not know which fields in the BSN table contain these.

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"


ATM = "Watershed atmospheric deposition file      .atm file " + DateAndTime + " " + SWAT_Vers + \
"""



"""

for basin in reach_table:
    ATM += "\n             0.000     0.000     0.000     0.000"

ATM += "\n"
fileName = "ATMO.ATM"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, ATM)


""""subbasin       1     1     1                              Subbasin: 1
          000010000.sub
subbasin       1     2     2                              Subbasin: 2
          000020000.sub
subbasin       1     3     3                              Subbasin: 3
          000030000.sub
subbasin       1     4     4                              Subbasin: 4
          000040000.sub
subbasin       1     5     5                              Subbasin: 5
          000050000.sub
subbasin       1     6     6                              Subbasin: 6
          000060000.sub
subbasin       1     7     7                              Subbasin: 7
          000070000.sub
subbasin       1     8     8                              Subbasin: 8
          000080000.sub
subbasin       1     9     9                              Subbasin: 9
          000090000.sub
subbasin       1    10    10                              Subbasin: 10
          000100000.sub
subbasin       1    11    11                              Subbasin: 11
          000110000.sub
route          2    12     1     1
          000010000.rte000010000.swq
route          2    13     3     3
          000030000.rte000030000.swq
route          2    14     6     6
          000060000.rte000060000.swq
route          2    15     8     8
          000080000.rte000080000.swq
route          2    16     9     9
          000090000.rte000090000.swq
route          2    17    11    11
          000110000.rte000110000.swq
add            5    18     5    13
add            5    19    18    15
route          2    20     5    19
          000050000.rte000050000.swq
add            5    21     7    20
add            5    22    21    17
route          2    23     7    22
          000070000.rte000070000.swq
add            5    24    10    14
add            5    25    24    23
route          2    26    10    25
          000100000.rte000100000.swq
add            5    27     2    16
add            5    28    27    26
route          2    29     2    28
          000020000.rte000020000.swq
add            5    30     4    12
add            5    31    30    29
route          2    32     4    31
          000040000.rte000040000.swq
saveconc      14    32     1     0
          watout.dat
finish         0
"""