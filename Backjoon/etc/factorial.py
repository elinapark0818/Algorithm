import math


# n = int(input())
# print(math.factorial(n))


# 재귀함수 사용
# def factorial(i):
#     if i == 0 or i == 1:
#         return 1
#     else:
#         return factorial(i - 1) * i
# x = int(input())
# print(factorial(x))

# 재귀함수 다른방법
# def factorial_2(j):
#     return j * factorial_2(j - 1) if j > 1 else 1
#
#
# y = int(input())
# print(factorial_2(y))

# 단순 반복문
a = int(input())

sum = 1
for i in range(a):
    sum *= i + 1
print(sum)