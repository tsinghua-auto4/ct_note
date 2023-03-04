import sys

input = sys.stdin.readline


def dfs(cnt, sum_val):  # cnt는 횟수, sum_val은 만들어 낼 수 있는 무게
  if dp[cnt][sum_val]:  # 만약 이미 참인 값이 들어오면 리턴
    return

  dp[cnt][sum_val] = True  # 만들어 낼 수 있는 값이므로 true 할당

  if cnt == weight_num:  # 있는 추를 다 썼다면 리턴
    return

  dfs(cnt + 1, sum_val)  # 현재의 추를 올려 놓지 않음
  dfs(cnt + 1, sum_val + weights[cnt])  # 현재의 추를 올려 놓음
  dfs(cnt + 1, abs(sum_val - weights[cnt]))  # 현재의 추를 구슬 쪽에 놓음으로써 사실상 뺌


weight_num = int(input())  # 추 개수
weights = list(map(int, input().split()))  # 추의 무게들
bead_num = int(input())  # 구슬의 개수
beads = list(map(int, input().split()))  # 구슬의 무게들

dp = [[False for _ in range(55001)] for _ in range(weight_num + 1)
      ]  # dp[i][j] i번째의 추까지 고려할 때 j의 무게를 만들어 낼 수 있는지 담는 불리언 배열

dfs(0, 0)

for i in beads:
  if dp[weight_num][i]:
    print('Y', end=" ")
  else:
    print('N', end=" ")
