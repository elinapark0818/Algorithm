
# def solution(arr):
#     answer = []
#
#     for i in range(len(arr)):
#         if arr[i - 1] != arr[i]:
#             answer.append(arr[i])
#         elif i == 0:
#             answer.append(arr[i])
#
#     return answer

# 다른 풀이

def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a