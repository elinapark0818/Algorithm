n, k = map(int, input().split())

circle = [i for i in range(1, n + 1)]
result = []
num = 0

while len(result) != n:
    num = (num + (k - 1)) % len(circle)
    result.append(circle.pop(num))

print("<%s>" % (", ".join(map(str, result))))