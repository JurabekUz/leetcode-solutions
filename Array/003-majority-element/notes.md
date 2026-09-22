majority element

[2,2,1,1,1,2,2]

len(array)/2

we use counter, this is a first approache

second: set(array) and in the loop calculate count.


The important solution: Boyer-Moore Voting Algorithm

If one element occurs more than n/2 times, it cannot be completely cancelled out by all the other elements.

Every time we see a different value, we effectively cancel one occurrence of the candidate:

candidate + 1 other → cancel

