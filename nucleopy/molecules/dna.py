"""
Creates a DNA object which contains a nucleotide sequence
"""
from nucleotide import Nucleotide


class DNA(Nucleotide):
    def __init__(self, sequence):
        """
        Creates a DNA object
        :param sequence: String sequence of nucleotides
        """

        Nucleotide.__init__(self, sequence)

        if 'A' not in self.seq or 'T' not in self.seq or 'G' not in self.seq or 'C' not in self.seq:
            raise ValueError("Not a valid DNA sequence")

    def complement(self):
        """
        Gets the complement strand of the DNA
        :return: Complement of the DNA sequence
        """

        dna_seq = []
        for base in self.seq:
            if base == "A":
                dna_seq.append("T")
            elif base == "T":
                dna_seq.append("A")
            elif base == "G":
                dna_seq.append("C")
            elif base == "C":
                dna_seq.append("G")

        return ''.join(dna_seq)

