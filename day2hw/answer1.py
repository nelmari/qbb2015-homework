#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

location = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

# DataFrame is set as the file in the "location"
df = pd.read_table(location, comment='#', header = None)

# The name of the columns is established for the Data Frame to better access 
df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]


count = 0

# The elements for the column "attributes" which contain "Sxl" are set to True,
# others False
roi = df["attributes"].str.contains("Sxl")

plt.figure()

#The title of the plot is set to "Sxl"
plt.title("Sxl")

#The rows in df for which series roi are true, are selected to create a plot with the values in "start"
plt.plot(df[roi]["start"])

#The x and y labels are established
plt.ylabel("start position")
plt.xlabel("gene")

#The figure is saver with the name betweeen parentesis 
plt.savefig("answer1.png")



    
        

