

dp = [0 for _ in range(5001)]
dp[0] = 1 # 괄호가 없어도 한가지 경우
for n in range(2, 5001, 2): # 괄호의 전체 개수
    for i in range(2, n+1, 2): # 첫번째 괄호를 닫는 경우
        dp[n] += dp[i-2] * dp[n-i]
    dp[n] %= 1000000007


for _ in range(int(input())):
    print(dp[int(input())])