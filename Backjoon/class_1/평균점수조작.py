n = int(input())
scoreList = input().split()

test = list(map(int, scoreList))

fakeMax = 0
for i in range(n):
    if fakeMax < test[i]:
        fakeMax = test[i]
for i in range(n):
    test[i] = (test[i] / fakeMax) * 100
fakeSum = 0
for i in range(n):
    fakeSum += test[i]
print(fakeSum / n)
