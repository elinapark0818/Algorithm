from collections import deque
import sys

n = int(sys.stdin.readline())

dq = deque()


def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0


def size():
    return len(dq)


for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])