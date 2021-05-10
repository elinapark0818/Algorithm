# 1, 7(1+(1*6), 19(7+(2*6)), 37(19+(3*6)), 61(37+(4*6))
# 벌집 개수가 6배로 증가한다

n = int(input())

beeHome = 1  # 순서 1부터 시작한당
count = 1  # 벌집이 1개부터 시작한당
while n > beeHome:
    beeHome = beeHome + (count * 6)
    count += 1
print(count)