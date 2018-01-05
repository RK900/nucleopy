"""
Creates an RNA object which contains a nucleotide sequence
"""


class RNA:
    def __init__(self, sequence):
        """
        Creates an RNA object
        :param sequence: String sequence of nucleotides
        """
        self.seq = sequence

    def toDNA(self):
        """
        Converts RNA to DNA
        :return: DNA sequence
        """
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

        return ''.join(dna_seq)

    def toDNAonehot(self):
        dna_seq = []
        for base in self.seq:
            if base == "A":
                dna_seq.append([1,0,0,0])
            elif base == "U":
                dna_seq.append([0,1,0,0])
            elif base == "G":
                dna_seq.append([0,0,1,0])
            elif base == "C":
                dna_seq.append([0,0,0,1])

        return ''.join(dna_seq)
