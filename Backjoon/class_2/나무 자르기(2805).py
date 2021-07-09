import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    avg = (start + end) // 2

    tree_sum = 0
    for i in tree:
        if i >= avg:
            tree_sum += i - avg

    if tree_sum >= M:
        start = avg + 1
    else:
        end = avg - 1
print(end)
