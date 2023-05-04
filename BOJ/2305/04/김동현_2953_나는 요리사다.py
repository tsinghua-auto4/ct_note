
data = []
ans = [-1, -1]
for i in range(5):
    data.append(sum(list(map(int, input().split()))))
    if data[-1] > ans[1]:
        ans = [i+1, data[-1]]

print(*ans)