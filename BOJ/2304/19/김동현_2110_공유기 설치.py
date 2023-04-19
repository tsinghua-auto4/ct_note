
N, C   = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

ans = 0
start, end = 0, houses[-1]-houses[0]
while start <= end:
    mid = (start + end)//2
    cur = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= cur + mid:
            cur = houses[i]
            cnt += 1
    
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)