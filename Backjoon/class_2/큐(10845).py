# from sys import stdin
#
# qu = []
#
# for _ in range(int(stdin.readline())):
#     array = stdin.readline().split()
#     if array[0] == 'push':
#         qu.append(array[1])
#     elif array[0] == 'pop':
#         if qu:
#             print(qu.pop(0))
#         else:
#             print(-1)
#     elif array[0] == 'size':
#         print(len(qu))
#     elif array[0] == 'empty':
#         print(1 - int(bool(qu)))
#     elif array[0] == 'front':
#         if qu:
#             print(qu[0])
#         else:
#             print(-1)
#     elif array[0] == 'back':
#         if qu:
#             print(qu[-1])
#         else:
#             print(-1)
#     else:
#         pass

# 다른 풀이

from sys import stdin

N = int(stdin.readline())
Que = []
for i in range(N):
    A = stdin.readline().split()

    if A[0] == 'push':
        Que.append(A[1])

    elif A[0] == 'pop':
        if Que:
            print(Que.pop(0))
        else:
            print(-1)

    elif A[0] == 'size':
        print(len(Que))

    elif A[0] == 'empty':
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif A[0] == 'front':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[0])

    elif A[0] == 'back':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[-1])
