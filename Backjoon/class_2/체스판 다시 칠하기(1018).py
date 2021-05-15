# M*N 크기의 보드
# M*N의 보드를 잘라서 8*8 로 만들자
# 색깔은 흰색 또는 검은색
# 체스판처럼 하기 위해 다시 칠해야 하는 칸의 최소 개수를 구하라
# B=블랙 W=화이트

# N, M = map(int, input().split())
# map_list = [list(input()) for _ in range(N)]
# min_num = None
#
# for i in range(N - 7):
#     for j in range(M - 7):
#         num1, num2 = 0, 0
#         for k in range(i, i + 8):
#             for l in range(j, j + 8):
#                 if ((k + l - i - j) % 2 == 0):
#                     if (map_list[k][l] == 'B'):
#                         num1 += 1
#                 else:
#                     if (map_list[k][l] == 'W'):
#                         num1 += 1
#         for k in range(i, i + 8):
#             for l in range(j, j + 8):
#                 if ((k + l - i - j) % 2 == 0):
#                     if (map_list[k][l] == 'W'):
#                         num2 += 1
#                 else:
#                     if (map_list[k][l] == 'B'):
#                         num2 += 1
#         change_box = num1 if num1 < num2 else num2
#         if (min_num is None):
#             min_num = change_box
#         else:
#             min_num = change_box if min_num > change_box else min_num
# print(min_num)

# N = 8
# str1 = 'WBWBWBWB'
# str2 = 'BWBWBWBW'
# pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
# pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]
#
# a, b = [int(x) for x in input().split()]
# arr = []
# for i in range(a):
#     arr.append(input())
# rst = float('inf')
# for i in range(a - N + 1):
#     for j in range(b - N + 1):
#         count = 0
#         for p in range(N):
#             for q in range(N):
#                 if arr[i + p][j + q] != pivot1[p][q]:
#                     count += 1
#         rst = min(rst, count)
#         count = 0
#         for p in range(N):
#             for q in range(N):
#                 if arr[i + p][j + q] != pivot2[p][q]:
#                     count += 1
#         rst = min(rst, count)
# print(rst)


# # 4중 for문
# N, M = map(int, input().split())
# board = list()
# for i in range(N):
#     board.append(input())
# repair = list()
#
# # i, j 로 8*8 크기 조절 = (N-i)*(M-j)
# for i in range(N - 7):
#     for j in range(M - 7):
#         # 화이트로 시작한 경우 와 블랙으로 시작한 경우의 값을 초기화 = 0
#         first_W = 0
#         first_B = 0
#         # 처음 자른 체스판부터 for 시작한다
#         for q in range(i, i + 8):
#             for p in range(j, j + 8):
#                 # 행과 열의 인덱스의 합이 짝수인 경우, 일정한 한 색을 가지게 되고
#                 # 홀수인 경우에도 다른 일정한 한 색을 가지게 된다.
#                 if (q + p) % 2 == 0:
#                     if board[q][p] != 'W':
#                         first_W += 1
#                     if board[q][p] != 'B':
#                         first_B += 1
#                 else:
#                     if board[q][p] != 'B':
#                         first_W += 1
#                     if board[q][p] != 'W':
#                         first_B += 1
#         # 화이트로 시작했을 때 바꿔야 할 부분
#         repair.append(first_W)
#         # 블랙으로 시작했을 때 바꿔야 할 부분
#         repair.append(first_B)
#
# # 바꿔야 할 개수의 최소값
# print(min(repair))

# sys 모듈

import sys

# 잘라야하는 체스판의 크기가 정해져있고, 경우의 수가 2개밖에 안되니 하드코딩으로 짜둠
start_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

start_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# N: 세로 길이 / M: 가로 길이
N, M = map(int, sys.stdin.readline().split(" "))

# 인풋 받아서 8*8 배열에 저장
field = [[] for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline().strip()
    for j in range(M):
        field[i].append(line[j])

# 결과값 64(8*8)로 셋팅
result = 64

# N*M 크기의 보드를 8*8 크기로 자르기 -> 8*8의 시작점(0,0)이 될 애 고르기
for i in range(N - 7):
    for j in range(M - 7):

        count1 = 0
        count2 = 0

        # 시작점: field[i][j]
        for r in range(8):
            for c in range(8):

                # 시작점부터 가로로 8, 세로로 8까지 돌면서
                # B로 시작하는 체스판과 몇개가 다른지 카운팅
                if field[i + r][j + c] != start_B[r][c]:
                    count1 += 1

                # W로 시작하는 체스판과 몇개가 다른지 카운팅
                if field[i + r][j + c] != start_W[r][c]:
                    count2 += 1

        # 가장 작은 값으로 result 갱신
        result = min(result, count1, count2)

# 최종 결과값 출력
print(result)
