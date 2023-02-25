import sys

n     = int(sys.stdin.readline())
stars = [[' ']*(n*2) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        stars[i][j] = '*'
        stars[i][2*n-1-j] = '*'
    print(''.join(stars[i]))

for i in range(n-1, 0, -1):
    print(''.join(stars[i]))