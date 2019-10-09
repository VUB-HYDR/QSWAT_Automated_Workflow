import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys, os
# from celrayfunctions import read_from, write_to

def single_spaces(string_,  remove_enter = True):
    str_ = string_
    for index in range(0, 20):
        str_ = str_.replace("  ", " ")
    if remove_enter:
        str_ = str_.replace("\n", "")
        str_ = str_.replace("\r", "")
    return str_

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
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close
    if report:
        print('\n\t> saved ' + os.path.basename(filename))

project_dir = sys.argv[1]
output_level = sys.argv[2]
variable = sys.argv[3]
years = sys.argv[4:]


txtinout_dir = os.path.join(project_dir, "Scenarios/Default/TxtInOut")
output_directory = os.path.join(project_dir, "Figures")

print("> creating figures:")
# print(txtinout_dir)
# print(output_level)
# print(years)

if not os.path.isdir(output_directory):
    os.makedirs(output_directory)

subbasins = {}

class object_result:
    def __init__(self):
        self.precip = None
        self.pet = None
        self.et = None
        self.surq = None
        self.perc = None
        self.gw = None
        self.wyld = None
if output_level == "sub":
    subbasin_results = read_from(os.path.join(txtinout_dir, "output.sub"))[9:]
else:
    print("currently only figures at subbasin level are supported")
    sys.exit()

for line in subbasin_results:
    if int(single_spaces(line).split(" ")[3].split(".")[0]) > 1000:
        if not single_spaces(line).split(" ")[3].split(".")[0] in subbasins: 
            subbasins[single_spaces(line).split(" ")[3].split(".")[0]] = {}
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]] = object_result()
        

        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].precip = float(single_spaces(line).split(" ")[4])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].pet = float(single_spaces(line).split(" ")[6])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].et = float(single_spaces(line).split(" ")[7])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].perc = float(single_spaces(line).split(" ")[9])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].surq = float(single_spaces(line).split(" ")[10])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].gw = float(single_spaces(line).split(" ")[11])
        subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]].wyld = float(single_spaces(line).split(" ")[12])

        # print(subbasins[single_spaces(line).split(" ")[3].split(".")[0]])
        # print(vars(subbasins[single_spaces(line).split(" ")[3].split(".")[0]][single_spaces(line).split(" ")[1]]))
        # print("")

if output_level == "sub":
    subs_shapefile_fn = os.path.join(project_dir, "Watershed/Shapes/subs1.shp")
else:
    print("currently only figures at subbasin level are supported")
    sys.exit()


subs_shapefile_gpd = gp.read_file(subs_shapefile_fn)
initial_crs = subs_shapefile_gpd.crs

yearly_gpd_df = {}

variables = ['Precipitation', 'PET', 'ET', 'Perc', 'SURQ', 'GW', 'WYLD']

for year in subbasins:
    if not year in yearly_gpd_df:
        yearly_gpd_df[year] = None

    new_dataframe = pd.DataFrame(columns=['Subbasin', 'Precipitation', 'PET', 'ET', 'Perc', 'SURQ', 'GW', 'WYLD', 'geometry'])
    for index, row  in subs_shapefile_gpd.iterrows():
        new_dataframe.loc[row.Subbasin - 1] = [
                row.Subbasin,
                subbasins[year]["{0}".format(row.Subbasin)].precip,
                subbasins[year]["{0}".format(row.Subbasin)].pet,
                subbasins[year]["{0}".format(row.Subbasin)].et,
                subbasins[year]["{0}".format(row.Subbasin)].perc,
                subbasins[year]["{0}".format(row.Subbasin)].surq,
                subbasins[year]["{0}".format(row.Subbasin)].gw,
                subbasins[year]["{0}".format(row.Subbasin)].wyld,
                row.geometry,
            ]

    yearly_gpd_df[year] = gp.GeoDataFrame(new_dataframe, crs = initial_crs, geometry="geometry")

    new_dataframe = None

for year in yearly_gpd_df:
    if not year in years:
        continue

    for variable in variables:
        yearly_gpd_df[year] = yearly_gpd_df[year].to_crs(epsg=4326)
        # yearly_gpd_df[year].plot()
        fig, ax = plt.subplots(1, figsize = (10, 6))
        # ax.axis("off")
        ax.set_title("{var} in {yr}".format(var = variable, yr = year), fontdict=   {'fontsize': '12', 'fontweight' : '3'})
        yearly_gpd_df[year].plot(ax = ax, column=variable, cmap="Blues",    linewidth=0.8, edgecolor='0.8', legend = True)

        print("\t - {1}_{0}.png".format(year,   variable))
        fig.savefig(os.path.join(output_directory, "{1}_{0}.png".format(year,   variable)))
        plt.close(fig)
