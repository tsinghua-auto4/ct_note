N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

ans = [1 for _ in range(N)]
for iter in range(N):
    for comp in range(N):
        if iter == comp:
            continue
        if data[iter][0] < data[comp][0] and data[iter][1] < data[comp][1]:
            ans[iter] += 1

print(*ans)