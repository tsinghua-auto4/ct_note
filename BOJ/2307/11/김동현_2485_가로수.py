from math import gcd

N     = int(input())
trees = [int(input()) for _ in range(N)]

numbers = []
for idx in range(N-1):
    numbers.append(trees[idx+1]-trees[idx])

g = numbers[0]
for idx in range(1, N-1):
    g = gcd(g, numbers[idx])

ans = 0
for iter in numbers:
    ans += iter//g - 1

print(ans)