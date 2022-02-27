"""Import_packs"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sas

###Import_Data>>>>>>>>>>>>>###################################################################################################################
""""Import_Data"""
data_wine_red = pd.read_csv("E:\Statistics Department\Data scenice\Data Base\wine-quality\winequality-red.csv", sep=";")
data_wine_white = pd.read_csv("E:\Statistics Department\Data scenice\Data Base\wine-quality\winequality-white.csv",
                              sep=";")
dataFrame_wine_red = pd.DataFrame(data_wine_red)
dataFrame_wine_white = pd.DataFrame(data_wine_white)
##Set option to max_rows & max_columns,,,,,,#########################################################################
""""Set option to max_rows & max_column"""
pd.set_option('display.max_rows', dataFrame_wine_red.shape[0] + 1)
pd.set_option('display.max_columns', dataFrame_wine_red.shape[0] + 1)
pd.set_option('display.max_rows', dataFrame_wine_white.shape[0] + 1)
pd.set_option('display.max_columns', dataFrame_wine_white.shape[0] + 1)

##Data_Quality,,,,,,,################################################################################################
"""Data_Quality
print('*' * 80)
print("***********dataFrame_wine_red*****************")
dataFrame_wine_red.info()
print('*' * 80)
print("************dataFrame_wine_White**************")
dataFrame_wine_white.info()
print('*' * 80)
print("************data_Check_duplicates_wine_White**************")

check_red = dataFrame_wine_red.duplicated()
check_white = dataFrame_wine_white.duplicated()
count_white = 0
count_red = 0
for white in check_white :
    if white is True :
        count_white += 1
for red in check_red:
    if red is True:
        count_red += 1
print("duplicates_wine_White= ",count_white,",,,","unique values_White=",4898-count_white,"\n","duplicates_wine_Red= ",count_red,",,,","unique values_Red=",1599-count_red)
print('*' * 80)
unique_valeus_red=dataFrame_wine_white["quality"].unique()
print(unique_valeus_red)
"""
##Data_Describe,,,,,,################################################################################################
"""Data_Describe
d_d_red = dataFrame_wine_red.describe()
d_d_white = dataFrame_wine_white.describe()
print("White_Wine", "\n", d_d_white, "\n", "*" * 80, "\n", "Red_Wine", "\n", d_d_red)
print('*' * 80)
"""
###New_Data<<<<<<<<<#################################################################################################
"""" New_Data 
dataFrame_wine_white["color"] = "white"
dataFrame_wine_red["color"] = "red"
pd.concat([dataFrame_wine_white,dataFrame_wine_red]).to_csv("new_data_from_python",index=False)
"""
# Read new Data
new_data = pd.read_csv("E:\Statistics Department\Data scenice\Data Base\wine-quality\data_from_python.csv")
#
# pd.set_option('display.max_rows', new_data.shape[0] + 1)
# pd.set_option('display.max_columns', new_data.shape[0] + 1)

######################################################################################################################
# des_data=new_data.describe()
###'acidity_levels',,,,,,,,############################################################################################

conditions = [(new_data["pH"] < 3.110), (new_data["pH"] < 3.21), (new_data["pH"] < 3.32), (new_data["pH"] >= 3.32)]
values = ["High", "Moderately", "Medium", "Low"]
new_data['acidity_levels'] = np.select(conditions, values)
mean_quality = new_data.groupby('acidity_levels').mean().quality
# print(mean_quality)

######better ratings_alcohol<<<<<<<<<<################################################################################################################
"""
Do wines with higher alcoholic content receive better ratings?
To answer this question, use query to create two groups of wine samples:

Low alcohol (samples with an alcohol content less than the median)
High alcohol (samples with an alcohol content greater than or equal to the median)
Then, find the mean quality rating of each group.
#############
conditions_2 = [new_data["alcohol"] >= new_data["alcohol"].median(), new_data["alcohol"] < new_data["alcohol"].median()]
values_2 = ["High alcohol", "Low alcohol"]
new_data["better ratings_alcohol"] = np.select(conditions_2, values_2)
mean_quality_2 = new_data.groupby("better ratings_alcohol").mean().quality
"""
###better ratings_residual sugar###################################################################################################################
"""
Q2: Do sweeter wines (more residual sugar) receive better ratings?
Similarly, use the median to split the samples into two groups by residual sugar and find the mean quality rating of each group.

condition_3 = [new_data["residual sugar"] >= new_data["residual sugar"].median(), new_data["residual sugar"] < new_data["residual sugar"].median()]
values_3=["sweeter wines", "Not_sweeter wines"]
new_data['sweeter wines'] = np.select(condition_3, values_3)
mean_quality_sweeter_wines = new_data.groupby("sweeter wines").mean().quality
print(mean_quality_sweeter_wines)
"""
######################################################################################################################
''''
color_plot = ['red', 'black']
color_mean = new_data.groupby("color").mean().quality
color_mean.plot(kind="bar", color=color_plot, alpha=0.7)
plt.xlabel("color_plot", fontsize=18)
plt.ylabel("quality", fontsize=18)
plt.show()
'''
color_plot = ['red', 'black']
count_acidity_levels_by_color = new_data.groupby(["acidity_levels", "color"])["color"].count()
count_acidity_levels_by_color.plot(kind="bar", figsize=(10, 10), color=color_plot)
plt.show()
print(count_acidity_levels_by_color)
