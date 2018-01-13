"""
Creates an RNA object which contains a nucleotide sequence
"""
from nucleotide import Nucleotide
import re


class RNA(Nucleotide):
    def __init__(self, sequence):
        """
        Creates an RNA object
        :param sequence: String sequence of nucleotides
        """
        Nucleotide.__init__(self, sequence)

        if re.search(r'[^AUCG]', self.seq) is not None:
            raise ValueError("Not a valid RNA sequence")

    def complement(self):
        """
        Gets the complement strand of the RNA
        :return: Complement of the RNA sequence
        """

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


    def Viennafold(self):
        try:
            import RNA
            struc, energy = RNA.fold(self.seq)
            return struc, energy
        except ImportError:
            print ("ViennaRNA Python library not installed. "
                   "Please see config-ViennaRNA.md for installation details.")

    def ViennaTargetEnergy(self, target_structure):
        try:
            import RNA
            e = RNA.energy_of_structure(self.seq, target_structure, 0)
            return e
        except ImportError:
            print ("ViennaRNA Python library not installed. "
                   "Please see config-ViennaRNA.md for installation details.")