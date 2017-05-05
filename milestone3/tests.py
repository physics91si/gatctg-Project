from protein import Protein
from protein import gRNA


a = Protein()
print(a.promoter) # prints 1, which means that I am initializing protein correctly


b = gRNA()
print(b.dCas9) # prints 0, which means that I am initializing the gRNA class correctly
