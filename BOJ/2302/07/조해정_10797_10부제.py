import sys
input = sys.stdin.readline
n = int(input())
cars = list(map(int, input().split()))
ans = 0
for car in cars:
    if n == car:
        ans += 1
print(ans)