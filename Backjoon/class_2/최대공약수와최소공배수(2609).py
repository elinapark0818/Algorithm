import math
import sys

a, b = map(int, input().split())

# 최대공약수 구하기
for i in range(a + 1, 1, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소공배수 구하기
for i in range(b, (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break


# 유클리드 호제법

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


# 유클리드 호제법으로 풀기

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return int(g * (a / g) * (b / g))


print(gcd(a, b))
print(lcm(a, b))

# math 모듈로 풀기
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
