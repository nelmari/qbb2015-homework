#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

location = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(location, comment='#', header = None)

df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]

count =0

for line in df["attributes"]:
    if "Sxl" not in line:
        pass
    else:
        roi = df["attributes"].str.contains("Sxl")
        count+=1

plt.figure()

plt.title("Sxl transcript")            
plt.plot(df[roi]["start"])
plt.ylabel("Start position")
plt.xlabel("Gene") 
plt.savefig("answer2.png")
            


print count
    
