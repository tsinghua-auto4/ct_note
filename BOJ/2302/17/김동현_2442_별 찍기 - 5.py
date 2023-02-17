import sys

n = int(sys.stdin.readline())
star = [' '] * (n-1)
star.append('*')
print(''.join(star))

for i in range(1, n):
    star[n-1-i] = '*'
    star.append('*')
    print(''.join(star))