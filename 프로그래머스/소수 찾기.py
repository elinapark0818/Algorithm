import sys


def solution(n):
    answer = set([i for i in range(3, n + 1, 2)])

    for i in range(3, n + 1, 2):
        if i in answer:
            answer -= set([i for i in range(i * 2, n + 1, i)])

    return len(answer) + 1


# def solution(n):
#     num = set(range(2, n + 1))
#
#     for i in range(2, n + 1):
#         if i in num:
#             num -= set(range(2 * i, n + 1, i))
#     return len(num)

print(solution(1000000))


def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


# ----------------------------------------

M, N = map(int, sys.stdin.readline().split())
li = []
for i in range(M, N + 1):
    if i == 1:
        pass
    elif i == 2:
        li.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                li.append(i)

for i in li:
    print(i)