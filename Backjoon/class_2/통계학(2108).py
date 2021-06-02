import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

print(round(sum(nums)/N))