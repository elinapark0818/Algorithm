# import sys
#
# n = sys.stdin.readline()
# N = set(sys.stdin.readline().split())
# m = sys.stdin.readline()
# M = sys.stdin.readline().split()
#
# for i in M:
#     sys.stdout.write('1\n') if 1 in N else sys.stdout.write('0\n')


# import sys
#
# input = sys.stdin.readline
# n = int(input())
# s = list(map(int, input().split()))
# m = int(input())
# s_ = list(map(int, input().split()))
# s.sort()
# for i in s_:
#     low, high = 0, n
#     while low <= high:
#         mid = (low + high) // 2
#         if mid < n and mid > -1:
#             if s[mid] < i:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         else:
#             break
#     if mid < n and mid > -1:
#         if i == s[high + 1]:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(0)


input_num = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
input_num2 = int(input())
numbers2 = list(map(int, input().split()))
for num in numbers2:
    left, right = 0, len(numbers) - 1
    is_find = False

    while True:
        median = (left + right) // 2
        if num == numbers[median]:
            print(1)
            is_find = True
            break
        elif num > numbers[median]:
            left = median + 1
        elif num < numbers[median]:
            right = median - 1
        if left > right:
            break

    if not is_find:
        print(0)
