import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

rst = sorted(arr)

for y, x in rst:
    print(x, y)