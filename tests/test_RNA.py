from unittest import TestCase
from nucleopy.molecules.rna import RNA
from nucleopy.molecules.dna import DNA


class TestRNA(TestCase):
    def __init__(self):
        self.complement1 = RNA('AUUGCCAGUUC')
        self.complement2 = RNA('UAACGGUCAAG')
        self.dna1 = DNA('ATTGCCAGTTC')

    def test_toDNA(self):
        self.assertEqual(self.complement1.toDNA(), self.dna1)

    def test_isComplement(self):
        self.assertTrue(self.complement1.isComplement(self.complement2))

    def test_complement(self):
        self.assertEqual(self.complement1.complement(), self.complement2)
