# def solution(v):
#     answer = []
#     v1 = []
#     v2 = []
#
#     for i in v:
#         if i[0] not in v1:
#             v1.append(i[0])
#         else:
#             v1.remove(i[0])
#         if i[1] not in v2:
#             v2.append(i[1])
#         else:
#             v2.remove(i[1])
#     answer = v1 + v2
#     return answer

# 다른 코드
import collections


def solution(v):
    answer = []
    for i in zip(*v):
        y = collections.Counter(i)
        answer.extend([i for i in y if y[i] == 1])

    return answer


# XOR 을 이용한 코드
def solution(v):
    x = [i[0] for i in v]
    y = [i[1] for i in v]

    for i in range(2):
        x[0] ^= x[i + 1]
        y[0] ^= y[i + 1]
    answer = [x[0], y[0]]

    return answer
