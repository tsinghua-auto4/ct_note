
N, M = map(int, input().split())
data = list(map(int, input().split()))

video_max = max(data)
start = video_max
end   = sum(data)

ans = 10**9
while start <= end:
    mid = (start + end)//2
    cnt = 1
    tmp = 0

    for i in range(N):
        if tmp+data[i] <= mid:
            tmp += data[i]
        else:
            tmp = data[i]
            cnt += 1
        
        if cnt > M:
            break
    
    if cnt > M:
        start = mid+1
    else:
        end = mid-1
        if mid >= video_max:
            ans = min(ans, mid)

print(ans)