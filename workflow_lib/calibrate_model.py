'''


'''

import sys, os
from datetime import datetime, timedelta
import shutil
from glob import glob
import init_file as variables

sys.path.append(variables.root.replace("workflow_lib", "")[:-1])

def read_from(filename):
    try:
        g = open(filename, 'r')
    except:
        print("\t> error reading {0}, make sure the file exists".format(filename))
        sys.exit()
        # return
    file_text = g.readlines()
    g.close
    return file_text

def write_to(filename,text_to_write, report = True):
    if not os.path.isdir(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close
    if report:
        print('\n\t> file saved to ' + filename)

def list_files_from(folder, extension):
    if folder.endswith("/"):
        if extension ==  "*":
            list_of_files = glob(folder + "*")
        else:
            list_of_files = glob(folder + "*." + extension)
    else:
        if extension ==  "*":
            list_of_files = glob(folder + "/*")
        else:
            list_of_files = glob(folder + "/*." + extension)
    return list_of_files

def copy_file(original_file_path, destination):
    # print("\t> copied {1}\n\t\tto {0}".format(destination, original_file_path))
    if not os.path.isdir(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    shutil.copy(original_file_path, destination)

# vars

cal_files_dir = os.path.join(sys.argv[1], "Data", "calibration_data")
raw_settings_fn = os.path.join(cal_files_dir, "calibration_control.csv")
raw_settings = read_from(raw_settings_fn)
nsga_par_def_string = "Name	      Minimum	Maximum\n"
nsga_def_string = ""
observed_reach_string = "{obs_var_number}     : number of observed variables\n"
txtinout_dir = os.path.join(sys.argv[1], "model", sys.argv[2], "Scenarios", "Default", "TxtInOut")
inputs_dir = os.path.join(txtinout_dir, "NSGA2.IN")
backup_dir = os.path.join(txtinout_dir, "Backup")

# create def files
for line in raw_settings[1:]:
    line_parts = line.split(",")
    if (line_parts[0] == 'settings') or (line_parts[0] == ""):
        break
    else:
        nsga_par_def_string += "{chgtyp}__{par_name}    {min}    {max}\n".format(
            par_name = line_parts[0],
            min = float(line_parts[1]),
            max = float(line_parts[2]),
            chgtyp = line_parts[3][:-1],
        )

write_to(os.path.join(inputs_dir, "nsga2_par.def"), nsga_par_def_string)

get_data = False

for line in raw_settings:
    line_parts = line.split(",")
    if line_parts[0].startswith('definition'):
        get_data = True
    
    if get_data:
        nsga_def_string += "{0}\t{1}\t{2}\n".format(line_parts[0],line_parts[1],line_parts[2])

write_to(os.path.join(inputs_dir, "nsga2.def"), nsga_def_string)

# get observation file data
observations = {}

get_data = False
for line in raw_settings:
    line_parts = line.split(",")
    if line_parts[0].startswith('channel number'):
        get_data = True
        continue
   
    if get_data:
        if line_parts[0] == "":
            break

        current_file = "{cal_dir}/observed/{fn}".format(fn = line_parts[1], cal_dir = cal_files_dir)
        current_file_string_list = read_from(current_file)
        if not line_parts[0] in observations:
            observations[line_parts[0]] = {}
        obs_line = None
        for obs_line in current_file_string_list[1:]:
            if not "startdate" in observations[line_parts[0]]:
                observations[line_parts[0]]["startdate"] = obs_line.split(",")[0]
            if not "reach_number" in observations[line_parts[0]]:
                observations[line_parts[0]]["reach_number"] = line_parts[0]
            
            observations[line_parts[0]][obs_line.split(",")[0]] = obs_line.split(",")[1]
        
        if not "end_date" in observations[line_parts[0]]:
            observations[line_parts[0]]["end_date"] = obs_line.split(",")[0]

        
# write observation file
observed_reach_string = observed_reach_string.format(obs_var_number = len(observations))
file_cio = read_from(os.path.join(txtinout_dir, "file.cio"))

def single_spaces(string_,  remove_enter = True):
    str_ = string_
    for index in range(0, 20):
        str_ = str_.replace("  ", " ")
    if remove_enter:
        str_ = str_.replace("\n", "")
        str_ = str_.replace("\r", "")
    return str_


cio_sim_number = int(single_spaces(file_cio[7]).split(" ")[1])
cio_start_year = int(single_spaces(file_cio[8]).split(" ")[1])
cio_skip_year = int(single_spaces(file_cio[59]).split(" ")[1])


for primary_key in observations:
    start_date = datetime(
        int(observations[primary_key]['startdate'].split("/")[2]),
        int(observations[primary_key]['startdate'].split("/")[1]),
        int(observations[primary_key]['startdate'].split("/")[0]),
    )
    current_date = datetime(cio_start_year + cio_skip_year, 1, 1)
    while not "{day}/{month}/{year}".format(
            year = current_date.year if current_date.year > 9 else "0" + str(current_date.year),
            month = current_date.month if current_date.month > 9 else "0" + str(current_date.month), 
            day= current_date.day if current_date.day > 9 else "0" + str(current_date.day)
            ) in observations[primary_key]:
            current_date += timedelta(days = 1)
            continue

    end_date = datetime(
        int(cio_start_year + cio_sim_number - 1),
        int(12),
        int(31),
    )

    observed_reach_string += "\noutput_rch_{r_number}              : this is the name of the file (output_rch) and the subbasin number to be included in the objective function\n".format(
        r_number = observations[primary_key]['reach_number']
    )
    observed_reach_string += "//data_points//                       : number of data points for this variable as it follows below. First column is a sequential number from beginning of the simulation for each date (missing data: jumps to next available date), second column is variable name and date (format arbitrary), third column is variable value.\n".format(
        data_points = len(observations[primary_key]) - 3
    )
    observed_reach_string += "{start_m}/{start_d}/{start_y}|{end_m}/{end_d}/{end_y}|2   :BeginDate|EndDate|ColumnNumber  (Date Format: MM/DD/YYYY; Column Number is in output.rch file as columnNumber=0 for area and 1 for the next and so on...)\n".format(
        start_d = start_date.day if start_date.day > 9 else "0" + str(start_date.day),
        start_m = start_date.month if start_date.month > 9 else "0" + str(start_date.month),
        start_y = start_date.year if start_date.year > 9 else "0" + str(start_date.year),

        end_d = end_date.day if end_date.day > 9 else "0" + str(end_date.day),
        end_m = end_date.month if end_date.month > 9 else "0" + str(end_date.month),
        end_y = end_date.year if end_date.year > 9 else "0" + str(end_date.year),

    )
    counter = 0
    datapoints = 0
    while current_date <= end_date:
        counter += 1
        if not "{day}/{month}/{year}".format(
            year = current_date.year if current_date.year > 9 else "0" + str(current_date.year),
            month = current_date.month if current_date.month > 9 else "0" + str(current_date.month), 
            day= current_date.day if current_date.day > 9 else "0" + str(current_date.day)
            ) in observations[primary_key]:
            current_date += timedelta(days = 1)
            continue
        observed_reach_string += "{2}	{0}	{1}".format(
            "{y}-{m}-{d}".format(
                y = current_date.year if current_date.year > 9 else "0" + str(current_date.year),
                m = current_date.month if current_date.month > 9 else "0" + str(current_date.month), 
                d = current_date.day if current_date.day > 9 else "0" + str(current_date.day)
            ),
        observations[primary_key]["{day}/{month}/{year}".format(
            year = current_date.year if current_date.year > 9 else "0" + str(current_date.year),
            month = current_date.month if current_date.month > 9 else "0" + str(current_date.month), 
            day= current_date.day if current_date.day > 9 else "0" + str(current_date.day)
            )],
        counter
        )
        current_date += timedelta(days = 1)
        datapoints += 1
    observed_reach_string = observed_reach_string.replace("//data_points//", str(datapoints))
write_to(os.path.join(inputs_dir, "observed_rch.txt"), observed_reach_string)

files = list_files_from(txtinout_dir, "*")
for fn in files:
    if (os.path.basename(fn) == "NSGA2.IN") or (os.path.basename(fn) == "NSGA2.OUT") or (os.path.basename(fn) == "Backup"):
        continue
    copy_file(fn, os.path.join(backup_dir, os.path.basename(fn)))

import os, sys
sys.path.append(os.path.join("C:\SWAT", "QSWAT Workflow")) #Use this if you do not want to install library
from nsga2lib import nsga2, SWATutilities, nsga2utilities


#---- Input ----(space on directory may cause problems during execution)
SWATtxtinoutDirectory = os.path.join(os.getcwd(), txtinout_dir)
#---------------

NSGAII=nsga2.nsga2(SWATtxtinoutDirectory) 
NSGAII.CreateInitialPopulation()

#Loop through generations
TotalNumGenerations = NSGAII.ngener
i=0
while i < TotalNumGenerations:
    NSGAII.CreateChildPopulation() #Thorough selection, crossover and mutation child population created from old population
    
    nsga2utilities.decode(NSGAII.new_pop_ptr, NSGAII.vlen, NSGAII.lim_b); #Turn binary calibration parameters into normal numbers.
    #new_pop_ptr=child population. vlen=the no.of bits assigned to the each calibration parameters. lim_b=range of calibration parameters.
    
    SWATutilities.CalculateObjectiveFunctions(NSGAII.new_pop_ptr,NSGAII.Outlet_Obsdata,NSGAII.FuncOpt,NSGAII.FuncOptAvr,NSGAII.parname,i+1,NSGAII.SWATdir);
    
    NSGAII.CreateParentPopulation(i+1) # Old and New populations goes throuth Elitism, crowding distances, nondominated sorting
    #and create the old population for next generation. Report is printed during this function process.
    i += 1

print("The NSGA-II execution finished. Look at the results in NSGA2.OUT folder.");

