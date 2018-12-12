import init_file as variables
import cj_function_lib as cj
from datetime import datetime

wwq_table = cj.extract_table_from_mdb(variables.ProjMDB, "wwq", variables.path + "\\wwq.tmp~")

wwq_params = wwq_table[0].split(",")
now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5.2"

# Parameters
OID = wwq_params[0].strip('"')
LAO = wwq_params[1].strip('"')
IGROPT = wwq_params[2].strip('"')
AI0 = wwq_params[3].strip('"')
AI1 = wwq_params[4].strip('"')
AI2 = wwq_params[5].strip('"')
AI3 = wwq_params[6].strip('"')
AI4 = wwq_params[7].strip('"')
AI5 = wwq_params[8].strip('"')
AI6 = wwq_params[9].strip('"')
MUMAX = wwq_params[10].strip('"')
RHOQ = wwq_params[11].strip('"')
TFACT = wwq_params[12].strip('"')
K_L = wwq_params[13].strip('"')
K_N = wwq_params[14].strip('"')
K_P = wwq_params[15].strip('"')
LAMBDA0 = wwq_params[16].strip('"')
LAMBDA1 = wwq_params[17].strip('"')
LAMBDA2 = wwq_params[18].strip('"')
P_N = wwq_params[19].strip('"')
CHLA_SUBCO = wwq_params[20].strip('"')

# Building String
wwq_file = "Watershed water quality file          .wwq file " + DateAndTime + " " + SWAT_Vers + \
    "\n" + cj.trailing_spaces(16, LAO, 0) + "    | LAO : Light averaging option" + \
    "\n" + cj.trailing_spaces(16, IGROPT, 0) + "    | IGROPT : Algal specific growth rate option" + \
    "\n" + cj.trailing_spaces(16, AI0, 3) + "    | AI0 : Ratio of chlorophyll-a to algal biomass [micro g-chla/mg algae]" + \
    "\n" + cj.trailing_spaces(16, AI1, 3) + "    | AI1 : Fraction of algal biomass that is nitrogen [mg N/mg alg]" + \
    "\n" + cj.trailing_spaces(16, AI2, 3) + "    | AI2 : Fraction of algal biomass that is phosphorus [mg P/mg alg]" + \
    "\n" + cj.trailing_spaces(16, AI3, 3) + "    | AI3 : The rate of oxygen production per unit of algal photosynthesis [mg O2/mg alg)]" + \
    "\n" + cj.trailing_spaces(16, AI4, 3) + "    | AI4 : The rate of oxygen uptake per unit of algal respiration [mg O2/mg alg)]" + \
    "\n" + cj.trailing_spaces(16, AI5, 3) + "    | AI5 : The rate of oxygen uptake per unit of NH3-N oxidation [mg O2/mg NH3-N]" + \
    "\n" + cj.trailing_spaces(16, AI6, 3) + "    | AI6 : The rate of oxygen uptake per unit of NO2-N oxidation [mg O2/mg NO2-N]" + \
    "\n" + cj.trailing_spaces(16, MUMAX, 3) + "    | MUMAX : Maximum specific algal growth rate at 20deg  C [day-1]" + \
    "\n" + cj.trailing_spaces(16, RHOQ, 3) + "    | RHOQ : Algal respiration rate at 20deg  C [day-1]" + \
    "\n" + cj.trailing_spaces(16, TFACT, 3) + "    | TFACT : Fraction of solar radiation computed in the temperature heat balance that is photosynthetically active" + \
    "\n" + cj.trailing_spaces(16, K_L, 3) + "    | K_L : Half-saturation coefficient for light [kJ/(m2deg min)]" + \
    "\n" + cj.trailing_spaces(16, K_N, 3) + "    | K_N : Michaelis-Menton half-saturation constant for nitrogen [mg N/lL]" + \
    "\n" + cj.trailing_spaces(16, K_P, 3) + "    | K_P : Michaelis-Menton half-saturation constant for phosphorus [mg P/l]" + \
    "\n" + cj.trailing_spaces(16, LAMBDA0, 3) + "    | LAMBDA0 : Non-algal portion of the light extinction coefficient [m-1]" + \
    "\n" + cj.trailing_spaces(16, LAMBDA1, 3) + "    | LAMBDA1 : Linear algal self-shading coefficient [m-1?(?g chla/l)-1)]" + \
    "\n" + cj.trailing_spaces(16, LAMBDA2, 3) + "    | LAMBDA2 : Nonlinear algal self-shading coefficient [m-1?(?g chla/l)-2]" + \
    "\n" + cj.trailing_spaces(16, P_N, 3) + "    | P_N : Algal preference factor for ammonia" + \
    "\n" + cj.trailing_spaces(16, CHLA_SUBCO, 3) + "    | CHLA_SUBCO : Regional adjustment on sub chla_a loading" + \
    "\n"

fileName = "basins.wwq"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, wwq_file)
#print fileName

