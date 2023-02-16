import sys

n = int(sys.stdin.readline())
star = ['*'] * n

print(''.join(star))
for i in range(n-1):
    star[i] = ' '
    print(''.join(star))