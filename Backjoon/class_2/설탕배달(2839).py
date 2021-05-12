N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break

# 다른 풀이
#
# N = int(input())
# count = 0
# while N >= 0:
#     if N % 5 == 0:
#         count += (N // 5)
#         print(count)
#         break
#     N -= 3
#     count += 1
# else:
#     print(-1)