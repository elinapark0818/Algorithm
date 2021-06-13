# N = int(input())
# for i in range(N):
#     a = input()
#     b = list(a)
#     rst = 0
#     for i in b:
#         if i == '(':
#             rst += 1
#         elif i == ')':
#             rst -= 1
#         if rst < 0:
#             print('NO')
#             break
#     if rst > 0:
#         print('NO')
#     elif rst == 0:
#         print('YES')

print('----------------------')

T = int(input())

for i in range(T):
    li = list(input())

    while len(li) != 0:
        if li[0] == ')':
            print("NO")
            break
        else:
            if ')' in li:
                li.remove(')')
                li.remove('(')
            else:
                print("NO")
                break
    if len(li) == 0:
        print("YES")