#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)
MAPQ_counter = 0
counter = 0 

for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        MAPQ_scores = fields[4]
        MAPQ_counter += int(MAPQ_scores)
        counter += 1
        
print MAPQ_counter/counter