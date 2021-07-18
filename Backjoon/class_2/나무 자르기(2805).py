# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# tree = list(map(int, sys.stdin.readline().split()))
# start, end = 1, max(tree)
#
# while start <= end:
#     avg = (start + end) // 2
#
#     tree_sum = 0
#     for i in tree:
#         if i >= avg:
#             tree_sum += i - avg
#
#     if tree_sum >= M:
#         start = avg + 1
#     else:
#         end = avg - 1
# print(end)


# 통과되는 풀이
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
result = []

while not right < left:
    length = 0
    mid = (left + right) // 2

    length = sum(i - mid if i > mid else 0 for i in trees)

    if length == M:
        result.append(mid)
        break
    elif length > M:
        result.append(mid)
        left = mid + 1
    else:
        right = mid - 1
H = max(result)

print(H)

# Counter 이용한 풀이

# from sys import stdin
# from collections import Counter
#
#
# def BS_tree(data, M):
#     start, end = 0, max(data)
#     result = 0
#     while start <= end:
#         total = 0
#         mid = (start + end) // 2
#         for x, num in data.items():
#             if x > mid:
#                 total += (x - mid) * num  # 해당 값이 등장한 개수만큼 곱한다
#
#         if total < M:
#             end = mid - 1
#         else:
#             result = mid
#             start = mid + 1
#
#     return result
#
#
# _, M = map(int, stdin.readline().split())
# data = Counter(map(int, stdin.readline().split()))
# print(BS_tree(data, M))
