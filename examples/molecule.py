from nucleopy.molecules.dna import DNA
from nucleopy.molecules.rna import RNA

r = RNA('AAUUGGCCCAGA')
d = DNA('AAACCGCCATTC')

print (r)
print (d)

print (r.toDNA())
print (d.toRNA())
print (r.toProtein())

print (d.onehot())
print (r.integerEncoding())

print (r.complement())

#print r.setSequence('m')
r[2] = 'm'
