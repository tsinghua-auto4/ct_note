N    = int(input())
data = sorted(list(map(int, input().split())))
x    = int(input())

ans = 0
lft, rgt = 0, N-1
while lft < rgt:
    tmp = data[lft] + data[rgt]
    if tmp == x:
        ans += 1
        lft += 1
    elif tmp < x:
        lft += 1
    else:
        rgt -= 1
print(ans)