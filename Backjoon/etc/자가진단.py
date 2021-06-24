# 1. 논리적 추론
# 두 사람만 진실을 말하고 있다. 거짓말 한 사람은? 빵을 먹은 사람은?

# A: "내가 빵을 먹었다."
# B: "A가 한 말은 거짓말이다."
# C: "B가 빵을 먹었다."

# A가 거짓이라면, B,C 진실 -> 정답
# B가 거짓이라면, A도 거짓이됨 -> 땡
# C가 거짓이라면, 누가 먹었는지 알 수 없음 -> 땡

# 정답 : A, 빵을 먹은 사람: B,C

# ------------------------------------------------------------
# 2. 패턴 찾기
# 1, 3, 6, 11, 19, 31, 48, (), ...

# +2, +3, +5, +8, +12, +17, ?
#   +1  +2   +3  +4   +5   +6

# 정답은 71 : 48 + 23(17+6)

# ------------------------------------------------------------

# 3. 반복구조

# count = 0;
# for (int i =1; i <= 100; i += 7)
#     count++;

# 정답 : 1, 8(1+7), 15(8+7), 22(15+7), 29(22+7) ...92(85+7)

for i in range(1, 101, 7):
    print(i)
# ------------------------------------------------------------
# 4. 조건식
# 다음은 1부터 100까지 합을 구하는 프로그램의 일부입니다.
# 빈 칸에 들어갈 내용으로 가장 알맞은 것은?
# count < 99
# count < 100
# count == 100
# count != 100
# count < 101

sum = 0
count = 1
while True:
    sum += count
    count += 1
    if count == 100:
        break
print(sum)
# ------------------------------------------------------------
# 5. 논리식
# 윤년 구하기, 연산자
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')

# ------------------------------------------------------------
# 6. 함수 구현

# def solution(arr):
#     number = 0
#     result = []
#     while number < 100:
#         if 1 < arr.count(number):
#             result.append(arr.count(number))
#             number += 1
#
#         if result == []:
#             return [-1]
#         else:
#             return result

arr = list(map(int, input().split()))

count = [0 for _ in range(10)]
copy = [0 for _ in range(10)]
new_count = []

for i in range(0, len(arr)):
    copy[i] = arr[i]
    count[arr[i]] += 1

for i in range(0, len(count)):
    if count[i] > 1:
        new_count.append(count[i])

    if len(new_count) > 0:
        print(new_count)
    else:
        print(-1)
