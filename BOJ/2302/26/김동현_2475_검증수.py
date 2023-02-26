import sys

data = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in data:
    ans += i**2

ans %= 10

print(ans)