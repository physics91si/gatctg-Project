from protein import Protein
from protein import gRNA
from scraper import *

a = Protein()
print(a.promoter) # prints 1, which means that I am initializing protein correctly


b = gRNA()
print(b.dCas9) # prints 0, which means that I am initializing the gRNA class correctly

print (scrapeKeys ("arthur", "tsang"))
print (scrapeKeys ("abdallah", "abuhashem"))
print (scrapeKeys ("joey", "murphy"))
#The function prints keywords related to all 3 of you! I have switchec my project and can discuss more with you about it in class to make sure it is doable.
