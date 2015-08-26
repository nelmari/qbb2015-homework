#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

location = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(location, comment='#', header = None)

df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]

count = 0

roi = df["attributes"].str.contains("Sxl")
plt.figure()
plt.title("Sxl")
plt.plot(df[roi]["start"])
plt.ylabel("start position")
plt.xlabel("gene") 
plt.savefig("Sxl.png")


print count
    
        

