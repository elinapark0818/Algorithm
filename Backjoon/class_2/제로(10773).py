
K = int(input())
rst = []
for i in range(K):
    num = int(input())
    if num == 0:
        rst.pop()
    else:
        rst.append(num)
print(sum(rst))
