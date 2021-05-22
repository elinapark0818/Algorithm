# 최대공약수를 구하는 함수를 gcd(x,y) 라고 가정
# x % y = 0이라면, gcd(x,y) = y가 성립
# x % y != 0이라면, gcd(x,y) = gcd(x, x%y)가 성립
# 두 번째 경우가 될때까지 반복한다

# 예를들어, '1071'과 '1029'의 최대공약수를 구하는 계산을 해보면
# '1071'은 '1029'로 나눠지지 않기때문에 '1071'을 '1029'로 나눈 나머지를 구한다 -> 42
# '1029'는 '42'로 딱 나눠지지 않기때문에 '1029'를 '42'로 나눈 나머지를 구한다 -> 21
# '42'는 '21'로 나눠진다. 그렇기에 최대공약수는 '21'이다

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


print(gcd(1071, 1029))


# 21

# 최소공배수는 x와 y의 공통된 배수 가운데 최소값으로
# 최소공배수는 x, y의 곱한 값을 x, y의 최대공약수를 나눈 것과 같다
# 즉, 유클리드 호제법으로 최대공약수를 구한 다음
# x와 y의 곱한 값을 나눠주면 최소공배수를 구할 수 있다

def lcm(x, y):
    return x * y // gcd(x, y)


print(lcm(1071, 1029))


# 52479


# N개의 최소공배수

def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


print(solution([2, 6, 8, 14]))
# 168