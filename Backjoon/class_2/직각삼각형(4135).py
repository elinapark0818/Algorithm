# 제일 큰 수랑 제일 작은 수를 더해서 /2 한 값을 찾아라
# 직각삼각형이 맞다면 right 아니라면 wrong
# 0 0 0 이 입력되면 break

while True:
    n = list(map(int, input().split()))
    a = max(n)
    b = min(n)
    if a == 0:
        break
    if ((a + b) % 2) == 0:
        print('right')
    else:
        print('wrong')