import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None, touple=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        if touple is not None:
            t_list = touple    
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int(fields[1])
                arrays[name] = numpy.zeros( size, dtype=bool )
                t_list =[]
        self.arrays = arrays
        self.t_list = t_list

    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1
            
    def Create_touple (self, fname):
        for line in open( fname ):
            fields = line.split()
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.t_list.append ((chrom, start, end)) 
    
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        b_list = []
        for value in self.t_list:
            b_list.append(value)
        for val in other.t_list:
            if val not in b_list:
                b_list.append(val) 
        print len(self.t_list),len(other.t_list), len (b_list)
        return ChromosomeLocationBitArrays( dicts=rval, touple = b_list )
    
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval ) 
        
    def copy( self ):
        return ChromosomeLocationBitArrays( dicts = copy.deepcopy( self.arrays), touple = copy.deepcopy (self.t_list) )                     

    
