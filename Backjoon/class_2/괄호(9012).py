N = int(input())
rst = []
for i in range(N):
    inputList = list(input())
    stack = []
    answer = True

    for j in range(len(inputList)):
        if inputList[j] == "(":
            stack.append(inputList[j])
        else:
            try:
                if stack.pop() == "(":
                    pass
            except:
                rst.append("no")
                answer = False
                break
    if len(stack):
        rst.append("no")
        continue
    if answer:
        rst.append("yes")
for i in rst:
    print(i)
