import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

print(round(sum(nums) / N))

# round() : 반올림하는 내장함수

print(nums[N // 2])

# 최빈값 : 빈도가 가장 많은 수 + 여러개일 경우 두 번재로 작은 값 출력
from collections import Counter

k = Counter(nums).most_common()
if len(nums) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(nums[0])

# 범위구하기 : 마지막꺼에서 첫번째꺼 빼편 되겠쮸

print(nums[-1] - nums[0])
