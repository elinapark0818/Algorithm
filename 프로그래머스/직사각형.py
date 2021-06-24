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
# import collections
#
#
# def solution(v):
#     answer = []
#     for i in zip(*v):
#         y = collections.Counter(i)
#         answer.extend([i for i in y if y[i] == 1])
#
#     return answer


# XOR 이용한 초간결 코드
def solution(v):

    answer = []

    x = sorted(list(map(lambda x: x[0], v)))
    y = sorted(list(map(lambda y: y[1], v)))

    print('x : ', x, ', y : ', y)

    answer.append(x[0] ^ x[1] ^ x[2])
    answer.append(y[0] ^ y[1] ^ y[2])

    return answer
