import itertools

arr = ['A', 'B', 'C', 'D']

# 원소 개수만큼 (여기서는 4) 순열 만들기
print(list(map(''.join, itertools.permutations(arr))))

# 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(arr, 3))))

# 2개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(arr, 2))))

# 2개의 원소로 순열 만들기 (1)
int_arr = ['1', '2', '3']
nPr = itertools.permutations(int_arr, 2)
print(list(nPr))
