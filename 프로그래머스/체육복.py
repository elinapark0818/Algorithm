# n = 전체 학생의 수

# abs() 이용 : 그냥..했나보다 굳이 절대값을?

# def solution(n, lost, reserve):
#     answer = n
#     result = []
#     for i in lost:
#         result.append([i, 0])
#     for j in reserve:
#         if j in lost:
#             result[lost.index(j)][1] = 1
#             continue
#         for i in result:
#             if i[1] == 0:
#                 if abs(j - i[0]) == 1:
#                     i[1] = 1
#                     break
#     if i in result:
#         if i[1] == 0:
#             answer -= 1
#     return answer


# # set 이용
#
# def solution(n, lost, reserve):
#     # 여벌의 체육복을 가진 set r를 구한다.
#     s = set(lost) & set(reserve)
#     # 체육복 없는 set l을 구한다.
#     l = set(lost) - s
#     r = set(reserve) - s
#
#     # 앞번호에게 먼저 빌려주기 위해 r을 정렬하여 탐색한다.
#     for i in sorted(r):
#         if i - 1 in l:
#             # 체육복을 받은 번호는 l에서 제거한다.
#             l.remove(i - 1)
#         elif i + 1 in l:
#             l.remove(i + 1)
#     # 전체 수 n 에서 l의 길이만큼 뺀 값을 반환한다.
#     return n - len(l)


# def solution(n, lost, reserve):
#     s_reserve = set(reserve) - set(lost)
#     s_lost = set(lost) - set(reserve)
#
#     for i in s_reserve:
#         # 왼쪽부터 있으면 빌려주기
#         if (i - 1) in s_lost:
#             s_lost.remove(i - 1)
#         # 왼쪽이 없으면 오른쪽으로 빌려주게끔
#         elif (i + 1) in s_lost:
#             s_lost.remove(i + 1)
#
#     return n - len(s_lost)


def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i not in lost:  # 안 잃어버린 학생
            answer += 1
        else:
            if i in reserve:  # 잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost:  # 잃어버리고 여분도 없어서 빌려야 하는 학생
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)

        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer
