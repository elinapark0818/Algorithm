# 이항계수(Binomial Coefficient) : 조합론에서 등장하는 개념으로
# 주어진 크기 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수를 일컫는다.
# 2를 상징하는 ‘이항’이라는 말이 붙은 이유는 하나의 아이템에 대해서는
# ‘뽑거나, 안 뽑거나’ 두 가지의 선택만이 있기 때문이다.

# 즉, n개 중에서 k개를 간택하는 것은 선택받지 못하는
# 나머지 (n-k)개를 선택하는 것과 같다.

# 선택할 기회가 n번 있을 때, 결국 k개를 뽑았을 경우의 수와 일치한다.
# - 주어진 기회는 n번이며, 각 기회에서 우리가 선택할 수 있는 전략은 1.선택하거나 2.선택하지 않거나 이다
# - 우리는 0번에서 시작해서 한 번씩 선택하며, 결국 n번째까지 선택했을 때, k개가 선택된 경우의 수를 알고 싶다.

# function(n, k) : n 만큼의 기회가 있었고,
#                  k 만큼을 선택했을 때,
#                  n번째에 도달했을 때 k개를 선택하는 경우의 수

# 결국 주어진 기회를 모두 사용했고,(n 만큼) and 결과적으로 k개가 선택되었다면
# 조합이 하나 완성되었기에 1을 반환하고, k개가 완성되었다면 0을 반환한다.

# 예제
import sys


def bino_coef(n, k):
    if k > n:
        return 0
    # 1
    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # 2
    # choose 함수는 times 번까지 got 개를 선택했을 때,
    # 최종적으로 n 번의 기회를 소진 시에 선택한 개수가 k 가 되는 경우의 수를 반환하는 함수이다.

    # 선택하는 가짓수를 통제했기 때문에 (n+1) * (r+1) 로도 충분했지만
    # 컴퓨터가 n 번 동안 0개부터 n 개를 선택하는 값을 모두 만들기 때문에 캐쉬를 키워줘야 한다
    # 그런데 캐쉬에 값이 0으로 되어 있으면 이게 계산한 값인지, 아니면 초기화된 값인지 알 수 없다.
    # 경우의 수는 0보다 작을 수 없다. 그래서 초기값으로 -1을 선택한 것이다.
    def choose(times, got):
        # 3
        if times == n:
            return got == k
        # 4
        #  -1은 초기화 값으로 현재 값이 -1이라는 얘기는
        #  이 위치의 값은 건드린 적이 없다는 것,
        #  그러니까 이전에 계산하지 않았기 때문에 계산해야 된다는 뜻이다
        if cache[times][got] != -1:
            return cache[times][got]
        # 5
        # times 번까지 got 개를 선택했을 때,
        # 최종적으로 n 번의 기회를 소진 시에 선택한 개수가 k 가 되는 경우의 수는
        # times+1 번째에 got 개가 선택되었을 때(이번에 선택하지 않았을 때)와
        # times+1 번째에 got+1 개가 선택된 경우의 수(이번에 선택했을 때)의 합이다.
        cache[times][got] = choose(times + 1, got) + choose(times + 1, got + 1)
        return cache[times][got]

    # 6
    return choose(0, 0)


import math

n, k = map(int, input().split())

result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(result)
