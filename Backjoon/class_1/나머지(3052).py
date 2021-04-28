n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)
print(n)

# set 함수 : 집합의 성질을 가지는 함수들을 비롯해 중복되지 않는 값을 찾을때
# 사용하는 함수.

result = set(n)

print(result)

# 개수를 구하는 건 길이를 구하는거라고 보면 되니까 len() 쓰면 됨

print(len(result))