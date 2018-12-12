"""
Author      : Celray James CHAWANDA (celray.chawanda@outlook.com)
Institution : Vrije Universiteit Brussel (VUB)

This is the main script for launching the SWAT model setup process
"""
import sys, os, shutil, shlex
from namelist import *
from datetime import datetime
import subprocess

def run_and_log(command, log_, save_dir, mode):
    if log_:
        print("\t> logging is set to 'True' in namelist; output is being saved to " + save_dir)
        if mode == "w":
            os.system(command + ">" + save_dir + '2>&1')
        elif mode == "a":
            os.system(command + ">>" + save_dir + '2>&1')
    else:
        os.system(command)

def copy_file(original_file_path, destination):
    if os.path.isfile(destination):
        os.remove(destination)
    shutil.copy(original_file_path, destination)

time_begin = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
home_dir = os.getcwd()

copy_file("namelist.py", "workflow_lib/namelist.py")
os.chdir(home_dir + "/workflow_lib/")

if not Model_2_namelist:
    run_and_log('python "' + os.path.join(home_dir, 'workflow_lib', 'prepare_project.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "w")
    run_and_log('python "' + os.path.join(home_dir, 'workflow_lib', 'main.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "a")
else:
    run_and_log('python "' + os.path.join(home_dir, 'workflow_lib', 'model_2_namelist.py') + '"', log, '"' + os.path.join(home_dir, 'log.txt') + '"', "a")

time_end = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Run Time:\n   From : " + time_begin)
print("   To   : " + time_end)

with open(home_dir + "/run_time.txt", "w") as f:
    f.write("Begin: " + time_begin + "\nEnd  : " + time_end)

raw_input("\n\npress ENTER to exit...")
