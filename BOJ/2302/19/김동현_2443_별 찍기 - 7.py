import sys

n = int(sys.stdin.readline())
star = [' '] * (n-1)
star.append('*')
print(''.join(star))

for i in range(1, n):
    star[n-1-i] = '*'
    star.append('*')
    print(''.join(star))

for i in range(1, n):
    star[i-1] = ' '
    print(''.join(star[0:2*n-i-1]))