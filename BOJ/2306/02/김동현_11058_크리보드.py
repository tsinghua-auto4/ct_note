

N = int(input())

dp = [i for i in range(N+1)] # 기본값은 모두 a를 출력하는 버튼을 누른 경우

# 6 까지는 a만 연타하는게 제일 큼, 나머지는 3step을 써서 선택/복사/붙여넣기 combo를 써서 뒤로 미뤄보기
# -3 은 1 combo = 2배, -4는 2 combo = 3배, -5는 3 combo = 4배, 수학적으로 3콤까지가 제일 효율적
for i in range(6, N+1):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[-1])