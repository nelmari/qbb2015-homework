#!/usr/bin/env python

""" 
This script will count kmers in a FASTA file
"""

import sys
from fasta import FASTAreader
reader = FASTAreader (sys.stdin)

k = 11

counts = {}

for identity, SEQUENCE in reader:
    for i in range (0, len( SEQUENCE) - k ):
        kmer = SEQUENCE [i : i+k]
        if kmer not in counts:
            counts [kmer] = [(identity,i)]
        else:
            counts [kmer].append (i) 
           
query = sys.argv [1]

for i in range (0, len(query) - k):
    kmer = query[i : i+k]
    matches = counts [kmer]
    for pos in matches:
        print i, pos, identity
    