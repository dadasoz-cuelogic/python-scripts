"""In the exercise below,
use the given lists to print out a set containing 
all the participants from event A which did not attend event B."""


a=["Jake","John","Eric"]
b=["John","Jill"]

aset=set(a)
bset=set(b)

print aset.difference(bset)