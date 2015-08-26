#!/usr/bin/env python

import pandas as pd

filename = "/Users/cmdb/qbb2015/rawdata/samples.csv"

count =0
df = pd.read_csv(filename)

for x in df["sample"]:
    temp_loc = "/Users/cmdb/qbb2015/stringtie/"+x+"/t_data.ctab"
    file = open (str(temp_loc))
    print x
    for line in file:
        if "FBtr0331261" in line:
            print line
            count+=1
        else:
            pass

print count

