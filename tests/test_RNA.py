from unittest import TestCase
import unittest
from nucleopy.molecules.rna import RNA
from nucleopy.molecules.dna import DNA


class TestRNA(TestCase):
    def setUp(self):
        self.complement1 = RNA('AUUGCCAGUUC')
        self.complement2 = RNA('UAACGGUCAAG')
        self.dna1 = DNA('ATTGCCAGTTC')

    def test_toDNA(self):
        self.assertEqual(self.complement1.toDNA().sequence(), self.dna1.sequence())

    def test_isComplement(self):
        self.assertTrue(self.complement1.isComplement(self.complement2.sequence()))

    def test_complement(self):
        self.assertEqual(self.complement1.complement().sequence(), self.complement2.sequence())


if __name__ == '__main__':
    unittest.main()
