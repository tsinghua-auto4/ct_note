N    = int(input())
data = [int(input()) for _ in range(N)]

stk = []
ans = 0
for cur in data:
    while stk and stk[-1][0] < cur:
        ans += stk.pop()[1]
    
    if not stk:
        stk.append((cur, 1))
        continue

    if stk[-1][0] == cur:
        tmp = stk.pop()[1]
        ans += tmp

        if stk:
            ans += 1
        stk.append((cur, tmp+1))
    else:
        stk.append((cur, 1))
        ans += 1

print(ans)