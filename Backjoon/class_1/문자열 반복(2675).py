n = int(input())
m = str()
for i in range(n):
    count, word = input().split()
    count = int(count)
    for j in word:
        m = m + (j * count)
    print(m)
    m = str()
