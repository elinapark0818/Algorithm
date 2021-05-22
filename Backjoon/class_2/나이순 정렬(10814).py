# 시간초과
# N = int(input())
# li = []
#
# for i in range(N):
#     li.append(list(input().split()))
#     li.sort(key=lambda x: int(x[0]))
#
# for i in range(N):
#     print(li[i][0], li[i][1])

#
#
#
#

# 시간초과
# import sys
#
# n = int(sys.stdin.readline())
# m = []
# for i in range(n):
#     m.append(list(sys.stdin.readline().split()))
#     m.sort(key=lambda x: int(x[0]))
# for i in range(n):
#     print(m[i][0], m[i][1])

#
#
#
#

n = int(input())
m = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    m.append((age, name))

m.sort(key=lambda m_list: (m_list[0]))
# age 정렬
# def Lambda(m_list):
#     return m_list[0]

for i in m:
    print(i[0], i[1])


