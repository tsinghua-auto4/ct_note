ans = -1*float('inf')
T   = int(input())
for _ in range(T):
    cur = sorted(list(map(int, input().split())))
    tmp = [cur[0], 1]
    for iter in range(1, 3):
        if tmp[0] == cur[iter]:
            tmp[1] += 1
        else:
            if tmp[1] >= 2:
                continue
            else:
                tmp = [cur[iter], 1]
    res = 0
    if tmp[1] == 3:
        ans = max(ans, 10000+tmp[0]*1000)
    elif tmp[1] == 2:
        ans = max(ans, 1000+tmp[0]*100)
    else:
        ans = max(ans, max(cur)*100)

print(ans)