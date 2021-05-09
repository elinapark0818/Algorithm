# DFS 문제다
# 직관적으로 풀면 되는 문제이다..
# 첫 번째 인풋은 TC 개수이다
# 다음 인풋은 H W N 값이다.
# H = 높이, W = 너비, N = 몇 번째인지 를 뜻한다
# x축은 range(1,H)
# y축은 range(1,W)

# 예를 들어 6 12 10 은
# [6*12] 공간에서 (1,1) 부터 시작해서
# 10 은 (2,4) = 402(호)

# H > N 이면, H-N 만큼 x축이 +=1
# H < N 이면, N만큼 y축이 += 1
# N = (x,y)

# T = int(input())
# for i in range(T):
#     H, W, N = map(int, input().split())
#     room = N
#     floor = N % H
#     if N % H == 0:
#         room = N
#         floor = H
#     print({floor * 100 + room})


# for _ in range(int(input())):
#     h, w, n = map(int, input().split())
#     a = n % h
#     b = n
#     if a == 0:
#         a = h
#         b -= 1
#     print(a * 100 + b)

# t 입력
# t = int(input())
# for i in range(t):
#     # h,w,n 입력
#     h, w, n = map(int, input().split())
#     # x축은 n을 h로 나눴을때의 몫+1
#     x = n // h + 1
#     # n(사람 수)이 h(층 수)로 나누어질때
#     if n % h == 0:
#         y = h
#         # x축은 n을 h로 나눈 몫이다
#         x = n // h
#     # n(사람 수)이 h(층 수)로 나누어지지 않는다면 층수만 올라간다
#     else:
#         # y축은 층수이다
#         y = n % h
#     # 결과값은 층수가 100자리부터 시작하니까 *100 하고서 x축 값을 더한것
#     result = y * 100 + x
#     print(result)

# t = int(input())
# for _ in range(t):
#     h, w, n = map(int, input().split())
#     x = (n // h) + 1
#     if n % h == 0:
#         y = h
#         x = n // h
#     else:
#         y = n % h
#     roomNumber = y * 100 + x
#     print(roomNumber)

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    x = (n // h) + 1
    if n % h == 0:
        x = n // h
        y = h
    else:
        y = n % h
    result = (y * 100) + x
    print(result)
