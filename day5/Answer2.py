#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

file = open (sys.argv[1])

LIST = []

for line in file:
    if "Nu" in line:
        pass
    elif "  N" in line:
        fields = line.split()
        scores = float(fields [2])
        e_val = float(fields [3])
        LIST.append((scores,e_val))
    else:
        pass

SCORES = [x[0] for x in LIST]  
E_VAL = [x[1] for x in LIST]

plt.figure()
plt.plot(E_VAL, SCORES, 'o')
plt.title("Scatter")
plt.savefig("Scatter.png")

plt.figure()
plt.title("Scores")
plt.axis([30, 2000, 0, 8200])
plt.hist(SCORES , bins = 30)
plt.xlabel("Score of alignment")
plt.savefig("Scores_hist.png")

plt.figure()
plt.title("e values")
plt.hist(E_VAL , bins = 30)
plt.xlabel("e values of alignment")
plt.savefig("Eval_hist.png")      
    