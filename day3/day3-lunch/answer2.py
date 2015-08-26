#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


table = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM =[] 

for value in table["FPKM"]:
    if np.log(value) > 0.0 :
        FPKM.append(np.log(value))
    else:
        pass

print len(FPKM)

plt.figure()
plt.hist(FPKM)
plt.title("FPKM in SRR0272893")
plt.xlabel("log of FPKM values")
plt.ylabel("Abundance in SRR0272893")
plt.savefig("histogram.png")


