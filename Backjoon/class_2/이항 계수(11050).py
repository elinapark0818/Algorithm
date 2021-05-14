# 파스칼의 법칙
# 이항계수란 n개의 원소에서 r개의 원소를 뽑아내는 방법의 수
# nCr = n-1Cr-1 + n-1Cr
# n-1개의 원소 중 r-1개를 뽑아내는 경우의 수 + n-1개의 원소 중 r개를 뽑아내는 경우의 수
# 즉, 이미 n번째 원소를 선택했다고 가정하고 나머지 원소 중에서 r-1개를 뽑는 경우의 수 + n번째 원소를 제외한 나머지 중에서 r개의 원소를 뽑는 경우의 수

# C(n, k) = C(n-1, k-1) + C(n-1, k)
# 이항계수는 C(n, 0), C(n, n)일 때 항상 1이라는 값을 가진다.

# ----------------
#
# a, b = map(int, input().split())
#
#
# def binomial(N, K):
#     if N == K:
#         return 1
#     elif K == 0:
#         return 1
#     else:
#         return binomial(N - 1, K - 1) + binomial(N - 1, K)
#
#
# print(binomial(a, b))

# ----------------
#
# from math import factorial
#
# n, k = map(int, input().split())
# rst = factorial(n) // factorial(k) * factorial(n - k)
# print(rst)

#
# n, k = list(map(int, input().split()))
#
# a = 1
# for i in range(n, n - k, -1):
#     a *= i
# b = 1
# for i in range(1, k + 1):
#     b *= i
# print(a // b)

# ----------------

import math

n, k = map(int, input().split())

result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(result)