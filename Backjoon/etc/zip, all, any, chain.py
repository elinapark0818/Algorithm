# zip() : 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환한다
import itertools

z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z))
print(next(z))
print(next(z))

# all() : iterable한 객체를 인수로 반아서 원소가 모두 참이면 True, 아니면 False 반환한다
a = all([1, 2, 3])
print(a)
a = all([0, 1, 2])  # 0은 falsy 하다
print(a)

# any() : iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False
b = any([0, 1, 2])
print(b)
b = any([0, False, [], -0])
print(b)

# chain() : iterable한 객체들을 인수로 받아 하나의 iterator로 반환
c_int = [1, 2, 3]
c_str = ['A', 'B', 'C']
c = itertools.chain(c_int, c_str)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
