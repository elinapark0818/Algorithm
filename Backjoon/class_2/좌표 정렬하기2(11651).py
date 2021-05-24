import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

rst = sorted(arr)

for y, x in rst:
    print(x, y)
