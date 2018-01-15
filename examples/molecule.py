from nucleopy.molecules.dna import DNA
from nucleopy.molecules.rna import RNA

r = RNA('AAUUGGCCCAGUA')
d = DNA('AAACCGCCATTCG')

print (r)
print (d)

print (r.toDNA())
print (d.toRNA())

print (d.onehot())
print (r.integerEncoding())

print (r.complement())

