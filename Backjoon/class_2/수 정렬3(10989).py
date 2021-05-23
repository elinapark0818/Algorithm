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

# 이 문제의 핵심은 10001로 미리 배열의 크기를 지정해 두고, 그 외 값을 저장하지 않는다는 점
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

# 다른 풀이

n = int(sys.stdin.readline())
count = [0] * 10001

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    sys.stdout.write('%s\n' % i * count[i])