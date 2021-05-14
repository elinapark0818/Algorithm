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

#
def factorial(n):
    if (n > 1):
        return n * factorial(n - 1)
    else:
        return 1


a = int(input())
print(factorial(a))

# 단순 반복문
# a = int(input())
#
# result = 1
# for i in range(1, a + 1, 1):
#     result *= i
# print(result)
