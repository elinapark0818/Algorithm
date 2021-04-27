# for _ in range(n)

numbers = []
# 9개의 서로 다른 자연수가 주어질 때,
for _ in range(9):
    i = int(input())
    numbers.append(i)

# numbers = [int(input()) for _ in range(9)]

# 이들 중 최댓값을 찾고
print(max(numbers))

# 그 최댓값이 몇 번째 수(0부터 시작하니까 1더한다)
print(numbers.index(max(numbers)) + 1)