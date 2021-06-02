import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

k = Counter(nums).most_common()

print(round(sum(nums) / N))
print(nums[N // 2])

if len(nums) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(nums[0][0])

print(nums[-1] - nums[0])
