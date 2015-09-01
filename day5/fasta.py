
class FASTAreader (object):
    def __init__ (self, file_name) :
        self.file = file_name
        self.last_ident = None
    
    def next (self):
        if self.last_ident == None:
            line = self.file.readline()
            # Verify that the file is in fasta format
            assert line.startswith(">"), "Not valid FASTA"
            identity = line [1:].rstrip("\r\n") # Reads spaces
        
        else:
            identity = self.last_ident
        
        sequences = []
        while True:
            line = self.file.readline()
            if not line:  # Equivalent to say: if line == "":  
                break
            elif line.startswith(">"):
                self.last_ident = line [1:].rstrip("\r\n") # Reads spaces
                break
            else:
                sequences.append ( line.strip() )
        
        if len (sequences) == 0:
            raise StopIteration
        
        SEQUENCE = "".join(sequences)
        
        return identity, SEQUENCE
                
    def __iter__ (self):
        return self