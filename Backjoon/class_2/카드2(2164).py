import sys
import collections

N = int(sys.stdin.readline())
rst = collections.deque([i for i in range(1, N + 1)])

while len(rst) > 1:
    rst.popleft()
    rst.rotate(-1)

print(rst[0])