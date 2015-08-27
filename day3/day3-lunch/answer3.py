#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy import stats

table = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM =[] 

for value in table["FPKM"]:
    if np.log(value) > 0.0 :
        FPKM.append(np.log(value))
    else:
        pass

#gaussian_kde object
density = gaussian_kde(FPKM)
print density.d

#numpy darray
denP = density.evaluate(FPKM)

plt.figure()
# plot histgram of sample
#plt.hist(FPKM, bins=20, color = "w")

# plot estimated density
plt.plot(FPKM, denP, label='kde', color= "c")
plt.title('Kernel Density Estimation')
plt.legend()
plt.xlabel("log of FPKM values")
#plt.ylabel("Abundance in SRR0272893")

plt.savefig("density.png")
   
print "0"