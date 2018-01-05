"""
Creates a DNA object which contains a nucleotide sequence
"""

class DNA:
    def __init__(self,sequence):
        """
        Creates a DNA object
        :param sequence: String sequence of nucleotides
        """
        self.seq = sequence

    def toRNA(self):
        rna_seq = []
        for base in self.seq:
            if base == "A":
                rna_seq.append("A")
            elif base == "T":
                rna_seq.append("U")
            elif base == "G":
                rna_seq.append("G")
            elif base == "C":
                rna_seq.append("C")

        return ''.join(rna_seq)

