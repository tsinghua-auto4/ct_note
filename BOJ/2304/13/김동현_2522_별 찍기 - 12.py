N = int(input())

target = [' ']*N
for i in range(N-1, -1, -1):
    target[i] = '*'
    print(''.join(target))
for i in range(0, N-1):
    target[i] = ' '
    print(''.join(target))