#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
Sxl = []

for sample in metadata [metadata["sex"] == "female"]["sample"]:
    dataframe = pd.read_table ("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = dataframe["t_name"].str.contains("FBtr0331261")
    Sxl.append(dataframe[roi]["FPKM"].values)
print len(Sxl)    
#plt. figure
#plt.plot(Sxl)
#plt.savefig("Timecourse.png")


# df_893 = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
# df_915 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

#chr_dict = {}

#for i, line in df_893.iterrows():
 #   if line["chr"] in ["2L", "2R", "3L", "3R", "X","Y"]:
  #      if line["chr"] not in chr_dict:
   #         chr_dict[line["chr"]] = 1
    #    else:
     #       chr_dict[line["chr"]] += 1
            
        
#print range(len(chr_dict))

#plt.figure()
#plt.bar(range(len(chr_dict)), chr_dict.values())
#plt.savefig("barplot.png")
#plt.scatter(df_893["FPKM"],df_915["FPKM"])
#plt.xlabel(" 893 - male 10 ")
#plt.ylabel(" 915 - female 4D ")
#plt.savefig("Scatt.png")