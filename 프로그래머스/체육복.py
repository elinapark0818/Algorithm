# n = 전체 학생의 수

# abs() 이용

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


# set 이용

def solution(n, lost, reserve):
    # 여벌의 체육복을 가진 set r를 구한다.
    s = set(lost) & set(reserve)
    # 체육복 없는 set l을 구한다.
    l = set(lost) - s
    r = set(reserve) - s

    # 앞번호에게 먼저 빌려주기 위해 r을 정렬하여 탐색한다.
    for i in sorted(r):
        if i - 1 in l:
            # 체육복을 받은 번호는 l에서 제거한다.
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
    # 전체 수 n 에서 l의 길이만큼 뺀 값을 반환한다.
    return n - len(l)
