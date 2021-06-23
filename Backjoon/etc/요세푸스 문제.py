N, K = map(int, input().split())
q = []
result = []

for i in range(K):
    q.append(i + 1)
    c = 0

while len(q) > 0:
    c = (c + (K - 1)) % len(q)
    cc = q.pop(c)
    result.append(str(cc))

print("<%s>" % (", ".join(result)))