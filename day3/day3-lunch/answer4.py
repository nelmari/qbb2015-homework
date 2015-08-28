#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


table = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
table2 = pd.read_table("~/qbb2015/stringtie/SRR072895/t_data.ctab")

#FPKM builds on the assumption that the number of reads that are generated from an isoform is proportional to the isoform abundance as well as the isoform length.

FP93 = table["FPKM"] > 0
FP95 = table2["FPKM"] > 0

simplified = FP93 & FP95 

FPKM_893 = table[simplified]["FPKM"] # R
FPKM_895 = table2[simplified]["FPKM"] # G

R = np.log2(FPKM_893)
G = np.log2(FPKM_895)
         
M = R - G
A = 0.5*(R + G) 

plt.figure()
plt.plot(A, M, 'o', label ="MA PLOT", color = "c")
plt.legend()
plt.title("MA Plot SRR072893 and SRR072895")

plt.savefig("MA_plot.png")



