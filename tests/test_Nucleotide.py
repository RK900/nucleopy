from unittest import TestCase
from nucleopy.molecules.rna import RNA
from nucleopy.molecules.dna import DNA


class TestNucleotide(TestCase):
    def setUp(self):
        self.rna1 = RNA('AUUGCCAGUUC')
        self.rna2 = RNA('UAACGGUCAAG')
        self.dna1 = DNA('ATTGCCAGTTC')
        self.dna2 = DNA('TAACGGTCAAG')


