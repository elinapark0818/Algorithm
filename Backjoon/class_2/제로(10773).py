K = int(input())
for i in K:
    num = list(int(input()))
    rst = []
    for j in num:
        if j != 0:
            rst.append(j)
        if j == 0:
            num.pop()
    print(sum(int(rst)))