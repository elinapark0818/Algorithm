# comprehension = 리스트를 쉽게 한 줄로 만들 수 있는 파이썬 문법

# 예제
size = 10
arr = [i * 2 for i in range(size)]
print(arr)

# [(변수를 활용한 값) for (사용할 변수 이름) in (순회할 수 있는 값)]

# 변수를 활용한 값 = 실제로 할당될 값

# 사용할 변수 이름 = for 안에서 사용될 인자의 이름

# 순회할 수 있는 값 = 'Iterable' 값을 하나씩 살펴볼 수 있는 것을 총칭한다
# range 뿐만 아니라 set,dict,tuple 등

# 다른 예제
new_arr = [n * n for n in arr]
print(new_arr)

# 문자열 예제
word = '가나다'
print([c * 2 for c in word])

# if 문을 적용한 예제
arr = [n for n in range(1, 11) if n % 2 == 0]
print(arr)

# AND 연산자를 적용한 예제 : and를 쓰면 SyntaxError가 발생한다
arr = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
print(arr)

# OR 연산자를 적용한 예제 : or 연산자로 논리 연산을 묶어줘야 한다
arr = [n for n in range(1, 16) if n % 2 == 0 or n % 3 == 0]
print(arr)

# set
set_number = {n ** 2 for n in range(10)}
print(set_number)

# dict
from string import ascii_lowercase as LOWERS

dict_number = {c: n for c, n in zip(LOWERS, range(1, 27))}
print(dict_number)

# tuple
tuple_number = tuple(n for n in range(1, 10))
print(tuple_number)
