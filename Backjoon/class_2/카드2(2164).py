# import sys
# import collections
#
# N = int(sys.stdin.readline())
# rst = collections.deque([i for i in range(1, N + 1)])
#
# while len(rst) > 1:
#     rst.popleft()
#     rst.rotate(-1)
#
# print(rst[0])

a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break