import sys

n    = int(sys.stdin.readline().rstrip())
a    = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

ans = 0

for i in range(n):
    cur = a[i]

    cur -= b
    ans += 1

    if cur > 0:
        if cur%c:
            ans += (cur//c + 1)
        else:
            ans += cur//c

print(ans)