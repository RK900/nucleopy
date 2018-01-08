"""
Molecule superclass for DNA and RNA classes
"""


class Nucleotide(object):

    def __init__(self, sequence):
        self.seq = sequence
        self.seq = self.seq.upper()

    def __repr__(self):
        return self.seq

    def sequence(self):
        return self.seq

    def setSequence(self, new_sequence):
        self.seq = new_sequence
