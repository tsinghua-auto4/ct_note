import sys

n = int(sys.stdin.readline())
star = ['*'] * (2*n-1)
print(''.join(star))

for i in range(1, n):
    star[i-1] = ' '
    print(''.join(star[0:2*n-i-1]))