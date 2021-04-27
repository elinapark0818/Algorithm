# 첫째 줄에 두 수 A , B 주어진다
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)


# 인덱스 역순으로 출력하기 ::-1
# print('-'*10)
# s = [123,456]
# print(s[::-1])
