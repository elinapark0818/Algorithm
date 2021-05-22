N = int(input())
R = []
for _ in range(N):
    x, y = map(int, input().split())
    R.append((x, y))

for i in R:
    rank = 1

    for j in R:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end=' ')
