import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr,2)
print(list(nCr))

# permutations 과 다르게
# 순서를 고려하지 않는다. ex> ('A','B') = ('B','A')
