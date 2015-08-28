#!/usr/bin/env python

print "\n VENN DIAGRAM "

import numpy as np
from matplotlib_venn import venn2 
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import sys

""" Define the functions """
def arrays_from_len_file (file_name):
    arrays ={}
    for line in open (file_name):  # We opened the file to read line by line
        fields = line.split() # We split the lines in columns  
        name = fields [0] 
        size = int( fields[1] ) 
        arrays[name] = np.zeros( size, dtype = bool )
    return arrays
        
def set_bits_from_file (arrays, file_name2):
    for line in open(file_name2):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int (fields[1])
        end = int (fields[2])
        arrays [chrom][start:end] = 1

def ALLOVER (file_name, array, array2):
    total = 0
    both_overlap = 0
    overlap_1 = 0
    overlap_2 = 0
    for line in open(file_name):
        fields = line.split()   
        chrom = fields[0]
        start = int (fields[1])
        end = int (fields[2])
        sl = array[chrom][start:end]
        sl2 = array2[chrom][start:end]
        total +=1
        overlap_1 += sl.any() 
        overlap_2 += sl2.any()
        if sl.any() == sl2.any():
            both_overlap += sl.any()
            
    return total, both_overlap, overlap_1, overlap_2

"""Implementation of functions and calculation of overlapping"""
# Making the arrays and initialice with 0
ARRAY_P1 = arrays_from_len_file (sys.argv[1]) # Array of protein 1 
ARRAY_P2 = arrays_from_len_file (sys.argv[1]) # Array of protein 2 
ARRAY_P3 = arrays_from_len_file (sys.argv[1]) # Array of protein 3

"""Create an array with the region for each protein"""
set_bits_from_file (ARRAY_P1, sys.argv[2]) 
set_bits_from_file (ARRAY_P2, sys.argv[3])
set_bits_from_file (ARRAY_P3, sys.argv[4])

""" Comparison between two proteins """    
CTCF_t, C_all , CandB, CandS = ALLOVER (sys.argv[2], ARRAY_P2, ARRAY_P3) # File protein1 / array protein2, array protein3
BEAF_t, B_all, BandC, BandS = ALLOVER (sys.argv[3], ARRAY_P1, ARRAY_P3) # File protein2 / array protein1, array protein3
SuHW_t, S_all, SandC, SandB = ALLOVER (sys.argv[4], ARRAY_P1, ARRAY_P2) # File protein3 / array protein1, array protein2

print " Ref : Tot  CTCF BEAF SuHW"
print " CTCF " , C_all, CTCF_t, CandB,  CandS
print " BEAF " , B_all, BandC,  BEAF_t, BandS
print " SuHW " , S_all, SandC,  SandB,  SuHW_t
print "\n"

SBC = (C_all + B_all + S_all)/3

SB = (BandS + SandB)/2 - SBC
BC = (BandC + CandB)/2 - SBC
SC = (SandC + CandS)/2 - SBC

S = SuHW_t - (SB + SC + SBC) 
B = BEAF_t - (SB + BC + SBC)
C = CTCF_t - (SC + BC + SBC) 

""" Plotting the results """ 
plt.figure()
plt.title("Venn Diagram- version1")
My_venn = venn3(subsets = (S, B, SB, C,SC, BC, SBC ), set_labels = ("SuHW","BEAF", "CTCF"))   

plt.savefig("Venn.png")
