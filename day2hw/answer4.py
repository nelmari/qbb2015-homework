#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

file = open(filename)
count =0
flag = False


for line in file:
    if "t_id" in line:
        df1 = pd.DataFrame(columns=(line.split()))
    else:
        fields = line.split()
        FPKM = float(fields[11])
        if FPKM == 0:
            pass
            
        elif flag == False:
            df2= pd.DataFrame(fields)
            flag = True
            result = df1.append(df2)
            
        else:
            result = result.append(pd.DataFrame(fields))

print result.shape            

plt.figure();
plt.title("Boxplot for FPKM")
           
plt.plot(result,"kind"==box)

plt.savefig("Boxplot.png")


###Make a boxplot of the top 1/3rd, middle 1/3rd, and bottom third FPKM values in SRR072893 