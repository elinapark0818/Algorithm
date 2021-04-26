a = list(map(int, input().split()))
tc = 0
for i in a:
    tc += i*i
tcRemainder = tc % 10
print(tcRemainder)
