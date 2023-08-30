N     = int(input())
dists = list(map(int, input().split()))
price = list(map(int, input().split()))

ans  = dists[0]*price[0]
past = price[0]
dist = 0

for idx in range(1, N-1):
    if price[idx] < past:
        ans += past*dist
        dist = dists[idx]
        past = price[idx]
    else:
        dist += dists[idx]

    if idx == N-2:
        ans += past*dist

print(ans)