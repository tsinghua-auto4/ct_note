

N       = int(input())
targets = list(map(int, input().split()))
targets.extend([0, 0])

dp = [[[0]*61 for _ in range(61)] for _ in range(61)] # 남은 체력으로 indexing
dp[targets[0]][targets[1]][targets[2]] = 1 # 첫번째

cases = [(9,3,1), (9,1,3), (3,9,1), (3,1,9), (1,9,3), (1,3,9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0: # 체력이 있으면~ 진행
                for case in cases:
                    ni = i-case[0] if i-case[0] >= 0 else 0
                    nj = j-case[1] if j-case[1] >= 0 else 0
                    nk = k-case[2] if k-case[2] >= 0 else 0
                    if dp[ni][nj][nk] == 0 or dp[ni][nj][nk] > dp[i][j][k] + 1:
                        dp[ni][nj][nk] = dp[i][j][k] + 1
print(dp[0][0][0]-1)