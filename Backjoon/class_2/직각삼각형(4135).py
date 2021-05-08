# 제일 큰 수랑 제일 작은 수를 더해서 /2 한 값을 찾아라

while True:
    n = map(int, input().split())
    result = 0
    if n == '0 0 0':
        break
    if ((max(n) + min(n)) / 2) == n:
        print('right')
    else:
        print('wrong')
