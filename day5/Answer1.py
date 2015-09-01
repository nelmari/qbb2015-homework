#!/usr/bin/env python

import sys

file = open (sys.argv[1])

dictionary = {}

for line in file:
    if line.startswith(">"):
        hit = line
    elif "Identities" in line:
        fields = line.split()
        identity = fields [2]
        gaps = fields [6]
        dictionary[hit]=(identity, gaps)
    else:
        pass

print dictionary 

         
        
        