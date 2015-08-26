#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

file = open(filename)
count =0

for line in file:
    if "t_id" in line:
        df1 = pd.DataFrame(columns=(line.split()))
    else:
        fields = line.split()
        FPKM = float(fields[11])
        if FPKM == 0.0:
            pass    
        else:
            df_temp = pd.DataFrame(fields)
            df1 = df1.append(df_temp)


 
n= len(df1.index)
print n
n1= int(1/3*n)
n2= int (2/3*n)

bottom= df1["FPKM"][0:n1]
middle = df1["FPKM"][n1:n2]
top= df1["FPKM"][n2:]

plt.figure();
plt.title("Boxplot for FPKM in SRR072893")           
plt.boxplot([top, middle, bottom])
plt.ylabel("FPKM")
plt.xlabel("SRR072893")
plt.savefig("answer4.png")
