# a제곱 + b제곱 = c제곱
# 직각삼각형이 맞다면 right 아니라면 wrong
# 0 0 0 이 입력되면 break

# while True:
#     n = list(map(int, input().split()))
#     a = max(n)
#     b = min(n)
#     if a == 0:
#         break
#     if ((a + b) % 2) == 0:
#         print('right')
#     else:
#         print('wrong')
import math

while True:
    n = list(map(int, input().split()))
    a = n[0]
    b = n[1]
    c = n[2]
    if a == 0:
        break
    if ((a * a) + (b * b)) == (c * c):
        print('right')
    else:
        print('wrong')
