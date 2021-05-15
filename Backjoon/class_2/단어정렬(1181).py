# N = int(input())
# word = []
# for _ in range(N):
#     word.append(input())
#
# word = list(set(word))
# word.sort(key=lambda x: (len(x), x))
#
# print("\n".join(word))

import sys

n = int(sys.stdin.readline())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word.sort()
word.sort(key=lambda x: len(x))
print(*word, sep='\n')

#  다른 풀이

N = int(sys.stdin.readline())
li = []

for _ in range(N):
    li.append(sys.stdin.readline().strip())

# 중복 제거
li = list(set(li))

# 소팅 (1차: 길이, 2차: 사전 순)
sort = sorted(li, key=lambda x: (len(x), x))

for each in sort:
    print(each)

#  다른 풀이 시간이 엄청 걸린다

words = {}
rst = []
c = int(input())
for _ in range(c):
    word = input()
    if len(word) not in words:
        words[len(word)] = [word]
    else:
        if word not in words[len(word)]:
            words[len(word)].append(word)

for i in sorted(words.keys()):
    rst += sorted(words[i])

for j in rst:
    print(j)
