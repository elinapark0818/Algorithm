# 소수 : 1과 자신으로 나눌 때만 나누어 떨어지는 자연수
# 1은 소수가 아니다
# 2는 소수 중 유일한 짝수

# N = int(input())
# nums = map(int, input().split())
# rst = 0
# for num in nums:
#     error = 0
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 error += 1
#         if error == 0:
#             rst += 1
# print(rst)

# 다른 풀이
N = int(input())
rst = list(map(int, input().split()))


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
for i in rst:
    if prime(i):
        count += 1
print(count)
