from unittest import TestCase
from nucleopy.molecules.rna import RNA
from nucleopy.molecules.dna import DNA


class TestNucleotide(TestCase):
    def setUp(self):
        self.rna1 = RNA('AUUGCCAGUUC')
        self.rna2 = RNA('UAACGGUCAAG')
        self.rna3 = RNA('AAUUGC')
        self.dna1 = DNA('ATTGCCAGTTC')
        self.dna2 = DNA('TAACGGTCAAG')
        self.int = [1,2,2,3,4,4,1,3,2,2,4]
        self.onehot = [[1,0,0,0],[0,1,0,0],[0,1,0,0],
                       [0,0,1,0],[0,0,0,1],[0,0,0,1],
                       [1,0,0,0],[0,0,1,0],[0,1,0,0],
                       [0,1,0,0],[0,0,0,1]]


