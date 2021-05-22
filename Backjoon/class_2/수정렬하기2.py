# 병합정렬, 퀵정렬, 힙정렬 을 이용한다
# 기본 정렬 라이브러리를 이용한다

# N = int(input())
# integer = []
#
# for _ in range(N):
#     x = int(input())
#     integer.append(x)
#
# for i in sorted(integer):
#     print(i)
#
#
#
#
# 시간이 매우 오래 걸렸다
# import sys
#
# n = int(input())
# li = []
# for i in range(n):
#     li.append(int(sys.stdin.readline()))
# for i in sorted(li):
#     sys.stdout.write(str(i) + '\n')

# 병합정렬
# 순서가 뒤죽박죽인 배열이 있을 때 정렬하기 위해 분할과 정복방식을 이용한다

# 1. 데이터를 절반씩 나누어 끝까지 갔다가(분할했다가)
# 2. 다시 절반씩 합치면서 그 안에서 정렬한다.(정복한다)