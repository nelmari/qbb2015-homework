#!/usr/bin/env python

import numpy as np
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import sys

print "\n VENN DIAGRAM "

""" Define the functions """
def arrays_from_len_file (file_name):
    arrays ={}
    for line in open (file_name):  # We opened the file to read line by line
        fields = line.split() # We split the lines in columns  
        name = fields [0] 
        size = int( fields[1] ) 
        arrays[name] = np.zeros( size, dtype = bool )
    return arrays
        
def set_bits_from_file (arrays, file_name):
    for line in open(file_name):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int (fields[1])
        end = int (fields[2])
        arrays [chrom][start:end] = 1
        
"""Implementation of functions and calculation of overlapping"""
# Making the arrays and initialice with 0
ARRAY_C = arrays_from_len_file (sys.argv[1]) # Array of protein 1 
ARRAY_B = arrays_from_len_file (sys.argv[1]) # Array of protein 2 
ARRAY_S = arrays_from_len_file (sys.argv[1]) # Array of protein 3

"""Create an array with the region for each protein"""
set_bits_from_file (ARRAY_C, sys.argv[2]) 
set_bits_from_file (ARRAY_B, sys.argv[3])
set_bits_from_file (ARRAY_S, sys.argv[4])

dic_venn = {"S": 0, "B": 0, "C": 0, "SB" : 0, "BC" : 0, "SC": 0, "SBC": 0} 

Tot_list = {}

print dic_venn

count =0

for REF_file in sys.argv[2:]:
     if REF_file not in Tot_list:
         Tot_list[REF_file] = 0
     file = open(REF_file)
     
     print REF_file, "\n"
     
     
     for line in file:
         Tot_list[REF_file] += 1
         fields = line.split()   
         chrom = fields[0]
         start = int (fields[1])
         end = int (fields[2])
         SliceS = ARRAY_S[chrom][start:end]
         SliceB = ARRAY_B[chrom][start:end]
         SliceC = ARRAY_C[chrom][start:end]
         SS = SliceS.any()
         SB = SliceB.any()
         SC = SliceC.any()
         if SC == True and SB == False and SS == False:       
             dic_venn ["C"] += SC
         elif SC == True and SB == True and SS == False:
             dic_venn ["BC"] += SC
         elif SC == True and SB == False and SS == True:
             dic_venn ["SC"] += SC
         elif SC == False and SB == True and SS == True:
             dic_venn ["SB"] += SB 
         elif SC == False and SB == False and SS == True:
             dic_venn ["S"] += SS
         elif SC == False and SB == True and SS == False:
             dic_venn ["B"] += SB 
         elif SC == True and SB == True and SS == True:
             dic_venn["SBC"] +=SC          
         else:
             print "ERROR"
         

print dic_venn
print count
print Tot_list
print dic_venn["C"],dic_venn["BC"], dic_venn["SC"], dic_venn["SBC"]

""" #Plotting the results 
""" 
plt.figure()
plt.title("Venn Diagram ")
My_venn = venn3(subsets = (dic_venn["S"],dic_venn["B"],dic_venn["SB"],dic_venn["C"],dic_venn["SC"],dic_venn["BC"],dic_venn["SBC"] ), set_labels = ("SuHW","BEAF", "CTCF"))   

plt.savefig("Venn2.png")
