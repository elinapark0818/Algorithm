import sys

N = int(sys.stdin.readline())
M = []
for i in range(N):
    M.append(list(map(int, sys.stdin.readline().split())))
    M.sort(key=lambda x: (x[0], x[1]))

for i in M:
    print(i[0], i[1])

# 다른 풀이

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    arr.append([a, b])
rst = sorted(arr)

for j in range(n):
    print(rst[j][0], rst[j][1])
