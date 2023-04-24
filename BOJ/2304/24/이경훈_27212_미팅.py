import sys

input = sys.stdin.readline

# 점화식
# dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + W[i][j])
# 즉, A대학 i번째 학생까지 고려하고 B대학 j번째 학생까지 고려 했을 때 미팅의 만족도 합의 최대

# 다음과 경우로 나뉜다.
# 1. A대학 i번째 학생이 악수를 못함
# 2. B대학 j번째 학생이 악수를 못함
# 3. A대학 i번째 학생과 B대학 j번째 학생이 악수를 함
# 이중에서 최대값을 구한다.

# 처음 값 들을 0을 추가함으로써 초기값 설정 pass

N, M, C = map(int, input().split())
W = [[0 for _ in range(C + 1)]]
for i in range(C):
    W.append([0] + list(map(int, input().split())))

A_personality = [0] + list(map(int, input().split()))
B_personality = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + W[A_personality[i]][B_personality[j]])

print(dp[N][M])
