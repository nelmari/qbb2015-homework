#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)
count =0

for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        column_loc = fields[2]
        if count < 10:
            print column_loc
            count += 1
        else:
            break
