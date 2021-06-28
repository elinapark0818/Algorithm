# 첫째 줄에는 K, N
# 1 <= K <= 10,000
# 1 <= N <= 1,000,000
# K <= N

import sys

K, N = map(int, input().split())
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
