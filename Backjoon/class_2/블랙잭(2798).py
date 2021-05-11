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

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_num = 0

for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if biggest_num < temp_sum <= target_num:
        biggest_num = temp_sum
print(biggest_num)
