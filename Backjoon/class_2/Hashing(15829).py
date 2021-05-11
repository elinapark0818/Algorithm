# 항의 번호에 해당하는만큼 특정한 숫자를 거듭제곱한 것을 곱한다음 더하는 것

L = int(input())
str = input()
result = 0
for i in range(L):
    result += (ord(str[i])-96)*(31**i)
print(result % 1234567891)

# ord() : 문자를 아스키코드 값으로 반환
# a = 97 이기 때문에 ord(str[i])-96 = 1 이 되도록 96을 빼준다
# r = 31 이기 때문에 (31**i) 를 곱해준다
