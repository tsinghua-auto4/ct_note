import sys

n = int(sys.stdin.readline())

ans = 1
for i in range(2, n+1):
    ans *= i

print(ans)