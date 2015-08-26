#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab" # Absolute address of the file to be opened

import sys

#print sys.argv #Shows what I am opening 

#filename = sys.argv[1]
#f = open(filename) # Opens the file - READ MODE

f = sys.stdin

name_counts = {}
        
for line_count, data in enumerate (f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts [gene_name] = 1
    else:
        name_counts [gene_name] += 1

# Iterate key, value pairs         
for key, value in name_counts.iteritems():
    print key, value   