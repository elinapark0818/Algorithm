# 스택 (stack)은 기본적인 자료구조 중 하나로,
# 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아
# 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
#
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써,
# 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. -> sort()
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.


# 첫번째 줄에서 받은 입력값 n을 기준으로, n번 반복하는 for문을 돌리면서 x로 입력값을 받는다.
# count, stack, result, no_message를 초기화한다.
# count가 x보다 작을 때까지 반복:
# count는 하나씩 증가시키고
# stack에는 count값을 축적시키고
# result에는 +를 추가
# 만약 stack의 마지막 값과 x가 같다면
# stack의 마지막 값을 꺼내고
# result에는 -추가
# 만약 stack의 마지막 값과 x가 같아지지 않는 경우
# no_message에 False로 저장
# exit(0)으로 다음 반복으로 넘어가도록 함

# n = int(input())
# count = 0
# stack = []
# result = []
# no_message = True
#
# for i in range(n):
#     x = int(input())
#
#     while count < x:
#         count += 1
#         stack.append(count)
#         result.append("+")
#
#     if stack[-1] == x:
#         stack.pop()
#         result.append("-")
#     else:
#         no_message = False
#         exit(0)
#
# if no_message == False:
#     print("NO")
# else:
#     print("\n".join(result))


n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
