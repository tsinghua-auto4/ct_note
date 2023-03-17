import sys
import copy

n    = int(sys.stdin.readline().rstrip())
coin = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

ans = n ** 2
coin_reversed = copy.deepcopy(coin)

for i in range(n):
    for j in range(n):
        if coin_reversed[i][j] == 'H':
            coin_reversed[i][j] = 'T'
        else:
            coin_reversed[i][j] = 'H'

for b in range(1 << n):
    coin_tmp = []
    for i in range(n):
        if b & (1<<i): # 현재 행의 비트가 1로 되어있으면 뒤집고, 아니면 가만히 둔다
            coin_tmp.append(coin_reversed[i][:])
        else:
            coin_tmp.append(coin[i][:])
    
    # 열방향 탐색으로 뒤집는 것과 안뒤집는 것중 최대값 저장
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if coin_tmp[j][i] == 'T':
                tmp += 1
        cnt += min(tmp, n-tmp)
    # 현재 답보다 작다면 최소값이므로 저장
    ans = min(ans, cnt)

print(ans)