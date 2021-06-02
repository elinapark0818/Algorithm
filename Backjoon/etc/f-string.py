# f-string의 모양은 f와 {}만 알면 된다.
# 문자열 맨 앞에 f를 붙여주고, 중괄호 안에 직접 변수이름이나 출력하고 싶은 것을 넣으면 된다.
# f'문자열 {변수}문자열'

s = 'coffe'
n = 5
result = f'저는 {s}를 좋아합니다. 하루에 {n}잔 마셔요.'
print(result)

#
#
#

# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)

# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)

# f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

# f-string 중괄호 출력 :
# 2개 = 중괄호 자체
# 3개 = {string 값}
num = 10
rst = f'my age {{{num}}}, {{num}}'
print(rst)