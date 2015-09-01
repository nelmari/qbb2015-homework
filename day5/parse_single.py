#!/usr/bin/env python

"""
This script will parse a single FASTA record from stdin and print it.
"""

import sys
from fasta import FASTAreader
 
reader = FASTAreader( sys.stdin )

#while 1:    
 #   print reader.Next()
    
for i, (identity, seq ) in enumerate(reader):
    print i, identity, seq
   


