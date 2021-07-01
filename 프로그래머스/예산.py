# # 예산신청 금액 []
#
# def solution(request, budget):
#     answer = 0
#     request.sort()
#     for i in range(len(request)):
#         if request[i] <= budget:
#             answer += 1
#             budget -= request[i]
#         else:
#             break
#     return answer
#
#
# # sort(), pop() 이용한 코드
#
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)
#
#
# # sorted를 이용한 코드
#
# def solution(d, budget):
#     answer = 0
#     for i in sorted(d):
#         budget -= i
#         if budget < 0:
#             break
#         answer += 1
#
#     return answer
#
#
# # itertools 과 combinations 이용한 코드
# from itertools import combinations
#
#
# def solution(d, budget):
#     if sum(d) == budget:
#         return len(d)
#     for i in range(len(d), 1, -1):
#         for j in list(combinations(d, i)):
#             if sum(j) == budget:
#                 return i
#


# 다시 풀어보기

# def solution(d, budget):
#     answer = 0
#     d.sort()
#     for i in range(len(d)):
#         if d[i] <= budget:
#             answer += 1
#             budget -= d[i]
#         else:
#             break
#     return answer



# 다른사람들이 많이 한 풀이

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)