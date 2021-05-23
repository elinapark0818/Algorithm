# 시간 초과
# N = int(input())
# li = []
#
# for i in range(N):
#     li.append(list(input().split()))
#     li.sort()
#
# for i in li:
#     print(i[0])

import sys

N = int(sys.stdin.readline())

li = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())

    li[input_num] = li[input_num] + 1

for i in range(10001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)