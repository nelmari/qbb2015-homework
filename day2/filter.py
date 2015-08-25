#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab" # Absolute address of the file to be opened
f = open(filename) # Opens the file - READ MODE


for line in f: # When you do a for loop on a file is always going line by line
    fields = line.split() # Divides in columns the rows on the file
    if "tRNA" in fields[9]: # Select the column in which we want the keyword to be found
        print line , # Displays the line only if the keyword was present in the selected column