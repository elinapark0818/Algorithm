from sys import stdin
qu = []
for _ in range(int(stdin.readline())):
    array = stdin.readline().split()
    if array[0] == 'push':
        qu.append(array[1])
    elif array[0] == 'pop':
        if qu:
            print(qu.pop(0))
        else:
            print(-1)
    elif array[0] == 'size':
        print(len(qu))
    elif array[0] == 'empty':
        print(1 - int(bool(qu)))
    elif array[0] == 'front':
        if qu:
            print(qu[0])
        else:
            print(-1)
    elif array[0] == 'back':
        if qu:
            print(qu[-1])
        else:
            print(-1)
    else:
        pass