#!/usr/bin/env python

"""
Count intersections of two BED files
"""

from __future__ import division

import sys
import numpy as np

def arrays_from_len_file (file_name):
    
    arrays ={}
    
    for line in open (file_name):  # We opened the file to read line by line
        fields = line.split() # We split the lines in columns  
        
        name = fields [0] 
        # We asign the first value (first column) in every column to a variable name
        
        size = int( fields[1] ) 
        # We asign the second value (second column) to a variable size which contain the size of each chromosome
        
        arrays[name] = np.zeros( size, dtype = bool )
        # We are building array rows with the size of each chromosome and making them by default zeros which represent False. 
        #The name of the chromosomes are established as keys 
        
    return arrays
        
def set_bits_from_file (arrays, file_name2):
    
    for line in open(file_name2):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int (fields[1])
        end = int (fields[2])
        
        arrays [chrom][start:end] = 1
        # We are using the array rows and using the chromosome names in the new file as keys.
        # We are setting the positions determined by end and starts and marking them with ones, which will substitute the zeros.
        

ARRAY = arrays_from_len_file (sys.argv[1])
# We are saving the array build in the function (which takes as input a file from the command line), in a global variable called arrays

set_bits_from_file (ARRAY,sys.argv[2])

#for key, value in arr.iteritems():
#    print key, type (value), value.shape  , np.sum(value)
    #To test this code until this point

total = 0

any_overlap = 0

all_overlap = 0

half_overlap = 0

for line in open(sys.argv[3]):
    fields = line.split()
    
    # Parse fields
    chrom = fields[0]
    start = int (fields[1])
    end = int (fields[2])
    
    # Get slice
    sl = ARRAY[chrom][start:end]
    
    # Aggregate
    total +=1
    any_overlap += sl.any() 
    #This function returns true if the callback function returns true for any array element; otherwise, false.
    
    all_overlap += sl.all()
    
    # 50% overlap
    half_overlap += (np.sum(sl)/ len (sl) > 0.5  )
    
    
    
print "Total: %d, Any overlap: %d, All overlap %d, Half overlapping %d " %(total, any_overlap, all_overlap, half_overlap)




