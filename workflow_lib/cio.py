
import sys
import os.path

import cj_function_lib as cj
import init_file as variables
import namelist
import mdbtools as mdt

#print variables.ProjMDB
#print variables.QSWAT_MDB

ciorgn = cj.extract_table_from_mdb(
    variables.QSWAT_MDB, 'ciorng', variables.path + "\\ciorgn.tmp~")
cio_configuration = cj.read_from(variables.path + "\\cio_config.tmp~")

cio_defaults = {}
defaults_list = []
for record in ciorgn:  # Getting a list of parameter names for cio and their defaults
    if record.split(",")[0].strip(" ") != "":
        cio_defaults[record.split(",")[0].strip(
            "\[").strip("\]")] = record.split(",")[3]
        defaults_list.append(record.split(",")[0].strip("\[").strip("\]"))

"""
# here we commit to table the parameters for the hru to a row in the table cio
"""
cio = mdt.mdb_with_ops(variables.ProjMDB)

cio.connect()

cio.create_table("cio", "OID", "INTEGER")
for field in defaults_list:
    cio.add_field("cio", field, "TEXT")

cio.clear_table("cio")

cio_defaults["OID"] = int(1)

cio_defaults["IPRINT"] = 1
cio_defaults["NBYR"] = cio_configuration[2]
cio_defaults["IYR"] = cio_configuration[0]
cio_defaults["IDAF"] = 1
cio_defaults["IDAL"] = cio_configuration[4]


if os.path.isfile(variables.pcp_file_txt):
    cio_defaults["PCPSIM"] = 1
    cio_defaults["NRGAGE"] = 1
    cio_defaults["NRTOT"] = cio_configuration[6]
    cio_defaults["NRGFIL"] = cio_configuration[6]
    
else:
    cio_defaults["PCPSIM"] = 2
    cio_defaults["NRGAGE"] = 0
    cio_defaults["NRTOT"] = 0
    cio_defaults["NRGFIL"] = 0

if os.path.isfile(variables.tmp_file_txt):
    cio_defaults["TMPSIM"] = 1
    cio_defaults["NTGAGE"] = 1
    cio_defaults["NTTOT"] = cio_configuration[6]
    cio_defaults["NTGFIL"] = cio_configuration[6]
else:
    cio_defaults["TMPSIM"] = 2
    cio_defaults["NTGAGE"] = 0
    cio_defaults["NTTOT"] = 0
    cio_defaults["NTGFIL"] = 0

hmd = "       "
if os.path.isfile(variables.hmd_file_txt):
    cio_defaults["RHSIM"] = 1
    cio_defaults["NHTOT"] = cio_configuration[6]
    hmd = "hmd.hmd"
else:
    cio_defaults["RHSIM"] = 2
    cio_defaults["NHTOT"] = 0

slr = "       "
if os.path.isfile(variables.slr_file_txt):
    cio_defaults["SLRSIM"] = 1
    cio_defaults["NSTOT"] = cio_configuration[6]
    slr = "slr.slr"
else:
    cio_defaults["SLRSIM"] = 2
    cio_defaults["NSTOT"] = 0

wnd = "       "
if os.path.isfile(variables.wnd_file_txt):
    cio_defaults["WNDSIM"] = 1
    cio_defaults["NWTOT"] = cio_configuration[6]
    wnd = "wnd.wnd"
else:
    cio_defaults["SLRSIM"] = 2
    cio_defaults["NWTOT"] = 0

cio_defaults["FCSTYR"] = 0
cio_defaults["FCSTDAY"] = 0
cio_defaults["FCSTCYCLES"] = 0

cio_defaults["DATES"] = "1/1/" + cio_configuration[0].strip("\n")
cio_defaults["DATEF"] = "12/31/" + cio_configuration[1].strip("\n")
cio_defaults["FDATES"] = None

cio_defaults["DEPFILE"] = cio_defaults["DEPFILE"].strip("'")

cio_defaults = cj.format_data_type(cio_defaults, ciorgn)
cio.insert_row("cio", cio_defaults, True)



from datetime import datetime

cio_table = cj.extract_table_from_mdb(variables.ProjMDB, "cio", variables.path + "\\cio.tmp~")

now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"


# Parameters
if namelist.Model_Run_period.replace(" ","") != "":
    NBYR    = int(namelist.Model_Run_period.replace(" ","").split("-")[1]) - int(namelist.Model_Run_period.replace(" ","").split("-")[0])
    IYR     = int(namelist.Model_Run_period.replace(" ","").split("-")[0])
else:
    NBYR    = cio_table[0].split(",")[1]
    IYR     = cio_table[0].split(",")[2]

IDAF = cio_table[0].split(",")[3]
IDAL = cio_table[0].split(",")[4]
IGEN = cio_table[0].split(",")[5]
PCPSIM = cio_table[0].split(",")[6]
IDT = cio_table[0].split(",")[7]
IDIST = cio_table[0].split(",")[8]
REXP = cio_table[0].split(",")[9]
NRGAGE = cio_table[0].split(",")[10]
NRTOT = cio_table[0].split(",")[11]
NRGFIL = cio_table[0].split(",")[12]
TMPSIM = cio_table[0].split(",")[13]
NTGAGE = cio_table[0].split(",")[14]
NTTOT = cio_table[0].split(",")[15]
NTGFIL = cio_table[0].split(",")[16]
SLRSIM = cio_table[0].split(",")[17]
NSTOT = cio_table[0].split(",")[18]
RHSIM = cio_table[0].split(",")[19]
NHTOT = cio_table[0].split(",")[20]
WNDSIM = cio_table[0].split(",")[21]
NWTOT = cio_table[0].split(",")[22]
FCSTYR = cio_table[0].split(",")[23]
FCSTDAY = cio_table[0].split(",")[24]
FCSTCYCLES = cio_table[0].split(",")[25]
DATES = cio_table[0].split(",")[26]
DATEF = cio_table[0].split(",")[27]
FDATES = cio_table[0].split(",")[28]
ISPROJ = cio_table[0].split(",")[29]
ICLB = cio_table[0].split(",")[30]
#IPRINT = cio_table[0].split(",")[31]
IPRINT = '0'
if namelist.Warm_up_period == "":
    NYSKIP = cio_table[0].split(",")[32]
else:
    NYSKIP = namelist.Warm_up_period
ILOG = cio_table[0].split(",")[33]
IPRP = cio_table[0].split(",")[34]
IPRS = cio_table[0].split(",")[35]
DEPFILE = cio_table[0].split(",")[36]
IPHR = cio_table[0].split(",")[37]
ISTO = cio_table[0].split(",")[38]
ISOL = cio_table[0].split(",")[39]
I_SUBW = cio_table[0].split(",")[40]
IA_B = cio_table[0].split(",")[41]
IHUMUS = cio_table[0].split(",")[42]
ISNOW = cio_table[0].split(",")[43]
ITEMP = cio_table[0].split(",")[44]
IMGT = cio_table[0].split(",")[45]
IWTR = cio_table[0].split(",")[46]
ICALEN = cio_table[0].split(",")[47]

# Building String
cio_file = "Master Watershed File: file.cio" + \
    "\n" + "Project Description:" + \
    "\n" + "General Input/Output section (file.cio):" + \
    "\n" + DateAndTime + " " + SWAT_Vers + \
    "\n" + \
    "\n" + "General Information/Watershed Configuration:" + \
    "\n" + "fig.fig" + \
    "\n" + cj.trailing_spaces(16, NBYR, 0) + "    | NBYR : Number of years simulated" + \
    "\n" + cj.trailing_spaces(16, IYR, 0) + "    | IYR : Beginning year of simulation" + \
    "\n" + cj.trailing_spaces(16, IDAF, 0) + "    | IDAF : Beginning julian day of simulation" + \
    "\n" + cj.trailing_spaces(16, IDAL, 0) + "    | IDAL : Ending julian day of simulation" + \
    "\n" + "Climate:" + \
    "\n" + cj.trailing_spaces(16, IGEN, 0) + "    | IGEN : Random number seed cycle code" + \
    "\n" + cj.trailing_spaces(16, PCPSIM, 0) + "    | PCPSIM : precipitation simulation code: 1=measured, 2=simulated" + \
    "\n" + cj.trailing_spaces(16, IDT, 0) + "    | IDT : Rainfall data time step" + \
    "\n" + cj.trailing_spaces(16, IDIST, 0) + "    | IDIST : rainfall distribution code: 0 skewed, 1 exponential" + \
    "\n" + cj.trailing_spaces(16, REXP, 3) + "    | REXP : Exponent for IDIST=1" + \
    "\n" + cj.trailing_spaces(16, NRGAGE, 0) + "    | NRGAGE: number of pcp files used in simulation" + \
    "\n" + cj.trailing_spaces(16, NRTOT, 0) + "    | NRTOT: number of precip gage records used in simulation" + \
    "\n" + cj.trailing_spaces(16, NRGFIL, 0) + "    | NRGFIL: number of gage records in each pcp file" + \
    "\n" + cj.trailing_spaces(16, TMPSIM, 0) + "    | TMPSIM: temperature simulation code: 1=measured, 2=simulated" + \
    "\n" + cj.trailing_spaces(16, NTGAGE, 0) + "    | NTGAGE: number of tmp files used in simulation" + \
    "\n" + cj.trailing_spaces(16, NTTOT, 0) + "    | NTTOT: number of temp gage records used in simulation" + \
    "\n" + cj.trailing_spaces(16, NTGFIL, 0) + "    | NTGFIL: number of gage records in each tmp file" + \
    "\n" + cj.trailing_spaces(16, SLRSIM, 0) + "    | SLRSIM : Solar radiation simulation Code: 1=measured, 2=simulated" + \
    "\n" + cj.trailing_spaces(16, NSTOT, 0) + "    | NSTOT: number of solar radiation records in slr file" + \
    "\n" + cj.trailing_spaces(16, RHSIM, 0) + "    | RHSIM : relative humidity simulation code: 1=measured, 2=simulated" + \
    "\n" + cj.trailing_spaces(16, NHTOT, 0) + "    | NHTOT: number of relative humidity records in hmd file" + \
    "\n" + cj.trailing_spaces(16, WNDSIM, 0) + "    | WINDSIM : Windspeed simulation code: 1=measured, 2=simulated" + \
    "\n" + cj.trailing_spaces(16, NWTOT, 0) + "    | NWTOT: number of wind speed records in wnd file" + \
    "\n" + cj.trailing_spaces(16, FCSTYR, 0) + "    | FCSTYR: beginning year of forecast period" + \
    "\n" + cj.trailing_spaces(16, FCSTDAY, 0) + "    | FCSTDAY: beginning julian date of forecast period" + \
    "\n" + cj.trailing_spaces(16, FCSTCYCLES, 0) + "    | FCSTCYCLES: number of time to simulate forecast period" + \
    "\n" + "Precipitation Files:" + \
    "\n" + "pcp1.pcp" + \
    "\n" + \
    "\n" + \
    "\n" + "Temperature Files:" + \
    "\n" + "tmp1.tmp" + \
    "\n" + \
    "\n" + \
    "\n" + slr + "             | SLRFILE: name of solar radiation file" + \
    "\n" + hmd + "             | RHFILE: name of relative humidity file" + \
    "\n" + wnd + "             | WNDFILE: name of wind speed file" + \
    "\n" + "cst.cst             | FCSTFILE: name of forecast data file" + \
    "\n" + "Watershed Modeling Options:" + \
    "\n" + "basins.bsn          | BSNFILE: name of basin input file" + \
    "\n" + "Database Files:" + \
    "\n" + "plant.dat           | PLANTDB: name of plant growth database file" + \
    "\n" + "till.dat            | TILLDB: name of tillage database file" + \
    "\n" + "pest.dat            | PESTDB: name of pesticide database file" + \
    "\n" + "fert.dat            | FERTDB: name of fertilizer database file" + \
    "\n" + "urban.dat           | URBANDB: name of urban database file" + \
    "\n" + "Special Projects:" + \
    "\n" + cj.trailing_spaces(16, ISPROJ, 0) + "    | ISPROJ: special project: 1=repeat simulation" + \
    "\n" + cj.trailing_spaces(16, ICLB, 0) + "    | ICLB: auto-calibration option: 0=no, 1=yes" + \
    "\n" + "                " + "    | CALFILE: auto-calibration parameter file" + \
    "\n" + "Output Information:" + \
    "\n" + cj.trailing_spaces(16, IPRINT, 0) + "    | IPRINT: print code (month, day, year)" + \
    "\n" + cj.trailing_spaces(16, NYSKIP, 0) + "    | NYSKIP: number of years to skip output printing/summarization" + \
    "\n" + cj.trailing_spaces(16, ILOG, 0) + "    | ILOG: streamflow print code: 1=print log of streamflow" + \
    "\n" + cj.trailing_spaces(16, IPRP, 0) + "    | IPRP: print code for output.pst file: 1= print pesticide output" + \
    "\n" + "Starting Output Variable Section" + \
    "\n" + "Reach output variables:" + \
    "\n" + "   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0" + \
    "\n" + "Subbasin output variables:" + \
    "\n" + "   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0" + \
    "\n" + "HRU output variables:" + \
    "\n" + "   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0" + \
    "\n" + "HRU data to be printed:" + \
    "\n" + "   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0" + \
    "\n" + "ATMOSPERIC DEPOSITION" + \
    "\n" + "ATMO.ATM" + \
    "\n" + cj.trailing_spaces(16, IPHR, 0) + "    | IPHR: print code for hourly output 0=no 1=yes (hourq.out)" + \
    "\n" + cj.trailing_spaces(16, ISTO, 0) + "    | ISTO: print code for soil storage 0=no 1=yes (output.swr)" + \
    "\n" + cj.trailing_spaces(16, ISOL, 0) + "    | ISOL: Code for printing phosphorus/nitrogen in soil profile (output.snu)" + \
    "\n" + cj.trailing_spaces(16, I_SUBW, 0) + "    | I_SUBW: Code for routing headwaters" + \
    "\n" + "septwq.dat" + \
    "\n" + cj.trailing_spaces(16, IA_B, 0) + "    | IA_B: Code for binary output of files (.rch, .sub, .hru files only)" + \
    "\n" + cj.trailing_spaces(16, IHUMUS, 0) + "    | IHUMUS: Print watqual.out file 0=no 1=yes (output.wql)" + \
    "\n" + cj.trailing_spaces(16, ITEMP, 0) + "    | ITEMP: 0=print no file(s) 1=print output.vel/output.dep" + \
    "\n" + cj.trailing_spaces(16, ISNOW, 0) + "    | ISNOW: 0=do not print snowband.out; 1=print output.snw" + \
    "\n" + cj.trailing_spaces(16, IMGT, 0) + "    | IMGT: 0=do not print output.mtg; 1=print output.mgt" + \
    "\n" + cj.trailing_spaces(16, IWTR, 0) + "    | IWTR: Code for printing output.pot and output.wtr files" + \
    "\n" + cj.trailing_spaces(16, ICALEN, 0) + "    | ICALEN: Code for printing out calendar or julian dates to .rch, .sub and .hru files" + \
    "\n"
fileName = "file.cio"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, cio_file)
#print fileName



