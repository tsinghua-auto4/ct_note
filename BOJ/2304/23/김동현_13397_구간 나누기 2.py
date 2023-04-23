

def divide(mid: int):
    v_max = data[0]
    v_min = data[0]

    cnt=1
    for cur in data:
        if v_max < cur:
            v_max = cur
        if v_min > cur:
            v_min = cur
        
        if v_max - v_min > mid:
            v_max = cur
            v_min = cur
            cnt += 1

    return M >= cnt


N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end   = max(data)

ans = end
while start <= end:
    mid = (start + end)//2

    if divide(mid):
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1

print(ans)