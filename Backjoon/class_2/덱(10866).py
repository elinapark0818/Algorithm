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
    elif command[0] == 'pop_front':
        if empty() == 1:
            print('-1')
        else:
            tmp = dq.popleft()
            print(tmp)
    elif command[0] == 'pop_back':
        if empty() == 1:
            print('-1')
        else:
            tmp = dq.pop()
            print(tmp)
    elif command[0] == 'front':
        if empty() == 1:
            print('-1')
        else:
            print(dq[0])
    elif command[0] == 'back':
        if empty() == 1:
            print('-1')
        else:
            print(dq[len(dq) - 1])
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
