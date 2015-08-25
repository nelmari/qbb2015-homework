#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header = None)

# print df

# print df.head()

# print df.describe()
# print df.info()

# print "\n This happens with [1:5]\n"
# print df[1:5]
# print "\n This happens with [0:5]\n"
# print df[0:5]

# To show rows 10-15 inclusive
# print df[9:15]

# Shows rows 20 to 25
# print df [19:25]

# print df.info()
df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]

# print df.info()

# print df.sort("type", ascending =False)

# print df["chromosome"] #Prints column called chromosome

# print df[["chromosome","start","end"]]

# print df["start"][9:15]

# print df.shape #Gives the size of the data frame
df2 = df["start"]
# print df2.shape

# df2.to_csv("startcolumn.txt")

df2.to_csv("startcolumn.txt", sep='\t', index=False)