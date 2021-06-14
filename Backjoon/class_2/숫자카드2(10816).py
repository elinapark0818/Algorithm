# Hashing

from sys import stdin

_ = stdin.readline()
N = map(int, stdin.readline().split())
_ = stdin.readline()
M = map(int, stdin.readline().split())
hashmap = {}
for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(' '.join(str(hashmap[j]) if j in hashmap else '0' for j in M))

# Counter

from collections import Counter

_ = stdin.readline()
A = stdin.readline().split()
_ = stdin.readline()
B = stdin.readline().split()

C = Counter(A)
print(' '.join(f'{C[i]}' if i in C else '0' for i in B))
