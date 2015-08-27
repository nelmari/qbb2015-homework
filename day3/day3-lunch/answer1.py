#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

Sxl_f = []
Sxl_m = []
Sxl_r = []

for sample in metadata [metadata["sex"] == "female"]["sample"]:
    df_f = pd.read_table ("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df_f["t_name"].str.contains("FBtr0331261")
    Sxl_f.append(df_f[roi]["FPKM"].values)
    
for sample in metadata [metadata["sex"] == "male"]["sample"]:
    df_m = pd.read_table ("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi_2= df_m["t_name"].str.contains("FBtr0331261")
    Sxl_m.append(df_m[roi_2]["FPKM"].values)
   
replicates = pd.read_csv("/Users/cmdb/qbb2015/rawdata/replicates.csv")

for columns in replicates["sample"]:
    df_r = pd.read_table ("~/qbb2015/stringtie/"+columns+"/t_data.ctab")
    roi_r = df_r["t_name"].str.contains("FBtr0331261")
    Sxl_r.append(df_r[roi_r]["FPKM"].values)

plt. figure
plt.plot(Sxl_f, label ="Female", color = "m")
plt.plot(Sxl_m, label= "Male", color = "r")
plt.plot([4,5,6,7,4,5,6,7],Sxl_r, 'o', label ="Replicates", color = "c")
plt.legend()
plt.axis([0,8,0,200])
plt.xlabel("Developmental Stage")

plt.ylabel("FPKM values")
plt.savefig("time_course_fm2.png")
