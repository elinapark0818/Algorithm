# n = 전체 학생의 수

def solution(n, lost, reserve):
    n = int(input())
    lost = list(map(int, input()))
    reserve = list(map(int, input()))
    result = []

    for i in range(n):
        if ((lost[i] + 1) in reserve[i]) or ((lost[i] - 1) in reserve[i]):
            result.append(lost[i])
        elif reserve:
            result.append(reserve[i])

        result.sort()

    return set(result)
