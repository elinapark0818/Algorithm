# 3장을 뽑아서 m과 가까운 정수의 합을 출력하라

# 3중 for문
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])
print(result)

# itertools, combinations 를 이용한 방법
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for card in combinations(cards, 3):
    cards_sum = sum(card)
    if result < cards_sum <= M:
        result = cards_sum
print(result)
