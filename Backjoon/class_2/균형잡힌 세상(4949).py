# N = sys.stdin.readline()
# while True:
#     string = input().rstrip()
#     stack = []
#     true_flag = 1
#     for i in string:
#         if string == '.':
#             break
#         if i == '(' or i == '[':
#             stack.append(i)
#         elif i == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#         elif i == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#     print("yes" if true_flag and not (stack) else "no")

#
# import sys
#
# input = sys.stdin.readline
#
#
# def check(vps):
#     stk = []
#     pairs = {'(': ')', '[': ']'}
#     while vps:
#         v = vps.pop()
#         if v == ')' or v == ']':
#             stk.append(v)
#         else:
#             if not stk:
#                 return False
#             s = stk.pop()
#             if pairs[v] != s:
#                 return False
#     if stk:
#         return False
#     return True
#
#
# while True:
#     string = input().rstrip()
#     if string == '.':
#         break
#
#     vps = []
#     for s in string:
#         if s in '()[]':
#             vps.append(s)
#
#     if check(vps):
#         print('yes')
#     else:
#         print('no')


while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True

    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)

        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break

        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer and not bracket_stack:
        print("yes")
    else:
        print("no")