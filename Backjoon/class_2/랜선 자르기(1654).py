# 첫째 줄에는 K, N
# 1 <= K <= 10,000
# 1 <= N <= 1,000,000
# K <= N

import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline()))
l, h = 1, max(arr)
result = 0

while l <= h:
    middle = (l + h) // 2
    countSum = sum([(i // middle) for i in arr])

    if countSum >= n:
        result = middle
        l = middle + 1

    elif countSum < n:
        h = middle - 1

print(result)



# 다른 풀이

# input = sys.stdin.readline
# k, n = map(int, input().split())
# s = []
# for i in range(k): s.append(int(input()))
# low, high = 0, 10000000000
# while low <= high:
#     mid = (low + high) // 2
#     num = 0
#     for i in s: num += i // mid
#     if num >= n: low = mid + 1
#     else: high = mid - 1
# print(high)


K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)