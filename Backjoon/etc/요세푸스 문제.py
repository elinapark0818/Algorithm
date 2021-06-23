# N, K = map(int, input().split())
# q = []
# result = []
#
# for i in range(K):
#     q.append(i + 1)
#     c = 0
#
# while len(q) > 0:
#     c = (c + (K - 1)) % len(q)
#     cc = q.pop(c)
#     result.append(str(cc))
#
# print("<%s>" % (", ".join(result)))


# 다른 풀이
# # 입력
# N, K = map(int, input().split())
#
# josephus = [i for i in range(1, N + 1)]
# result = []
#
# temp = K - 1
#
# for i in range(N):
#     if len(josephus) > temp:  # 위치가 리스트를 넘지 않은 경우
#         result.append(josephus.pop(temp))  # 답 추가
#         temp += K - 1  # 다음 위치로 이동
#
#     elif len(josephus) <= temp:  # 위치가 리스트를 넘은 경우
#         temp = temp % len(josephus)
#         result.append(josephus.pop(temp))
#         temp += K - 1
#
# # 출력
# print("<", end='')
# for i in result:
#     if i == result[-1]:
#         print(i, end='')
#     else:
#         print("%s, " % (i), end='')
# print(">")

#
# n, k = map(int, input().split())
#
# circle = [i for i in range(1, n + 1)]
# result = []
# num = 0
#
# while len(result) != n:
#     num = (num + (k - 1)) % len(circle)
#     result.append(circle.pop(num))
#
# print("<%s>" % (", ".join(map(str, result))))


n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
key = 0
temp = k - 1
order = []

while people:
    key = (key+temp) % len(people)
    order.append(people.pop(key))

print('<'+', '.join(map(str, order))+'>')

