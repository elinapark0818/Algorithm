# 직각삼각형에서 직각을 낀 두 변의 길이를 각각 a,b라 하고 빗변의 길이를 c라고 하면
# 두 변(a,b)의 제곱의 합은 빗변의 길이의 제곱과 같다.
import math

n = input()
m = input()

a = float(n)
b = float(m)
c = (a * a) + (b * b)

print("빗변의 길이는", math.sqrt(c))
