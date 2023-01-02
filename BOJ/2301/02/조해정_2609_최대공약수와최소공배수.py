import sys
input = sys.stdin.readline
n1, n2 = map(int, input().split())
a, b = max(n1, n2), min(n1, n2)
M = b
while M > 0:
    if b % M == 0 and a % M == 0:
        break
    M -= 1
N = (a * b) // M
print(M)
print(N)
