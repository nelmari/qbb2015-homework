#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)

alignments_per_chr = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X" :0}
        
for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        column_loc = fields[2]
        if column_loc in ("2L", "2R", "3L", "3R", "4", "X"):
            alignments_per_chr[column_loc] += 1 ;
        else:
            pass

for key, value in alignments_per_chr.iteritems():
    print key, value
            

   
    
    
    
