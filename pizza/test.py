import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

S = range(12)
for aset in findsubsets(S, 10):
	print aset[0]
