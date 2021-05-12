# 땅 위에 달팽이가 있다.
# 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다.
# 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다.
# 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

A, B, V = map(int, input().split())
result = 1
while True:
    V = V - A
    if V <= 0:
        print(result)
        break
    V = V + B
    result += 1
print(result)

#
a, b, v = map(int, input().split())
rst = 0
if (v - b) % (a - b) != 0:
    rst = ((v - b) // (a - b)) + 1
else:
    rst = (v - b) // (a - b)
print(rst)

#
a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(int(day) if day == int(day) else int(day) + 1)

#
A, B, V = map(int, input().split())
high = V - A
if high % (A - B) == 0:
    result = int(high / (A - B))
else:
    result = int(high / (A - B) + 1)
print(result + 1)

#
import math

a, b, v = map(int, input().split())
day = math.ceil((v - a) / (a - b)) + 1
print(day)
