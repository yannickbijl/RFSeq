class ESC_RFSeq():
    def __init__(self, seq):
        self.fseq = seq
        self.cseq = self.make_complement(self.fseq)
        self.rf1, self.rf2, self.rf3 = self.make_reading_frames(self.fseq)
        self.rf4, self.rf5, self.rf6 = self.make_reading_frames(self.cseq)
        
    def make_complement(self, seq):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "".join(complement.get(base, base) for base in reversed(seq))
    
    def make_reading_frames(self, seq):
        if len(seq) % 3 == 0:
            return seq, seq[1:-2], seq[2:-1]
        elif len(seq) % 3 == 1:
            return seq[:-1], seq[1:], seq[2:-2]
        elif len(seq) % 3 == 2:
            return seq[:-2], seq[1:-1], seq[2:]
    
    def get_rf1(self):
        return self.rf1
    
    def get_rf2(self):
        return self.rf2
    
    def get_rf3(self):
        return self.rf3
   
    def get_rf4(self):
        return self.rf4
    
    def get_rf5(self):
        return self.rf5

    def get_rf6(self):
        return self.rf6
    
    def get_fseq(self):
        return self.fseq

    def get_cseq(self):
        return self.cseq