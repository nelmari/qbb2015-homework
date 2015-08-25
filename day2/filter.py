#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab" # Absolute address of the file to be opened
f = open(filename) # Opens the file - READ MODE


#for line in f: # When you do a for loop on a file is always going line by line
#    fields = line.split() # Divides in columns the rows on the file
#    if "tRNA" in fields[9]: # Select the column in which we want the keyword to be found
#        print line , # Displays the line only if the keyword was present in the selected column

count = 0

for count, data in enumerate(f): # Enumerate will make a touple with count and lines which will increase  
    if count <= 10: # If lines with an index from 0-10 it will not do anything
        pass ;
    elif count <= 15: # If lines have an index equal or below 15 (greater than 10), the line will be displayed 
        print data,
    else: # Lines 15 and over won't do anything
        break
        
    