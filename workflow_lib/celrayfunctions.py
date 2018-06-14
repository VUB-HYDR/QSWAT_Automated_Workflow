# -*- coding: utf-8 -*-
# This module contains functions commonly used by Celray James

# Imports
import sys, os, shutil
from glob import glob
#from termcolor import colored
import datetime


#####################                               Functions                    ##########################
def create_directory(folder_path):
    directory = os.path.dirname(folder_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
def end():
    sys.exit()

def copy_file(original_file_path, destination):
    shutil.copy(original_file_path, destination)

def rename_by_folder_structure(parent_directory, file_types):
    # file types as strings in tuple
    list_fh = list_files_in_subfolders(parent_directory,file_types)
    count = 0
    length_ = len(list_fh)
    for filename in list_fh:
        tmp_name = filename.split(parent_directory)[1].replace("\\", "_")[1:]

        file_real_name = filename.split("\\")[-1]
        file_base = filename.split(file_real_name)[0]

        os.rename(filename, file_base + tmp_name)
        count += 1
        update_progress(count, length_, 30)
def list_files_from(folder, extension):
    if folder.endswith("/"):
        list_of_files = glob(folder + "*." + extension)
    else:
        list_of_files = glob(folder + "/*." + extension)
    return list_of_files

def list_subdirectories_from(path):
    list_of_subs = glob(path + "\\*\\")
    return list_of_subs

def list_files_in_subfolders(path_, list_as_tuple):
    # list as tuple eg (".html", ".txt")
    specific_files = [os.path.join(root, name)
                 for root, dirs, files in os.walk(path_)
                 for name in files
                 if name.endswith(list_as_tuple)]
    return specific_files

def cwd():
    cwd = os.getcwd()
    return cwd

def chdir(new_path):
    os.chdir(new_path)
    print "\nNew working directory : " + new_path

def delete_file(file_path):
    os.remove(file_path)
    print "\nDeleted : " + file_path

def write_to(filename,text_to_write):
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close
    print '\nFile saved to ' + filename

def read_from(filename):
    g = open(filename, 'r')
    file_text = g.readlines()
    return file_text
    g.close

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

#def print_colour(colour,text):
#    print colored(text, colour)

def list_to_string(list_to_change,newline = True):
    string_holder = ""
    for line in list_to_change:
        if newline == True:
            string_holder = string_holder + str(line) + "\n"
        else:
            string_holder = string_holder + str(line)
    return string_holder

def create_date(day, month, year):
    date_ = datetime.datetime(int(year), int(month), int(day))
    return date_

def time_delta(unit, quantity):
    if unit == "years":
        dt = datetime.timedelta(years=quantity)
    if unit == "months":
        dt = datetime.timedelta(months=quantity)
    if unit == "days":
        dt = datetime.timedelta(days=quantity)
    if unit == "hours":
        dt = datetime.timedelta(hours=quantity)
    if unit == "minutes":
        dt = datetime.timedelta(minutes=quantity)
    if unit == "seconds":
        dt = datetime.timedelta(seconds=quantity)
    return dt

def update_status(message):
    sys.stdout.write("\r" + message)
    sys.stdout.flush()

def update_progress(count,end_val, bar_length):   #bar_length=20
    percent = float(count) / end_val
    hashes = "#" * int(round(percent * bar_length))
    spaces = '_' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent Complete: [{0}] {1}%".format(hashes + spaces, float(round(percent * 100, 2)) if str(float(round(percent * 100, 2)))[-2:-1] != "." else str(float(round(percent * 100, 2))) + "0"))
    sys.stdout.flush()
print "___________________________________________________________________________________________"
print("\nModules have loaded!!")

###########################################################################################################
