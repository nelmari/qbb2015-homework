#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)
count = 0

for line in f:
    if "NH:i:1" in line:
        count += 1 

print count,
        