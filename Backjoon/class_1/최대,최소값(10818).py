# n = int(input())
# a = list(map(int, input().split()))
# print(min(a), max(a), end='')

n = input()

numList = list(map(int, input().split()))
Max = numList[0]
Min = numList[0]
for i in numList:
    if i > Max:
        Max = i
    if i < Min:
        Min = i
print(Min, Max, end='')
