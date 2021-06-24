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


# sort(), pop() 이용한 코드

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
