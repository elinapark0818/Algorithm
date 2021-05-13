# input() : 파이썬의 내장함수
# input > 개행(줄바꿈)문자를 벗겨내어 > 문자열로 변환 > return

# sys.stdin : file object 이다. 사용자의 입력을 받는 buffer를 만들어 그 buffer에서 읽어드리는 것

# import sys

# N = int(input())
# a = [sys.stdin.readline() for _ in range(N)]
# print(a)

# sys.stdin.readline() : 한 줄의 문자열을 반환한다.
# ^Z 를 입력받으면 종료되며, 개행문자(\n)까지 입력된다

import sys
# 정수를 한 줄에 입력받을 때
a, b, c = map(int, sys.stdin.readline().split())
print(a, b, c)

# 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때
data = list(map(int, sys.stdin.readline().split()))

# 임의의 개수의 정수를 한 줄에 입력받아 2차원 리스트에 저장할 때
# 각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고
# 길이가 다른 2차원 리스트도 입력받을 수 있다
arr = []
x = int(sys.stdin.readline())
for i in range(x):
    arr.append(list(map(int, sys.stdin.readline().split())))

# strip() : 문자열 맨 앞과 맨 끝의 공백문자를 제거한다
y = int(sys.stdin.readline())
str_list = [sys.stdin.readline().strip() for i in range(y)]

