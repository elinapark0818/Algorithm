import math
# 수학과 관련된 함수들을 모아높은 모듈
# ceil, floor, sign, cosign 등등 이용 가능하다

# math.ceil()
# 실수를 입력하면 올림하여 정수로 반환하는 함수

print(math.ceil(3.14))
# 4
print(math.ceil(-3.14))
# -3
print(math.ceil(-0.15))
# 0

# math.floor()
# 실수를 입력하면 내림하여 정수로 반환하는 함수

print(math.floor(3.14))
# 3
print(math.floor(-3.14))
# -4
print(math.floor(0.15))
# 0