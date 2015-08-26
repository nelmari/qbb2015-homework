#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

file = open(filename)
count =0
flag = False
x=0

num_lines = sum(1 for line in file)

for line in file:
    if "t_id" in line:
        df1 = pd.DataFrame(columns=(line.split()))
        x +=1
    else:
        fields = line.split()
        FPKM = float(fields[11])
        if FPKM == 0:
            x+=1
        elif flag == False:
            df2= pd.DataFrame(line.split())
            flag = True
            result =df1.append(df2)
            print result
            x += 1
        else: 
            if x < = num_lines
            df3 = pd.DataFrame(line.split())
            x+=1
            
        #TOTAL = result.append(df3)
            

#print TOTAL.shape

###Make a boxplot of the top 1/3rd, middle 1/3rd, and bottom third FPKM values in SRR072893 