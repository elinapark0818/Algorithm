# 분해합(m) = 256(245+2+4+5) 생성자(x)= 245
# x = input()
# n = sum(map(int, str(x)))
# m = int(x) + int(n)
# print(m)

n = int(input())
a = 0

for i in range(1, n + 1):
    m = list(map(int, str(i)))
    a = i + sum(m)

    if a == n:
        print(i)
        break
    if i == n:
        print(0)

