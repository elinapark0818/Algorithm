numbers = []
for _ in range(3):
    i = int(input())
    numbers.append(i)

x = numbers[0] * numbers[1] * numbers[2]

x_list = list(str(x))
for i in range(10):
    x_count = x_list.count(str(i))
    print(x_count)

