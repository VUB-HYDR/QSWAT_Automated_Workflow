"""
Author      : Celray James CHAWANDA (celray.chawanda@outlook.com)
Institution : Vrije Universiteit Brussel (VUB)

This script writes the bsn file
"""


import init_file as variables
import cj_function_lib as cj
from datetime import datetime

bsn_table = cj.extract_table_from_mdb(variables.ProjMDB, "bsn", variables.path + "\\bsn.tmp~")

bsn_params = bsn_table[0].split(",")
now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

# Parameters
SFTMP = bsn_params[1].strip('"')
SMTMP = bsn_params[2].strip('"')
SMFMX = bsn_params[3].strip('"')
SMFMN = bsn_params[4].strip('"')
TIMP = bsn_params[5].strip('"')
SNOCOVMX = bsn_params[6].strip('"')
SNO50COV = bsn_params[7].strip('"')
IPET = bsn_params[8].strip('"')
ESCO = bsn_params[9].strip('"')
EPCO = bsn_params[10].strip('"')
EVLAI = bsn_params[11].strip('"')
FFCB = bsn_params[12].strip('"')
IEVENT = bsn_params[13].strip('"')
ICRK = bsn_params[14].strip('"')
SURLAG = bsn_params[15].strip('"')
ADJ_PKR = bsn_params[16].strip('"')
PRF_BSN = bsn_params[17].strip('"')
SPCON = bsn_params[18].strip('"')
SPEXP = bsn_params[19].strip('"')
RCN = bsn_params[20].strip('"')
CMN = bsn_params[21].strip('"')
N_UPDIS = bsn_params[22].strip('"')
P_UPDIS = bsn_params[23].strip('"')
NPERCO = bsn_params[24].strip('"')
PPERCO = bsn_params[25].strip('"')
PHOSKD = bsn_params[26].strip('"')
PSP = bsn_params[27].strip('"')
RSDCO = bsn_params[28].strip('"')
PERCOP = bsn_params[29].strip('"')
ISUBWQ = bsn_params[30].strip('"')
WDPQ = bsn_params[31].strip('"')
WGPQ = bsn_params[32].strip('"')
WDLPQ = bsn_params[33].strip('"')
WGLPQ = bsn_params[34].strip('"')
WDPS = bsn_params[35].strip('"')
WGPS = bsn_params[36].strip('"')
WDLPS = bsn_params[37].strip('"')
WGLPS = bsn_params[38].strip('"')
BACTKDQ = bsn_params[39].strip('"')
THBACT = bsn_params[40].strip('"')
WOF_P = bsn_params[41].strip('"')
WOF_LP = bsn_params[42].strip('"')
WDPF = bsn_params[43].strip('"')
WGPF = bsn_params[44].strip('"')
WDLPF = bsn_params[45].strip('"')
WGLPF = bsn_params[46].strip('"')
IRTE = bsn_params[47].strip('"')
MSK_CO1 = bsn_params[48].strip('"')
MSK_CO2 = bsn_params[49].strip('"')
MSK_X = bsn_params[50].strip('"')
IDEG = bsn_params[51].strip('"')
IWQ = bsn_params[52].strip('"')
TRNSRCH = bsn_params[53].strip('"')
EVRCH = bsn_params[54].strip('"')
IRTPEST = bsn_params[55].strip('"')
ICN = bsn_params[56].strip('"')
CNCOEF = bsn_params[57].strip('"')
CDN = bsn_params[58].strip('"')
SDNCO = bsn_params[59].strip('"')
BACT_SWF = bsn_params[60].strip('"')
BACTMX = bsn_params[61].strip('"')
BACTMINLP = bsn_params[62].strip('"')
BACTMINP = bsn_params[63].strip('"')
WDLPRCH = bsn_params[64].strip('"')
WDPRCH = bsn_params[65].strip('"')
WDLPRES = bsn_params[66].strip('"')
WDPRES = bsn_params[67].strip('"')
TB_ADJ = bsn_params[68].strip('"')
DEP_IMP = bsn_params[69].strip('"')
DDRAIN_BSN = bsn_params[70].strip('"')
TDRAIN_BSN = bsn_params[71].strip('"')
GDRAIN_BSN = bsn_params[72].strip('"')
CN_FROZ = bsn_params[73].strip('"')
ISED_DET = bsn_params[74].strip('"')
ETFILE = bsn_params[75].strip('"')
DORM_HR = bsn_params[76].strip('"')
SMXCO = bsn_params[77].strip('"')
FIXCO = bsn_params[78].strip('"')
NFIXMX = bsn_params[79].strip('"')
ANION_EXCL_BSN = bsn_params[80].strip('"')
CH_ONCO_BSN = bsn_params[81].strip('"')
CH_OPCO_BSN = bsn_params[82].strip('"')
HLIFE_NGW_BSN = bsn_params[83].strip('"')
RCN_SUB_BSN = bsn_params[84].strip('"')
BC1_BSN = bsn_params[85].strip('"')
BC2_BSN = bsn_params[86].strip('"')
BC3_BSN = bsn_params[87].strip('"')
BC4_BSN = bsn_params[88].strip('"')
DECR_MIN = bsn_params[89].strip('"')
ICFAC = bsn_params[90].strip('"')
RSD_COVCO = bsn_params[91].strip('"')
VCRIT = bsn_params[92].strip('"')
CSWAT = bsn_params[93].strip('"')
RES_STLR_CO = bsn_params[94].strip('"')
BFLO_DIST = bsn_params[95].strip('"')
IUH = bsn_params[96].strip('"')
UHALPHA = bsn_params[97].strip('"')
LU_NODRAIN = bsn_params[98].strip('"')
EROS_SPL = bsn_params[99].strip('"')
RILL_MULT = bsn_params[100].strip('"')
EROS_EXPO = bsn_params[101].strip('"')
SUBD_CHSED = bsn_params[102].strip('"')
C_FACTOR = bsn_params[103].strip('"')
CH_D50 = bsn_params[104].strip('"')
SIG_G = bsn_params[105].strip('"')
RE_BSN = bsn_params[106].strip('"')
SDRAIN_BSN = bsn_params[107].strip('"')
DRAIN_CO_BSN = bsn_params[108].strip('"')
PC_BSN = bsn_params[109].strip('"')
LATKSATF_BSN = bsn_params[110].strip('"')
ITDRN = bsn_params[111].strip('"')
IWTDN = bsn_params[112].strip('"')
SOL_P_MODEL = bsn_params[113].strip('"')
IABSTR = bsn_params[114].strip('"')
IATMODEP = bsn_params[115].strip('"')
RAMMO_SUB = bsn_params[116].strip('"')
RCN_SUB = bsn_params[117].strip('"')
DRYDEP_NH4 = bsn_params[118].strip('"')
DRYDEP_NO3 = bsn_params[119].strip('"')
R2ADJ_BSN = bsn_params[120].strip('"')
SSTMAXD_BSN = bsn_params[121].strip('"')
ISMAX = bsn_params[122].strip('"')
IROUTUNIT = bsn_params[123].strip('"')


# Building String
bsn_file = "Basin data           .bsn file " + DateAndTime + " " + SWAT_Vers + \
    "\n" + "Modeling Options: Land Area" + \
    "\n" + "Water Balance:" + \
    "\n" + cj.trailing_spaces(16, SFTMP, 3) + "    | SFTMP : Snowfall temperature [deg C]" + \
    "\n" + cj.trailing_spaces(16, SMTMP, 3) + "    | SMTMP : Snow melt base temperature [deg C]" + \
    "\n" + cj.trailing_spaces(16, SMFMX, 3) + "    | SMFMX : Melt factor for snow on June 21 [mm H2O/deg C-day]" + \
    "\n" + cj.trailing_spaces(16, SMFMN, 3) + "    | SMFMN : Melt factor for snow on December 21 [mm H2O/deg C-day]" + \
    "\n" + cj.trailing_spaces(16, TIMP, 3) + "    | TIMP : Snow pack temperature lag factor" + \
    "\n" + cj.trailing_spaces(16, SNOCOVMX, 3) + "    | SNOCOVMX : Minimum snow water content that corresponds to 100% snow cover [mm]" + \
    "\n" + cj.trailing_spaces(16, SNO50COV, 3) + "    | SNO50COV : Fraction of snow volume represented by SNOCOVMX that corresponds to 50% snow cover" + \
    "\n" + cj.trailing_spaces(16, IPET, 0) + "    | IPET: PET method: 0=priest-t, 1=pen-m, 2=har, 3=read into model" + \
    "\n" + "                " + "    | PETFILE: name of potential ET input file" + \
    "\n" + cj.trailing_spaces(16, ESCO, 3) + "    | ESCO: soil evaporation compensation factor" + \
    "\n" + cj.trailing_spaces(16, EPCO, 3) + "    | EPCO: plant water uptake compensation factor" + \
    "\n" + cj.trailing_spaces(16, EVLAI, 3) + "    | EVLAI : Leaf area index at which no evaporation occurs from water surface [m2/m2]" + \
    "\n" + cj.trailing_spaces(16, FFCB, 3) + "    | FFCB : Initial soil water storage expressed as a fraction of field capacity water content" + \
    "\n" + "Surface Runoff:" + \
    "\n" + cj.trailing_spaces(16, IEVENT, 0) + "    | IEVENT: rainfall/runoff code: 0=daily rainfall/CN" + \
    "\n" + cj.trailing_spaces(16, ICRK, 0) + "    | ICRK: crack flow code: 1=model crack flow in soil" + \
    "\n" + cj.trailing_spaces(16, SURLAG, 3) + "    | SURLAG : Surface runoff lag time [days]" + \
    "\n" + cj.trailing_spaces(16, ADJ_PKR, 3) + "    | ADJ_PKR : Peak rate adjustment factor for sediment routing in the subbasin (tributary channels)" + \
    "\n" + cj.trailing_spaces(16, PRF_BSN, 3) + "    | PRF_BSN : Peak rate adjustment factor for sediment routing in the main channel" + \
    "\n" + cj.trailing_spaces(16, SPCON, 4) + "    | SPCON : Linear parameter for calculating the maximum amount of sediment that can be reentrained during channel sediment routing" + \
    "\n" + cj.trailing_spaces(16, SPEXP, 3) + "    | SPEXP : Exponent parameter for calculating sediment reentrained in channel sediment routing" + \
    "\n" + "Nutrient Cycling:" + \
    "\n" + cj.trailing_spaces(16, RCN, 3) + "    | RCN : Concentration of nitrogen in rainfall [mg N/l]" + \
    "\n" + cj.trailing_spaces(16, CMN, 5) + "    | CMN : Rate factor for humus mineralization of active organic nitrogen" + \
    "\n" + cj.trailing_spaces(16, N_UPDIS, 3) + "    | N_UPDIS : Nitrogen uptake distribution parameter" + \
    "\n" + cj.trailing_spaces(16, P_UPDIS, 3) + "    | P_UPDIS : Phosphorus uptake distribution parameter" + \
    "\n" + cj.trailing_spaces(16, NPERCO, 3) + "    | NPERCO : Nitrogen percolation coefficient" + \
    "\n" + cj.trailing_spaces(16, PPERCO, 3) + "    | PPERCO : Phosphorus percolation coefficient" + \
    "\n" + cj.trailing_spaces(16, PHOSKD, 3) + "    | PHOSKD : Phosphorus soil partitioning coefficient" + \
    "\n" + cj.trailing_spaces(16, PSP, 3) + "    | PSP : Phosphorus sorption coefficient" + \
    "\n" + cj.trailing_spaces(16, RSDCO, 3) + "    | RSDCO : Residue decomposition coefficient" + \
    "\n" + "Pesticide Cycling:" + \
    "\n" + cj.trailing_spaces(16, PERCOP, 3) + "    | PERCOP : Pesticide percolation coefficient" + \
    "\n" + "Algae/CBOD/Dissolved Oxygen:" + \
    "\n" + cj.trailing_spaces(16, ISUBWQ, 0) + "    | ISUBWQ: subbasin water quality parameter" + \
    "\n" + "Bacteria:" + \
    "\n" + cj.trailing_spaces(16, WDPQ, 3) + "    | WDPQ : Die-off factor for persistent bacteria in soil solution. [1/day]" + \
    "\n" + cj.trailing_spaces(16, WGPQ, 3) + "    | WGPQ : Growth factor for persistent bacteria in soil solution [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDLPQ, 3) + "    | WDLPQ : Die-off factor for less persistent bacteria in soil solution [1/day]" + \
    "\n" + cj.trailing_spaces(16, WGLPQ, 3) + "    | WGLPQ : Growth factor for less persistent bacteria in soil solution. [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDPS, 3) + "    | WDPS : Die-off factor for persistent bacteria adsorbed to soil particles. [1/day]" + \
    "\n" + cj.trailing_spaces(16, WGPS, 3) + "    | WGPS : Growth factor for persistent bacteria adsorbed to soil particles. [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDLPS, 3) + "    | WDLPS : Die-off factor for less persistent bacteria adsorbed to soil particles. [1/day]" + \
    "\n" + cj.trailing_spaces(16, WGLPS, 3) + "    | WGLPS : Growth factor for less persistent bacteria adsorbed to soil particles. [1/day]" + \
    "\n" + cj.trailing_spaces(16, BACTKDQ, 3) + "    | BACTKDQ : Bacteria partition coefficient" + \
    "\n" + cj.trailing_spaces(16, THBACT, 3) + "    | THBACT : Temperature adjustment factor for bacteria die-off/growth" + \
    "\n" + cj.trailing_spaces(16, WOF_P, 3) + "    | WOF_P: wash-off fraction for persistent bacteria on foliage" + \
    "\n" + cj.trailing_spaces(16, WOF_LP, 3) + "    | WOF_LP: wash-off fraction for less persistent bacteria on foliage" + \
    "\n" + cj.trailing_spaces(16, WDPF, 3) + "    | WDPF: persistent bacteria die-off factor on foliage" + \
    "\n" + cj.trailing_spaces(16, WGPF, 3) + "    | WGPF: persistent bacteria growth factor on foliage" + \
    "\n" + cj.trailing_spaces(16, WDLPF, 3) + "    | WDLPF: less persistent bacteria die-off factor on foliage" + \
    "\n" + cj.trailing_spaces(16, WGLPF, 3) + "    | WGLPF: less persistent bacteria growth factor on foliage" + \
    "\n" + cj.trailing_spaces(16, ISED_DET, 0) + "    | ISED_DET:" + \
    "\n" + "Modeling Options: Reaches" + \
    "\n" + cj.trailing_spaces(16, IRTE, 0) + "    | IRTE: water routing method 0=variable travel-time 1=Muskingum" + \
    "\n" + cj.trailing_spaces(16, MSK_CO1, 3) + "    | MSK_CO1 : Calibration coefficient used to control impact of the storage time constant (Km) for normal flow" + \
    "\n" + cj.trailing_spaces(16, MSK_CO2, 3) + "    | MSK_CO2 : Calibration coefficient used to control impact of the storage time constant (Km) for low flow " + \
    "\n" + cj.trailing_spaces(16, MSK_X, 3) + "    | MSK_X : Weighting factor controlling relative importance of inflow rate and outflow rate in determining water storage in reach segment" + \
    "\n" + cj.trailing_spaces(16, IDEG, 0) + "    | IDEG: channel degradation code" + \
    "\n" + cj.trailing_spaces(16, IWQ, 0) + "    | IWQ: in-stream water quality: 1=model in-stream water quality" + \
    "\n" + "   basins.wwq       | WWQFILE: name of watershed water quality file" + \
    "\n" + cj.trailing_spaces(16, TRNSRCH, 3) + "    | TRNSRCH: reach transmission loss partitioning to deep aquifer" + \
    "\n" + cj.trailing_spaces(16, EVRCH, 3) + "    | EVRCH : Reach evaporation adjustment factor" + \
    "\n" + cj.trailing_spaces(16, IRTPEST, 0) + "    | IRTPEST : Number of pesticide to be routed through the watershed channel network" + \
    "\n" + cj.trailing_spaces(16, ICN, 0) + "    | ICN  : Daily curve number calculation method" + \
    "\n" + cj.trailing_spaces(16, CNCOEF, 3) + "    | CNCOEF : Plant ET curve number coefficient" + \
    "\n" + cj.trailing_spaces(16, CDN, 3) + "    | CDN : Denitrification exponential rate coefficient" + \
    "\n" + cj.trailing_spaces(16, SDNCO, 3) + "    | SDNCO : Denitrification threshold water content" + \
    "\n" + cj.trailing_spaces(16, BACT_SWF, 3) + "    | BACT_SWF : Fraction of manure applied to land areas that has active colony forming units" + \
    "\n" + cj.trailing_spaces(16, BACTMX, 3) + "    | BACTMX : Bacteria percolation coefficient [10 m3/Mg]." + \
    "\n" + cj.trailing_spaces(16, BACTMINLP, 3) + "    | BACTMINLP : Minimum daily bacteria loss for less persistent bacteria [# cfu/m2]" + \
    "\n" + cj.trailing_spaces(16, BACTMINP, 3) + "    | BACTMINP : Minimum daily bacteria loss for persistent bacteria [# cfu/m2]" + \
    "\n" + cj.trailing_spaces(16, WDLPRCH, 3) + "    | WDLPRCH: Die-off factor for less persistent bacteria in streams (moving water) at 20 C [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDPRCH, 3) + "    | WDPRCH : Die-off factor for persistent bacteria in streams (moving water) at 20 C [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDLPRES, 3) + "    | WDLPRES : Die-off factor for less persistent bacteria in water bodies (still water) at 20 C [1/day]" + \
    "\n" + cj.trailing_spaces(16, WDPRES, 3) + "    | WDPRES : Die-off factor for persistent bacteria in water bodies (still water) at 20 C [1/day]" + \
    "\n" + cj.trailing_spaces(16, TB_ADJ, 3) + "    | TB_ADJ : New variable in testing ...Adjustment factor for subdaily unit hydrograph basetime" + \
    "\n" + cj.trailing_spaces(16, DEP_IMP, 3) + "    | DEPIMP_BSN : Depth to impervious layer for modeling perched water tables [mm]" + \
    "\n" + cj.trailing_spaces(16, DDRAIN_BSN, 3) + "    | DDRAIN_BSN : Depth to the sub-surface drain [mm]" + \
    "\n" + cj.trailing_spaces(16, TDRAIN_BSN, 3) + "    | TDRAIN_BSN : Time to drain soil to field capacity [hours]" + \
    "\n" + cj.trailing_spaces(16, GDRAIN_BSN, 3) + "    | GDRAIN_BSN : Drain tile lag time [hours]" + \
    "\n" + cj.trailing_spaces(16, CN_FROZ, 6) + "    | CN_FROZ : Parameter for frozen soil adjustment on infiltration/runoff" + \
    "\n" + cj.trailing_spaces(16, DORM_HR, 3) + "    | DORM_HR : Time threshold used to define dormancy [hours]" + \
    "\n" + cj.trailing_spaces(16, SMXCO, 3) + "    | SMXCO : Adjustment factor for maximum curve number S factor" + \
    "\n" + cj.trailing_spaces(16, FIXCO, 3) + "    | FIXCO : Nitrogen fixation coefficient" + \
    "\n" + cj.trailing_spaces(16, NFIXMX, 3) + "    | NFIXMX : Maximum daily-n fixation [kg/ha]" + \
    "\n" + cj.trailing_spaces(16, ANION_EXCL_BSN, 3) + "    | ANION_EXCL_BSN : Fraction of porosity from which anions are excluded" + \
    "\n" + cj.trailing_spaces(16, CH_ONCO_BSN, 3) + "    | CH_ONCO_BSN : Channel organic nitrogen concentration in basin [ppm]" + \
    "\n" + cj.trailing_spaces(16, CH_OPCO_BSN, 3) + "    | CH_OPCO_BSN : Channel organic phosphorus concentration in basin [ppm]" + \
    "\n" + cj.trailing_spaces(16, HLIFE_NGW_BSN, 3) + "    | HLIFE_NGW_BSN : Half-life of nitrogen in groundwater [days]" + \
    "\n" + cj.trailing_spaces(16, RCN_SUB_BSN, 3) + "    | RCN_SUB_BSN : Concentration of nitrate in precipitation [ppm]" + \
    "\n" + cj.trailing_spaces(16, BC1_BSN, 3) + "    | BC1_BSN : Rate constant for biological oxidation of NH3 [1/day]" + \
    "\n" + cj.trailing_spaces(16, BC2_BSN, 3) + "    | BC2_BSN : Rate constant for biological oxidation NO2 to NO3 [1/day]" + \
    "\n" + cj.trailing_spaces(16, BC3_BSN, 3) + "    | BC3_BSN : Rate constant for hydrolosis of organic nitrogen to ammonia [1/day]" + \
    "\n" + cj.trailing_spaces(16, BC4_BSN, 3) + "    | BC4_BSN : Rate constant for decay of organic phosphorus to dissolved phosphorus [1/day]" + \
    "\n" + cj.trailing_spaces(16, DECR_MIN, 3) + "    | DECR_MIN: Minimum daily residue decay" + \
    "\n" + cj.trailing_spaces(16, ICFAC, 3) + "    | ICFAC : C-factor calculation method" + \
    "\n" + cj.trailing_spaces(16, RSD_COVCO, 3) + "    | RSD_COVCO : Residue cover factor for computing fraction of cover" + \
    "\n" + cj.trailing_spaces(16, VCRIT, 3) + "    | VCRIT : Critical velocity" + \
    "\n" + cj.trailing_spaces(16, CSWAT, 0) + "    | CSWAT : Code for new carbon routines" + \
    "\n" + cj.trailing_spaces(16, RES_STLR_CO, 3) + "    | RES_STLR_CO : Reservoir sediment settling coefficient" + \
    "\n" + cj.trailing_spaces(16, BFLO_DIST, 3) + "    | BFLO_DIST 0-1 (1:profile of baseflow in a day follows rainfall pattern, 0:baseflow evenly distributed to each time step during a day" + \
    "\n" + cj.trailing_spaces(16, IUH, 0) + "    | IUH : Unit hydrograph method: 1=triangular UH, 2=gamma function UH" + \
    "\n" + cj.trailing_spaces(16, UHALPHA, 3) + "    | UHALPHA : alpha coefficient for gamma function unit hydrograph. Required if iuh=2 is selected" + \
    "\n" + "Land Use types in urban.dat that do not make runoff to urban BMPs:" + \
    "\n" + \
    "\n" + "Subdaily Erosion:" + \
    "\n" + cj.trailing_spaces(16, EROS_SPL, 3) + "    | EROS_SPL: The splash erosion coefficient ranges 0.9 - 3.1" + \
    "\n" + cj.trailing_spaces(16, RILL_MULT, 3) + "    | RILL_MULT: Multiplier to USLE_K for soil susceptible to rill erosion, ranges 0.5 - 2.0" + \
    "\n" + cj.trailing_spaces(16, EROS_EXPO, 3) + "    | EROS_EXPO: an exponent in the overland flow erosion equation, ranges 1.5 - 3.0" + \
    "\n" + cj.trailing_spaces(16, SUBD_CHSED, 3) + "    | SUBD_CHSED: 1=Brownlie(1981) model, 2=Yang(1973,1984) model" + \
    "\n" + cj.trailing_spaces(16, C_FACTOR, 3) + "    | C_FACTOR: Scaling parameter for Cover and management factor in ANSWERS erosion model" + \
    "\n" + cj.trailing_spaces(16, CH_D50, 1) + "    | CH_D50 : median particle diameter of channel bed [mm]" + \
    "\n" + cj.trailing_spaces(16, SIG_G, 3) + "    | SIG_G : geometric standard deviation of particle sizes" + \
    "\n" + cj.trailing_spaces(16, RE_BSN, 2) + "    | RE_BSN: Effective radius of drains" + \
    "\n" + cj.trailing_spaces(16, SDRAIN_BSN, 2) + "    | SDRAIN_BSN: Distance between two drain or tile tubes" + \
    "\n" + cj.trailing_spaces(16, DRAIN_CO_BSN, 2) + "    | DRAIN_CO_BSN: Drainage coefficient" + \
    "\n" + cj.trailing_spaces(16, PC_BSN, 3) + "    | PC_BSN: Pump capacity" + \
    "\n" + cj.trailing_spaces(16, LATKSATF_BSN, 2) + "    | LATKSATF_BSN: Multiplication factor to determine lateral ksat from SWAT ksat input value for HRU" + \
    "\n" + cj.trailing_spaces(16, ITDRN, 0) + "    | ITDRN: Tile drainage equations flag" + \
    "\n" + cj.trailing_spaces(16, IWTDN, 0) + "    | IWTDN: Water table depth algorithms flag" + \
    "\n" + cj.trailing_spaces(16, SOL_P_MODEL, 0) + "    | SOL_P_MODEL: if = 1, use new soil P model" + \
    "\n" + cj.trailing_spaces(16, IABSTR, 2) + "    | IABSTR: Initial abstraction on impervious cover (mm)" + \
    "\n" + cj.trailing_spaces(16, IATMODEP, 0) + "    | IATMODEP: 0 = average annual inputs 1 = monthly inputs" + \
    "\n" + cj.trailing_spaces(16, R2ADJ_BSN, 0) + "    | R2ADJ_BSN: basinwide retention parm adjustment factor" + \
    "\n" + cj.trailing_spaces(16, SSTMAXD_BSN, 0) + "    | SSTMAXD_BSN: basinwide retention parm adjustment factor" + \
    "\n" + cj.trailing_spaces(16, ISMAX, 0) + "    | ISMAX: max depressional storage code" + \
    "\n" + cj.trailing_spaces(16, IROUTUNIT, 0) + "    | IROUTUNIT:" + \
    "\n"


fileName = "basins.bsn"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, bsn_file)
#print fileName

