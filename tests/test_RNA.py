from test_Nucleotide import TestNucleotide
import unittest


class TestRNA(TestNucleotide):
    def setUp(self):
        TestNucleotide.setUp(self)

    def test_toDNA(self):
        self.assertEqual(self.rna1.toDNA().sequence(), self.dna1.sequence())

    def test_isComplement(self):
        self.assertTrue(self.rna1.isComplement(self.rna2.sequence()))

    def test_complement(self):
        self.assertEqual(self.rna1.complement().sequence(), self.rna2.sequence())

    def test_integer(self):
        self.assertEqual(self.rna1.integerEncoding(), self.int)

    def test_onehot(self):
        self.assertEqual(self.rna1.onehot(), self.onehot)


if __name__ == '__main__':
    unittest.main()
