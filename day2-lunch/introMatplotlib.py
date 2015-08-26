#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header = None)

df.columns = ["chromosome","database","type","start","end","score", "strand", "frame", "attributes"]

# roi = df["chromosome"].str.contains("2L")
# print df[roi].shape
# plt.figure()
# plt.plot(df[roi]["start"]) #Y axis position along the chromosome (its start position) and X axis is row number
# plt.savefig("chr2L.png")

for chromosome in ("2L","2R","Y"):
    roi = df["chromosome"].str.contains(chromosome)
    plt.figure()
    plt.title(chromosome)
    plt.plot(df[roi]["start"])
    plt.ylabel("start position")
    plt.xlabel("gene") 
    plt.savefig("starts"+chromosome+ ".png")