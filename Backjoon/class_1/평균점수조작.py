n = int(input())
scoreList = list(map(int, input().split()))
scoreMax = max(scoreList)
fakeSum = 0
for item in scoreList:
    fakeSum += (item / scoreMax) * 100

fakeAverage = fakeSum / n

print('%.2f'%fakeAverage)
