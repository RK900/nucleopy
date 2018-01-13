# nucleopy
Scientific Python library to easily work with nucleotide data. Users can create `DNA` and `RNA` objects and easily manipulate them
for use in scientific programming.
## Author
Rohan Koodli

## To Use
See the `examples` folder for example use cases for nucleopy.

### Creating a nucleotide object
```python
r = RNA('AGGCUUUACA')
d = DNA('ATCGGATCCG')
```

### Functions
```python
d.complement() # TAGCCTAGGC
d.isComplement('TAAGCG') # False
r.toDNA() # AGGCTTTACA
```

### RNA-specific functions (requires [ViennaRNA](https://github.com/ViennaRNA/ViennaRNA) installation)
```python
r.Viennafold()
r.ViennaTargetEnergy('(((....)))')
```
