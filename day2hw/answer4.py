#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_csv(filename)

df.sort("type", ascending =False)
        
 
n= float(len(df1.index))

n1= int(0.33*n)
n2= int (0.66*n)
print n
print n1
print n2
#bottom= df1["FPKM"][0:n1]
#middle = df1["FPKM"][n1:n2]
#top= df1["FPKM"][n2:]

#plt.figure();
#plt.title("Boxplot for FPKM in SRR072893")           
#plt.boxplot([top, middle, bottom])
#plt.ylabel("FPKM")
#plt.xlabel("SRR072893")
#plt.savefig("answer4.png")
