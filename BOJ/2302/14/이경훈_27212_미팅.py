import sys
input = sys.stdin.readline

# 입력
n, m, c = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(c)]
A = list(map(lambda x: int(x)-1, input().split()))
B = list(map(lambda x: int(x)-1, input().split()))

# dp[i][j] : A대학 0부터 i까지의 사람과 B대학 0부터 j까지의 사람들이 미팅 했을 때 만족도 합의 최대값
dp = [[0] * m for _ in range(n)]

# dp[i][j]는 3가지 경우로 나뉜다.     
for i in range(n):
  for j in range(m):
    # 1) A[i]와 B[j]가 매칭 된 경우
    solution_1 = W[A[i]][B[j]]
    if i > 0 and j > 0:
      solution_1 += dp[i-1][j-1]

    # 2) A[i]가 쓰이지 않은 경우
    solution_2 = 0
    if i > 0:
      solution_2 = dp[i-1][j]

    # 3) B[j]가 쓰이지 않은 경우
    solution_3 = 0
    if j > 0:
      solution_3 = dp[i][j-1]

    # 그중에 최대값을 구함
    dp[i][j] = max(solution_1, solution_2, solution_3)

# dp의 정의가 A[0...i] B[0...j]이므로, 0을 고려해서 하나를 빼줘야 함
print(dp[n-1][m-1])