

N = int(input())
A = list(map(int, input().split()))

dp = [N+1 for _ in range(N)]
dp[0] = 0

for iter in range(N):
    for j in range(1, A[iter]+1):
        if iter+j < N:
            dp[iter+j] = min(dp[iter] + 1 , dp[iter+j])
print(dp[N-1] if dp[N-1] != N+1 else -1)