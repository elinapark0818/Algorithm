import sys

N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    tree = list(map(int, sys.stdin.readline().split()))
    H = []
    for i in range(len(tree)):
        if tree[i] > M:
            H.append(tree[i])
            print(H)

        #     tree.pop(i)
        # elif min(tree):
        #     tree.pop(i)
        # H.append(tree)
        # for i in range(len(H)):
        #     H_sum = sum(H[i])
        #     result = H_sum % len(H)
        #     print(result)
