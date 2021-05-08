# a제곱 + b제곱 = c제곱
# 직각삼각형이 맞다면 right 아니라면 wrong
# 0 0 0 이 입력되면 break
# 빗변의 길이는 제일 긴 값(max)이다


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

# while True:
#     n = list(map(int, input().split()))
#     a = n[0]
#     b = n[1]
#     c = n[2]
#     if a == 0:
#         break
#     if ((a * a) + (b * b)) == (c * c):
#         print('right')
#     else:
#         print('wrong')

while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        break
    max_n = max(n)
    n.remove(max_n)
    if n[0] ** 2 + n[1] ** 2 == max_n ** 2:
        print('right')
    else:
        print('wrong')
