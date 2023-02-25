import sys

import sys

n     = int(sys.stdin.readline())
stars = [['*']*(n*2-1) for _ in range(n+1)]

for i in range(n):
    for j in range(i):
        stars[i][j] = ' '
        stars[i] = stars[i][:2*n-2-j]
    print(''.join(stars[i]))

for i in range(n-2, -1, -1):
    print(''.join(stars[i]))