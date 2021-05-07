# M*N 크기의 보드
# M*N의 보드를 잘라서 8*8 로 만들자
# 색깔은 흰색 또는 검은색
# 체스판처럼 하기 위해 다시 칠해야 하는 칸의 최소 개수를 구하라
# B=블랙 W=화이트

N, M = map(int, input().split())
map_list = [list(input()) for _ in range(N)]
min_num = None

for i in range(N - 7):
    for j in range(M - 7):
        num1, num2 = 0, 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'B'):
                        num1 += 1
                else:
                    if (map_list[k][l] == 'W'):
                        num1 += 1

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'W'):
                        num2 += 1
                else:
                    if (map_list[k][l] == 'B'):
                        num2 += 1

        change_box = num1 if num1 < num2 else num2
        if (min_num is None):
            min_num = change_box
        else:
            min_num = change_box if min_num > change_box else min_num

print(min_num)
