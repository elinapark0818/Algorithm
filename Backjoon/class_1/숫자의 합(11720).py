n = int(input())
numbers = list(input())
result = []
for i in numbers:
    result.append(int(i))
    if len(result) == n:
        print(sum(result))
