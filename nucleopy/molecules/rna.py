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
        """
        Turns RNA sequence into one-hot encoded list
        :return: List of one-hots
        """

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
        """
        Turns RNA sequence into integer-encoded list
        :return: List of integers
        """

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

    def __compatible(self, base1, base2):
        """
        Helper function to determine if two bases can be paired
        :param base1: Nucleotide 1
        :param base2: Nucleotide 2
        :return: True of bases can be paired; false otherwise
        """

        if (base1 == 'A' and base2 == 'U') or (base1 == 'U' and base2 == 'A'):
            return True
        elif (base1 == 'G' and base2 == 'C') or (base1 == 'C' and base2 == 'G'):
            return True
        else:
            return False

    def isComplement(self, otherseq):
        """
        Checks of two sequences are complements
        :param otherseq: Another RNA sequence
        :return: True if strands are complements; false otherwise
        """

        if len(self.seq) != len(otherseq):
            raise ValueError("Sequences not of same length")
        else:
            for i in range(len(otherseq)):
                if self.__compatible(self.seq[i], otherseq[i]):
                    continue
                else:
                    return False

            return True

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