N    = int(input())

hist = [int(input()) for _ in range(N)]
hist.append(0)

lft  = 0
stk  = [(0, hist[0])]

ans  = 0
for idx in range(1, N+1):
    lft = idx
    while stk and stk[-1][1] > hist[idx]:
        lft, h = stk.pop()
        ans = max(ans, (idx-lft)*h)
    stk.append((lft, hist[idx]))

print(ans)