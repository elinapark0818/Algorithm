# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#
#     return participant[-1]
#
#
# # Counter()를 이용한 코드
# import collections
#
#
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     result = collections.Counter(participant) - collections.Counter(completion)
#
#     return list(result.keys())[0]
#
#
# # hash()를 이용한 코드
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#
#     for p in participant:
#         dic[hash(p)] = p
#         temp += int(hash(p))
#
#     for c in completion:
#         temp -= hash(c)
#         answer = dic[temp]
#
#     return answer
#
#
# # zip()을 이용한 코드
#
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant.pop()

# 다시 풀어보기

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    answer = ''
    return answer