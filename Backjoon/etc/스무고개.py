# 친구와 1부터 100까지 숫자 중 1가지 숫자를 맞추는 스무고개 게임을 하려고 합니다.
# 이 때 사용할 알고리즘을 의사코드로 표현하면 어떻게 될까요?

# N = int(input())
# for i in range(N):
#     a = int(input())
#     if a == N:
#         print('정답')
#     else:
#         print('땡!')

print('-' * 10)

import random

n = random.randint(1, 100)
print('1 ~ 100 까지의 숫자가 있습니다.')

for i in range(1, 21):
    print('숫자를 입력해주세요.')
    rst = int(input())

    if rst < n:
        print('UP!!!')
    elif rst > n:
        print('DOWN!!!')
    else:
        break

if rst == n:
    print('정답입니다.🎉')
else:
    print('틀렸습니다.💩')
