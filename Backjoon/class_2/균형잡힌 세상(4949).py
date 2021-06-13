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
#
# -----------------------------------------
#
# while True:
#     bracket = input()
#     if bracket == ".":
#         break
#     bracket_stack = []
#     answer = True
#
#     for j in bracket:
#         if j == "(" or j == "[":
#             bracket_stack.append(j)
#
#         elif j == ")":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "(":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
#
#         elif j == "]":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "[":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
#
#     if answer and not bracket_stack:
#         print("yes")
#     else:
#         print("no")
#
# while True:
#     stack = []
#     push, pop = stack.append, stack.pop
#     s = input()
#     if s == '.':
#         break
#     r = 'yes'
#     for c in s:
#         if c in ['[', '(']:
#             push(c)
#         elif c == ']':
#             if not stack or pop() != '[':
#                 r = 'no'
#                 break
#         elif c == ')':
#             if not stack or pop() != '(':
#                 r = 'no'
#                 break
#     if stack:
#         r = 'no'
#         print(r)


while True:
    stack = [];
    push, pop = stack.append, stack.pop
    s = input()
    if s == '.': break
    r = 'yes'
    for c in s:
        if c in ['[', '(']:
            push(c)
        elif c == ']':
            if not stack or pop() != '[': r = 'no';break
        elif c == ')':
            if not stack or pop() != '(': r = 'no';break
    if stack: r = 'no'
    print(r)