N = int(input())
li = []

for i in range(N):
    li.append(list(input().split()))
    li.sort()

for i in li:
    print(i)