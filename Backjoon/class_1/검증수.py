# a = list(map(int, input().split()))
# tc = 0
# for i in a:
#     tc += i*i
# tcRemainder = tc % 10
# print(tcRemainder)

a = list(map(int, input().split()))
x = 0
for i in a:
    x += i*i
print(x % 10)