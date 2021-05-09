# 분해합(m) = 256(245+2+4+5) 생성자(x)= 245
# x = input()
# n = sum(map(int, str(x)))
# m = int(x) + int(n)
# print(m)

# n = int(input())
# a = 0
#
# for i in range(1, n + 1):
#     m = list(map(int, str(i)))
#     a = i + sum(m)
#
#     if a == n:
#         print(i)
#         break
#     if i == n:
#         print(0)

# n = int(input())
# for i in range(n+1):
#     i_str = str(i)
#     total = i
#     for j in i_str:
#         total += int(j)
#     if total == n:
#         break
#
# print(i if i != n else 0)


N = int(input())  # 목표 분해합
low = 0

def get_devided_num(low_n):
    e = list(map(int, str(low_n)))
    devided_num = low_n + sum(e)
    return devided_num

while get_devided_num(low) != N:
    if low == N:
        low = 0
        break
    else:
        low += 1
print(low)
