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
