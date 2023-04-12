# 입력받자
n, k  = map(int, input().split())
coins = [int(input()) for _ in range(n)] # 정렬 필요 ㄴㄴ

# DP ㄱㄱ
dp    = [0]*(k+1) # 합이 k가 되는 경우의 수? -> 합이 j가 되는 경우의 수? [큰 문제를 작은 문제로 바꾸는 방법, DP]
dp[0] = 1 # 동전 1개만 쓸때의 경우의 수, coin 액수를 만들땐 coin 1개만 필요
for i in coins: # 코인을 순회해보자
    for j in range(i, k+1): # 코인보다 작은 화폐를 조합할 순 없으니, 더 큰걸로 알아보자
        if j-i >= 0: # 알아볼 화폐가 존재하면(0보다 큰, 조합가능한 수) 진행
            # dp[j]는 j 크기의 화폐를 조합할 수 있는 경우의 수
            # -> dp[j-i]의 i를 뺀 이유는 현재 보고 있는 코인이 i라서 j-i+i 크기의 화폐 조합 가능, 그래서 dp[j]에 경우의 수 dp[j-i]를 더해줌
            dp[j] += dp[j-i]
print(dp[k])