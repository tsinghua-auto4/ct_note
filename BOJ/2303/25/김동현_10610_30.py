import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
zero  = 0
check = 0
for cur in n:
    if int(cur) == 0:
        zero = True
    check += int(cur)

if check % 3 == 0 and zero:
    print(''.join(n))
else:
    print(-1)