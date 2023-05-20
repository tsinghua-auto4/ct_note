

n, m = map(int, input().split())

a, b, c = 1, 1, 1
for cur in range(1, n+1):
    a *= cur
    if cur <= m:
        c *= cur
    if cur <= n-m:
        b *= cur

print(a//(b*c))