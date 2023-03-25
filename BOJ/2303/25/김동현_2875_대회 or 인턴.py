import sys

n, m, k = map(int, sys.stdin.readline().split()) #girls, boys, internship quantity

ans = 0
while True: # calculate team quantity first
    n -= 2
    m -= 1
    if n < 0 or m < 0 or n+m < k:
        break
    ans += 1
print(ans)