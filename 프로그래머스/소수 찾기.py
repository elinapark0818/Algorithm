def solution(n):
    answer = set([i for i in range(3, n + 1, 2)])

    for i in range(3, n + 1, 2):
        if i in answer:
            answer -= set([i for i in range(i * 2, n + 1, i)])

    return len(answer) + 1