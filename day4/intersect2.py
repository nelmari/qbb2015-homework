#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys

import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
suhw.set_bits_from_file( sys.argv[4] )

C_and_B = ctcf.union (beaf)
B_and_C = beaf.union (ctcf)
print C_and_B

ctcf.Create_touple(sys.argv[2])
