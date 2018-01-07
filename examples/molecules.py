from nucleopy.molecule import dna
from nucleopy.molecule import rna

r = rna.RNA('AAUUGGCCCAGUA')
d = dna.DNA('AAACCGCCATTCG')

print r.toDNA()
print r.complement()
print r