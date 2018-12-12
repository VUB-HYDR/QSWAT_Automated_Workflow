'''
Author      : Celray James CHAWANDA (celray.chawanda@outlook.com)
Institution : Vrije Universiteit Brussel (VUB)

This script applies parameters to the database based on settings in the namelist the bsn file
'''

import sys

import cj_function_lib as cj
import init_file as variables
import mdbtools as mdt
import namelist

# read present bsn
bsn     = cj.extract_table_from_mdb(variables.ProjMDB, 'bsn', variables.path + "\\bsn.tmp~")
fields  = ["OID", "SFTMP", "SMTMP", "SMFMX", "SMFMN", "TIMP", "SNOCOVMX", "SNO50COV", "IPET", "ESCO", "EPCO", "EVLAI", "FFCB", "IEVENT", "ICRK", "SURLAG", "ADJ_PKR", "PRF_BSN", "SPCON", "SPEXP", "RCN", "CMN", "N_UPDIS", "P_UPDIS", "NPERCO", "PPERCO", "PHOSKD", "PSP", "RSDCO", "PERCOP", "ISUBWQ", "WDPQ", "WGPQ", "WDLPQ", "WGLPQ", "WDPS", "WGPS", "WDLPS", "WGLPS", "BACTKDQ", "THBACT", "WOF_P", "WOF_LP", "WDPF", "WGPF", "WDLPF", "WGLPF", "IRTE", "MSK_CO1", "MSK_CO2", "MSK_X", "IDEG", "IWQ", "TRNSRCH", "EVRCH", "IRTPEST", "ICN", "CNCOEF", "CDN", "SDNCO", "BACT_SWF", "BACTMX", "BACTMINLP", "BACTMINP", "WDLPRCH", "WDPRCH", "WDLPRES", "WDPRES", "TB_ADJ", "DEP_IMP", "DDRAIN_BSN", "TDRAIN_BSN", "GDRAIN_BSN", "CN_FROZ", "ISED_DET", "ETFILE", "DORM_HR", "SMXCO", "FIXCO", "NFIXMX", "ANION_EXCL_BSN", "CH_ONCO_BSN", "CH_OPCO_BSN", "HLIFE_NGW_BSN", "RCN_SUB_BSN", "BC1_BSN", "BC2_BSN", "BC3_BSN", "BC4_BSN", "DECR_MIN", "ICFAC", "RSD_COVCO", "VCRIT", "CSWAT", "RES_STLR_CO", "BFLO_DIST", "IUH", "UHALPHA", "LU_NODRAIN", "EROS_SPL", "RILL_MULT", "EROS_EXPO", "SUBD_CHSED", "C_FACTOR", "CH_D50", "SIG_G", "RE_BSN", "SDRAIN_BSN", "DRAIN_CO_BSN", "PC_BSN", "LATKSATF_BSN", "ITDRN", "IWTDN", "SOL_P_MODEL", "IABSTR", "IATMODEP", "RAMMO_SUB", "RCN_SUB", "DRYDEP_NH4", "DRYDEP_NO3", "R2ADJ_BSN", "SSTMAXD_BSN", "ISMAX", "IROUTUNIT"]

bsn_dictionary = {}

count = 0
for field in fields:
        bsn_dictionary[field] = bsn[0].split(",")[count]
        count += 1


if namelist.Run_off_method == 1:
        bsn_dictionary["IEVENT"] = 0

if namelist.Run_off_method == 2:
        if namelist.rainfall_timestep == 1:
                bsn_dictionary["IEVENT"] = 1
        elif namelist.Routing_timestep == 1:
                bsn_dictionary["IEVENT"] = 2
        else:
                bsn_dictionary["IEVENT"] = 3

bsn_dictionary["IPET"] = namelist.ET_method - 1
if namelist.Routing_method == 2:
        bsn_dictionary["IRTE"] = 0                              # variable storage
else:
        bsn_dictionary["IRTE"] = namelist.Routing_method        # muskingum

"""
# here we commit to table the parameters for the basin to a row in the table bsn
"""
db = mdt.mdb_with_ops(variables.ProjMDB)
db.connect()
db.clear_table("bsn")
db.insert_row("bsn", bsn_dictionary, True)
db.disconnect()
