"""
Author: Celray James CHAWANDA - VUB

                                            """

import sys, os, shutil, csv, time
import pyodbc
import csv
import datetime, calendar
from glob import glob
import stat
import subprocess
import gdal, osr

from decimal import Decimal, ROUND_HALF_UP

def get_raster_stats(raster_file):
    # open raster and choose band to find min, max
    gtif = gdal.Open(raster_file)
    srcband = gtif.GetRasterBand(1)
    # Get raster statistics
    stats = srcband.GetStatistics(True, True)
    # Print the min, max, mean, stdev based on stats index
    raster_stats = {"min": stats[0], "max": stats[1], "mean": stats[2], "std_dev": stats[3]}
    return raster_stats

def get_slsbbsn(hru_slope):
    hru_slope = float(hru_slope)
    sl_sub_bsn = None
    if hru_slope < 0.02:
        sl_sub_bsn = 121.951
    elif (hru_slope >= 0.02) and (hru_slope <  0.05):
        sl_sub_bsn = 91.463
    elif (hru_slope >= 0.05) and (hru_slope <  0.12):
        sl_sub_bsn = 60.976
    elif (hru_slope >= 0.12) and (hru_slope <  0.16):
        sl_sub_bsn = 24.390
    elif (hru_slope >= 0.16) and (hru_slope <  0.20):
        sl_sub_bsn = 18.293
    elif (hru_slope >= 0.20) and (hru_slope <  0.25):
        sl_sub_bsn = 15.244
    elif (hru_slope >= 0.25):
        sl_sub_bsn = 9.146
    else:
        sl_sub_bsn = 50.000
        
    return sl_sub_bsn

def get_extents(raster):
    src = gdal.Open(raster)
    upper_lef_x, xres, xskew, upper_left_y, yskew, yres  = src.GetGeoTransform()
    lower_right_x = upper_lef_x + (src.RasterXSize * xres)
    lower_right_y = upper_left_y + (src.RasterYSize * yres)
    return upper_lef_x, lower_right_y, lower_right_x, upper_left_y

def get_auth(raster_file):
    '''
    gives epsg and srs_id
    '''
    prj_name = None
    srs_id = None
    try:
        list_of_wkt = read_from("wkt_lookup.uesv")
        datafile = gdal.Open(raster_file, gdal.GA_ReadOnly)
        wkt_info = datafile.GetProjection()
        prj_info = osr.SpatialReference(wkt_info)
        prj_name = prj_info.GetAttrValue('PROJCS',0)
        speroid = prj_info.GetAttrValue('SPHEROID',0)
        if prj_name.startswith("UTM Zone"):
            try:
                if prj_name.split(",")[1].startswith(" N"):
                    prj_name = speroid + " / UTM Zone " + prj_name.split(" ")[2].replace(",", "") + "N"
                if prj_name.split(",")[1].startswith(" S"):
                    prj_name = speroid + " / UTM Zone " + prj_name.split(" ")[2].replace(",", "") + "S"
            except:
                pass
        for wkt in list_of_wkt:
            if prj_name is None:
                break
            if wkt.startswith("epsg_code"):
                continue
            if wkt.split(";")[1].replace(" ", "").lower().replace("\n", "") == prj_name.replace(" ", "").lower():
                #print("\ti> found epsg code: {0}".format(wkt.split(";")[6]))
                srs_id = wkt.split(";")[0].replace(" ", "").lower().replace("\n", "")
                return wkt.split(";")[6], srs_id, prj_name
        #print("\ti> using geographic epsg code: {0}".format(prj_info.GetAttrValue('AUTHORITY',1)))
        return prj_info.GetAttrValue('AUTHORITY',1), srs_id, prj_name
    except:
        #print("\ti> falling back to default epsg code")
        return "4326", "3452", prj_name

def get_proj4_from(raster_or_shape):
    datafile = gdal.Open(raster_or_shape, gdal.GA_ReadOnly)
    projInfo = datafile.GetProjection()
    spatialRef = osr.SpatialReference()
    spatialRef.ImportFromWkt(projInfo)
    spatialRefProj = spatialRef.ExportToProj4()
    proj_bo = spatialRef.IsGeographic()
    if proj_bo == 0:
        is_projected = "false"
    else:
        is_projected = "true"
    return spatialRefProj, is_projected

def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def convert_raster(input_raster, output_raster, output_format = "GTiff"):
    src_ds = gdal.Open(input_raster)                #Open existing dataset
    driver = gdal.GetDriverByName(output_format)    #Open output format driver, see gdal_translate --formats for list
    dst_ds = driver.CreateCopy(output_raster, src_ds, 0) #Output to new format
    dst_ds = None                                   #Properly close the datasets to flush to disk
    src_ds = None

def run_and_log(command, log_file = 'log.txt'):
    with open(log_file, 'w') as f:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, ''):
            sys.stdout.write(line)
            f.write(line)

def copytree(src, dst, symlinks = False, ignore = None):
  if not os.path.exists(dst):
    os.makedirs(dst)
    shutil.copystat(src, dst)
  lst = os.listdir(src)
  if ignore:
    excl = ignore(src, lst)
    lst = [x for x in lst if x not in excl]
  for item in lst:
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if symlinks and os.path.islink(s):
      if os.path.lexists(d):
        os.remove(d)
      os.symlink(os.readlink(s), d)
      try:
        st = os.lstat(s)
        mode = stat.S_IMODE(st.st_mode)
        os.lchmod(d, mode)
      except:
        pass # lchmod not available
    elif os.path.isdir(s):
      copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)


def copy_file(original_file_path, destination):
    if os.path.isfile(destination):
        delete_file(destination)
    if not os.path.isdir(os.path.dirname(destination)): 
        os.makedirs(os.path.dirname(destination))
    try:
        shutil.copy(original_file_path, destination)
    except:
        raise

def get_days_in_year(year):
    days_ = (datetime.date(year + 1, 1, 1) - datetime.date(year, 1, 1)).days
    return days_

def list_files_from(folder, extension):
    if folder.endswith("/"):
        if extension == "":
            list_of_files = glob(folder + "*")
        else:
            list_of_files = glob(folder + "*." + extension)
    else:
        if extension == "":
            list_of_files = glob(folder + "/*")
        else:
            list_of_files = glob(folder + "/*." + extension)
    return list_of_files

def delete_file(file_path):
    os.remove(file_path)

def create_directory(folder_path):
    directory = os.path.dirname(folder_path)
    try:
        os.makedirs(directory)
    except:
        pass

def write_to(filename,text_to_write):
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close
    
def read_from(filename):
    g = open(filename, 'r')
    file_text = g.readlines()
    return file_text
    g.close

def get_filename(sub_basin_number, HRU_number, table):
    def get_part(number):
        if number < 10:
            subpar = "0000" + str(number) 
        elif number >=10 and number <100:
            subpar = "000" + str(number)
        elif number >=100 and number <1000:
            subpar = "00" + str(number)
        elif number >=1000 and number <10000:
            subpar = "0" + str(number)
        else:
            subpar = str(number)
        return subpar

    subB = get_part(sub_basin_number)
    hruP = get_part(HRU_number)[1:5]

    filename = subB + hruP + "." + table
    return filename

def trailing_zeros(max_spaces,number,decimals):
    if decimals == 0:
        the_val = "{0:.0f}".format(round(float(number),decimals))  
    elif decimals == 1:
        the_val = "{0:.1f}".format(round(float(number),decimals))  
    elif decimals == 2:
        the_val = "{0:.2f}".format(round(float(number),decimals))  
    elif decimals == 3:
        the_val = "{0:.3f}".format(round(float(number),decimals))  
    elif decimals == 4:
        the_val = "{0:.4f}".format(round(float(number),decimals))  
    elif decimals == 5:
        the_val = "{0:.5f}".format(round(float(number),decimals))  
    elif decimals == 6:
        the_val = "{0:.6f}".format(round(float(number),decimals))  
    elif decimals == 7:
        the_val = "{0:.7f}".format(round(float(number),decimals))  
    else:
        #print("Error: Too many decimal Spaces for the function to handle")
        sys.exit()
    
    leading_degits = max_spaces - len(str(the_val).strip("-"))

    if "-" in str(the_val):
        the_val = str(the_val).strip("-")
        final_string = "-" + "0" * (leading_degits - 1) + str(the_val)

    else:
        final_string = "0" * leading_degits + str(the_val)
        
    return final_string

def string_trailing_spaces(max_spaces,the_string):
    leading_spaces = max_spaces - len(str(the_string))
    final_string = " "*leading_spaces + str(the_string)
    return final_string

def round_decimal(value, rounding):
    number = Decimal(str(value))
    decimal_point = float("1e%d" % -rounding)
    return float(number.quantize(Decimal(str(decimal_point)), ROUND_HALF_UP)) #to avoid rounding 'down' for even whole numbers if .5

def trailing_spaces(max_spaces,number,decimals):
    the_val = None
    try:
        float(number)
    except:
        the_val = ""
        decimals = -1
        
    if decimals == 0:
        the_val = "{0:.0f}".format(round_decimal(float(number),decimals))  
    elif decimals == 1:
        the_val = "{0:.1f}".format(round_decimal(float(number),decimals))  
    elif decimals == 2:
        the_val = "{0:.2f}".format(round_decimal(float(number),decimals))  
    elif decimals == 3:
        the_val = "{0:.3f}".format(round_decimal(float(number),decimals))  
    elif decimals == 4:
        the_val = "{0:.4f}".format(round_decimal(float(number),decimals))  
    elif decimals == 5:
        the_val = "{0:.5f}".format(round_decimal(float(number),decimals))  
    elif decimals == 6:
        the_val = "{0:.6f}".format(round_decimal(float(number),decimals))  
    elif decimals == 7:
        the_val = "{0:.7f}".format(round_decimal(float(number),decimals))  
    else:
        pass
        #print("Error: Too many decimal Spaces for the function to handle")

    leading_degits = max_spaces - len(str(the_val))
    final_string = " "*leading_degits + str(the_val)

    return final_string

def extract_table_from_mdb(mdb_path,table,output_file):
    # set up some constants
    DRV = '{Microsoft Access Driver (*.mdb)}'; PWD = 'pw'

    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,mdb_path,PWD))
    cur = con.cursor()

    # run a query and get the results 
    SQL = 'SELECT * FROM ' + table + ';' # your query goes here
    rows = cur.execute(SQL).fetchall()
    #column_names = [d[0] for d in cur.description]
    #print column_names
    #for row in cur:
    #    yield dict(itertools.izip(columns, row))
    #print dict

    cur.close()
    con.close()
    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    with open(output_file, 'wb') as fou:
        csv_writer = csv.writer(fou) # default field-delimiter is ","
        csv_writer.writerows(rows)

    table_contents = read_from(output_file)
    return table_contents

    
def format_data_type(table_dictionary, rgn_table):
    for key in table_dictionary:
        notfound = False
        if table_dictionary[key] == "":
            table_dictionary[key] = None
            continue
        if table_dictionary[key] == '"': #Tests didnt work
            table_dictionary[key] = None
            continue
        if table_dictionary[key] == None:
            continue
        for record in rgn_table:
            if key == record.split(",")[0].strip("\[").strip("\]"):
                if (record.split(",")[5][0:4] == "AUTO") or (record.split(",")[5][0:4] == "INTE"):
                    table_dictionary[key] = int(float(str(table_dictionary[key]).replace("'","").replace('"','')))     # gave me problems when a decimal is coverted to integer
                    #if record.split(",")[3] == "na":
                    #    table_dictionary[key] = int(1)
                    #else:
                    #    table_dictionary[key] = int(table_dictionary[key])
                elif (record.split(",")[5][0:4] == "FLOA"):
                    table_dictionary[key] = float(table_dictionary[key])
                elif (record.split(",")[5][0:4] == "TEXT"):
                    table_dictionary[key] = str(table_dictionary[key])
                break
        notfound = True
        if notfound:
            for record in rgn_table:
                if key[0:4] == record.split(",")[0].strip("\[").strip("\]")[0:4]:
                    if (record.split(",")[5][0:4] == "AUTO") or (record.split(",")[5][0:4] == "INTE"):
                        table_dictionary[key] = int(float(str(table_dictionary[key]).replace("'","").replace('"','')))     # gave me problems when a decimal is coverted to integer
                        #if record.split(",")[3] == "na":
                        #    table_dictionary[key] = int(1)
                        #else:
                        #    table_dictionary[key] = int(table_dictionary[key])
                    elif (record.split(",")[5][0:4] == "FLOA"):
                        table_dictionary[key] = float(table_dictionary[key])
                    elif (record.split(",")[5][0:4] == "TEXT"):
                        table_dictionary[key] = str(table_dictionary[key])

    return table_dictionary

def update_status(message, logging = False):
    if logging:
        print(message)
    else:
        sys.stdout.write("\r\t\t\t\t\t\t\t\t")
        sys.stdout.flush()
        sys.stdout.write("\r" + message)
        sys.stdout.flush()

def update_progress(count, end_val, bar_length):  # bar_length=22
    percent = float(count) / end_val
    hashes = "#" * int(round(percent * bar_length))
    spaces = '_' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent Complete: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()

def create_text_from_dbf(filename):  # file is created in the same directory
    if filename.endswith('.dbf'):
        csv_fn = filename[:-4] + ".txt"
        with open(csv_fn, 'wb') as csvfile:
            in_db = dbf.Dbf(filename)
            out_csv = csv.writer(csvfile)
            names = []
            for field in in_db.header.fields:
                names.append(field.name)
            out_csv.writerow(names)
            for rec in in_db:
                out_csv.writerow(rec.fieldData)
            in_db.close()
    else:
        #print("Error: Could not find a lookup .dbf file")
        sys.exit()
    return csv_fn.replace("\\", "/")
