import itertools

arr = ['A', 'B', 'C', 'D']

# 원소 개수만큼 (여기서는 4) 수열 만들기
print(list(map(''.join, itertools.permutations(arr))))

# 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(arr, 3))))

# 2개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(arr, 2))))
