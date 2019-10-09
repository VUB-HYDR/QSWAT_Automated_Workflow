"""
Author      : Celray James CHAWANDA (celray.chawanda@outlook.com)
Institution : Vrije Universiteit Brussel (VUB)

This is the main script for launching the SWAT model setup process
"""
import sys, os, shutil, shlex

home_dir = os.path.dirname(os.path.realpath(__file__))
python = "C:\\Python27\\python.exe"
current_dir  = os.getcwd()
sys.path.append(current_dir)
from namelist import *
from datetime import datetime
import subprocess

def run_and_log(command, log_, save_dir, mode, args_):
    if log_:
        print("\t> logging is set to 'True' in namelist; output is being saved to " + save_dir)
        if mode == "w":
            os.system(command + " " +args_ + ">" + save_dir + '2>&1')
        elif mode == "a":
            os.system(command + " " +args_ + ">>" + save_dir + '2>&1')
    else:
        os.system(command + " " +args_)

def copy_file(original_file_path, destination):
    if os.path.isfile(destination):
        os.remove(destination)
    shutil.copy(original_file_path, destination)

time_begin = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

copy_file("namelist.py", home_dir + "/workflow_lib/namelist.py")
os.chdir(home_dir + "/workflow_lib/")

if not Model_2_namelist:
    run_and_log(python + ' "' + os.path.join(home_dir, 'workflow_lib', 'prepare_project.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "w", '"' + current_dir + '"')
    run_and_log(python + ' "' + os.path.join(home_dir, 'workflow_lib', 'main.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "a", '"' + current_dir + '"')
else:
    run_and_log(python + ' "' + os.path.join(home_dir, 'workflow_lib', 'model_2_namelist.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "a", '"' + current_dir + '"')

if not Model_2_namelist:
    if calibrate:
        run_and_log(python + ' "' + os.path.join(home_dir, 'workflow_lib', 'calibrate_model.py') + '"', False, '"' + os.path.join(home_dir, 'log.txt') + '"', "a", '"' + current_dir + '"' + ' ' + Project_Name)

    if make_figures:
        run_and_log(python + ' "' + os.path.join(home_dir, 'workflow_lib', 'figures.py') + '"', False, '"' + os.path.join(home_dir, 'log.txt') + '"', "a", os.path.join('"' + current_dir + '"', "model", Project_Name) + " sub null " + " ".join([str(i) for i in range(int(Model_Run_period.split(" ")[0].split("-")[0]), int(Model_Run_period.split(" ")[-1].split("-")[-1]) + 1 )]))

time_end = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Run Time:\n   From : " + time_begin)
print("   To   : " + time_end)

with open(current_dir + "/run_time.txt", "w") as f:
    f.write("Begin: " + time_begin + "\nEnd  : " + time_end)

raw_input("\n\npress ENTER to exit...")
