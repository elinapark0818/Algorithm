# for x in range(97, 123):
#     print(chr(x), end="")

s = input()
a = list(range(97, 123))

for i in a:
    print(s.find(chr(i)))
