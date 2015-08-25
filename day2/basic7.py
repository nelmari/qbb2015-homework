#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)
count = 0

for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        if "2L" in fields[2] and fields[3] in range(10000,20001): 
             count += 1
        else:
            pass

print count