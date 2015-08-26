#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


table = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM =[] 

for value in table["FPKM"]:
    if value != 0:
        FPKM.append(table["FPKM"])
    else:
        pass

l_FPKM =[]

for value in FPKM:
    l_FPKM.append(np.log(value))

hist, bin_edges = np.histogram(l_FPKM)

print hist
print bin_edges
#plt.bar(bin_edges[:-1], hist, width = 1)
#plt.xlim(min(bin_edges), max(bin_edges))
#plt.savefig("histogram.png")


