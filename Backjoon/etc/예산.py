# 예산신청 금액 []

def solution(request, budget):
    answer = 0
    request.sort()
    for i in range(len(request)):
        if request[i] <= budget:
            answer += 1
            budget -= request[i]
        else:
            break
    return answer
