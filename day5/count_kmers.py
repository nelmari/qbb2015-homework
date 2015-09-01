#!/usr/bin/env python

import sys

""" 
This script will count kmers in a FASTA file
"""

# Use the following to run:
# cat subset.fa | ./count_kmers.py ./fasta.py

from fasta import FASTAreader

reader = FASTAreader (sys.stdin)

counts = {}

k = 11

for identity, SEQUENCE in reader:
    for i in range (0, len( SEQUENCE) - k ):
        kmer = SEQUENCE [i : i+k]
        if kmer not in counts:
            counts [kmer] = 1
        else:
            counts [kmer] += 1
            
for key in sorted ( counts, key=counts.get ):
    print key, counts[key]
        
