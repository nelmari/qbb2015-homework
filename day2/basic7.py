#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)
count = 0

for line in f:
    if line.startswith("@"):
        pass
    else:
        fields = line.split()
        if "2L" in fields[2] and int(fields[3])<20001 and int(fields[3])>= 10000:
            count += 1

print count