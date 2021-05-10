# a층의 b호에 살려면 a-1층 1호부터 b호까지의 사람들의 수의 합만큼
# 사람들을 데려와 살아야 한다.
# 0층부터 있고 1호부터 시작한다.
# 0층의 i호에는 i명이 산다.


# k층 n호에 몇 명이 살고 있는지 출력하라.
#
# T = int(input())
#
# for _ in range(T):
#     k = int(input())  # 층
#     n = int(input())  # 호
#     result = [i for i in range(1, n + 1)]  # 제일 아래층 사람 수
#
#     for _ in range(k):  # 층 수만큼 반복
#         for q in range(1, n):  # 1 ~ number-1 까지
#             print(result[q])
#             result[q] += result[q - 1]  # 층 별 각 호실의 사람 수를 변경
#         print(result)
#     print(result[-1])  # 가장 마지막 수 출력

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    rst = [i for i in range(1, n + 1)]
    for _ in range(k):
        for q in range(1, n):
            rst[q] += rst[q - 1]
    print(rst[-1])
