# '666' 을 포함하는 숫자
# 10000 이하

# 666
# 1666
# 2666
# 3666
# 4666
# 5666
# 6660
# 6661
# 6662
# 6663
# 6664
# 6665
# 6666
# 6667
# 6668
# 6669
# 7666
# 8666
# 9666

N = int(input())
movie = 666

while N:
    if '666' in str(movie):
        N -= 1
    movie += 1
print(movie - 1)


# import sys
#
#
# def movie(n):
#     end = 666
#     while n != 0:
#         if '666' in str(end):
#             n -= 1
#         end += 1
#     return end
#
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     print(movie(n) - 1)