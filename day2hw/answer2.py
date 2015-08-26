#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

location = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(location, comment='#', header = None)

df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]

count =0

roi= df["attributes"].str.contains("Sxl")
roi2 = df["type"].str.contains("transcript")

print df[roi].shape

#for count in df[]: 
 #   if roi[count] == roi2[count]:
  #      print roi[count]
   # count += 1;
    #else:
     #   print False
     #   count +=1
 
        
print count
    
