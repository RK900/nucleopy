from test_Nucleotide import TestNucleotide
import unittest


class TestDNA(TestNucleotide):
    def setUp(self):
        TestNucleotide.setUp(self)

    def test_toRNA(self):
        self.assertEqual(self.dna1.toRNA().sequence(), self.rna1.sequence())

    def test_isComplement(self):
        self.assertTrue(self.dna1.isComplement(self.dna2.sequence()))

    def test_complement(self):
        self.assertEqual(self.dna1.complement().sequence(), self.dna2.sequence())


if __name__ == '__main__':
    unittest.main()