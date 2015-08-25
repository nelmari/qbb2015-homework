#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open (filename)

for line in f:
    if "H0" in line:
        print line,