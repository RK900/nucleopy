"""
Molecule superclass for DNA and RNA classes
"""


class Nucleotide(object):

    def __init__(self, sequence):
        """
        Initializes Nucleotide object
        :param sequence: Nucleotide sequence
        """

        self.seq = sequence
        self.seq = self.seq.upper()

    def __repr__(self):
        """
        Printable representation of Nucleotide object
        :return: Sequence
        """

        return self.seq

    def sequence(self):
        """
        Returns a sequence
        :return: Sequence
        """
        return self.seq

    def setSequence(self, new_sequence):
        """
        Sets a new sequence
        :param new_sequence: New sequence to be in the Nucleotide object
        """
        self.seq = new_sequence

    def toRNA(self):
        """
        Converts the DNA to RNA
        :return: RNA sequence
        """

        from rna import RNA
        rna_seq = self.seq.replace("T", "U")

        return RNA(rna_seq)

    def toDNA(self):
        """
        Converts RNA to DNA
        :return: DNA sequence
        """

        from dna import DNA
        dna_seq = self.seq.replace("U", "T")
        return DNA(dna_seq)

    def onehot(self):
        """
        Turns DNA sequence into one-hot encoded list
        :return: List of one-hots
        """

        seq = []
        for base in self.seq:
            if base == "A":
                seq.append([1,0,0,0])
            elif base == "T" or base == 'U':
                seq.append([0,1,0,0])
            elif base == "G":
                seq.append([0,0,1,0])
            elif base == "C":
                seq.append([0,0,0,1])

        return seq

    def integerEncoding(self):
        """
        Turns DNA sequence into integer-encoded list
        :return: List of integers
        """

        seq = []
        for base in self.seq:
            if base == "A":
                seq.append(1)
            elif base == "T" or base == 'U':
                seq.append(2)
            elif base == "G":
                seq.append(3)
            elif base == "C":
                seq.append(4)

        return seq

    def __compatible(self, base1, base2):
        """
        Helper function to determine if two bases can be paired
        :param base1: Nucleotide 1
        :param base2: Nucleotide 2
        :return: True of bases can be paired; false otherwise
        """

        if (base1 == 'A' and base2 == 'T') or (base1 == 'T' and base2 == 'A'):
            return True
        elif (base1 == 'G' and base2 == 'C') or (base1 == 'C' and base2 == 'G'):
            return True
        elif (base1 == 'A' and base2 == 'U') or (base1 == 'U' and base2 == 'A'):
            return True
        else:
            return False

    def isComplement(self, otherseq):
        """
        Checks of two sequences are complements
        :param otherseq: Another DNA sequence
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
