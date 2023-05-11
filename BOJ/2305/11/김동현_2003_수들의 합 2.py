

N, M   = map(int, input().split())
target = list(map(int, input().split()))

ans = 0
lft, rgt = 0, 1
while rgt <= N and lft <= rgt:
    tmp = sum(target[lft:rgt])

    if tmp == M:
        ans += 1
        rgt += 1

    elif tmp < M:
        rgt += 1

    else:
        lft += 1

print(ans)