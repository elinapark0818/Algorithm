# while True:
#     n = input()
#     if n == '0':
#         break
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')

import sys
import collections

while True:
    case = sys.stdin.readline().strip()

    if case == "0":
        break

    deque = collections.deque(list(map(int, case)))

    while True:
        if len(deque) == 1:
            print("yes")
            break

        left = deque.popleft()
        right = deque.pop()

        if left != right:
            print("no")
            break

        if left == right and len(deque) == 0:
            print("yes")
            break