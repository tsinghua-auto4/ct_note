def mul(a, b):
    n   = len(a)
    res = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            cur = 0
            for iter in range(n):
                cur += a[r][iter]*b[iter][c]
            res[r][c] = cur%1000
    return res

def square(a, b):
    if b == 1:
        for r in range(len(a)):
            for c in range(len(a)):
                a[r][c] %= 1000
        return a
    
    tmp = square(a, b//2)
    if b%2 == 1:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = square(A, B)
for r in ans:
    print(*r)