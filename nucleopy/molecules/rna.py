"""
Creates an RNA object which contains a nucleotide sequence
"""
from nucleotide import Nucleotide


class RNA(Nucleotide):
    def __init__(self, sequence):
        """
        Creates an RNA object
        :param sequence: String sequence of nucleotides
        """
        Nucleotide.__init__(self, sequence)

        if 'A' not in self.seq or 'U' not in self.seq or 'G' not in self.seq or 'C' not in self.seq:
            raise ValueError("Not a valid RNA sequence")

    def __repr__(self):
        return self.seq

    #@classmethod
    def toDNA(self):
        """
        Converts RNA to DNA
        :return: DNA sequence
        """
        from dna import DNA
        dna_seq = []
        for base in self.seq:
            if base == "A":
                dna_seq.append("A")
            elif base == "U":
                dna_seq.append("T")
            elif base == "G":
                dna_seq.append("G")
            elif base == "C":
                dna_seq.append("C")

        return DNA(''.join(dna_seq))

    def onehot(self):
        seq = []
        for base in self.seq:
            if base == "A":
                seq.append([1,0,0,0])
            elif base == "U":
                seq.append([0,1,0,0])
            elif base == "G":
                seq.append([0,0,1,0])
            elif base == "C":
                seq.append([0,0,0,1])

        return seq

    def integerEncoding(self):
        seq = []
        for base in self.seq:
            if base == "A":
                seq.append(1)
            elif base == "U":
                seq.append(2)
            elif base == "G":
                seq.append(3)
            elif base == "C":
                seq.append(4)

        return seq

    def complement(self):
        rna_seq = []
        for base in self.seq:
            if base == "A":
                rna_seq.append("U")
            elif base == "U":
                rna_seq.append("A")
            elif base == "G":
                rna_seq.append("C")
            elif base == "C":
                rna_seq.append("G")

        return ''.join(rna_seq)

    def __compatible(self, base1, base2):
        if (base1 == 'A' and base2 == 'U') or (base1 == 'U' and base2 == 'A'):
            return True
        elif (base1 == 'G' and base2 == 'C') or (base1 == 'C' and base2 == 'G'):
            return True
        else:
            return False

    def isComplement(self,otherseq):
        if len(self.seq) != len(otherseq):
            raise ValueError("Sequences not of same length")
        else:
            for i in range(len(otherseq)):
                if self.__compatible(self.seq[i], otherseq[i]):
                    continue
                else:
                    return False

            return True