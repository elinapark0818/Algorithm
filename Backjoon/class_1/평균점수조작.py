n = int(input())
scoreList = list(map(int, input().split()))
scoreMax = max(scoreList)
fakeAverage = 0

for i in range(0, n):
    scoreList[i] = (scoreList[i] / scoreMax) * 100
    fakeAverage += scoreList[i]

fakeAverage = fakeAverage / n

print('%.2f'%fakeAverage)