
N, M  = map(int, input().split())
Trees = list(map(int, input().split()))

start, end = 1, max(Trees)
while start <= end:
    mid = (start+end)//2
    cnt = 0

    for tree in Trees:
        if tree-mid > 0:
            cnt += (tree-mid)

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)