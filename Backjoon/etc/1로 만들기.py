# 점화식
# f(x)는 다음과 같은 값에서 최소값을 가진다
# f(x-1) +1
# f(x/2) +1
# f(x/3) +1
#  위 3가지 함수의 최소값을 구하면 된다

# 재귀함수를 매번 호출하면 시간복잡도가 커지므로 다이나믹을 이용한다
# 즉, 리스트를 만들어 값을 매번 저장한다

# D[n] = min(D[n/3], D[n/2], D[n-1]) + 1

n = int(input())
result = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    if i == 1:
        result[i] = 0
        continue
    result[i] = result[i - 1] + 1
    if i % 3 == 0 and result[i // 3] + 1 < result[i]:
        result[i] = result[i // 3] + 1
    if i % 2 == 0 and result[i // 2] + 1 < result[i]:
        result[i] = result[i // 2] + 1
print(result[n])

# 다른 방법

x = int(input())
dp = [0, 0, 1, 1]
cnt = 0
for i in range(4, x + 1):
    dp.append(dp[i - 1] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
print(dp[x])
