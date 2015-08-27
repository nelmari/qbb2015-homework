#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


table = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM =[] 

#FPKM builds on the assumption that the number of reads that are generated from an isoform is proportional to the isoform abundance as well as the isoform length.
print table.columns.values
for value in table["FPKM"]:
    if np.log2(value) > 0.0 :
        FPKM.append(np.log(value))
    else:
        pass

print FPKM

#M = R - G
#A = 0.5*(R + G) ##Average intensity =FPKM???



