# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#
#     return participant[-1]

# import collections
#
#
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     result = collections.Counter(participant) - collections.Counter(completion)
#
#     return list(result)[0]

# 다른 코드
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))

    for c in completion:
        temp -= hash(c)
        answer = dic[temp]

    return answer
