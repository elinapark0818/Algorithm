n = int(input())
for i in range(n):
    a = input()
    b = list(a)
    result = 0
    c = 1
    for j in b:
        if j == 'O':
            result += c
            c += 1
        else:
            c = 1
    print(result)

print('-'*10)

num = int(input())
for _ in range(num):
    inputList = list(input())
    score = 0
    sum = 0 # 새로운 ox리스트를 입력받으면 점수합계를 리셋한다
    for i in inputList:
        if i == 'O':
            score += 1 # 'O'가 연속되면 점수가 1씩 커짐
            sum += score
        else:
            score = 0 # 'X'는 0점이다
    print(sum)