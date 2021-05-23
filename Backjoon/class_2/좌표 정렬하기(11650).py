import sys

N = int(sys.stdin.readline())
M = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    M.append((x, y))
    M.sort(key=lambda x: (x[0], x[1]))

for i in M:
    print(i[0], i[1])
