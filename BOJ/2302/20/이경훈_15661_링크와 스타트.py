import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(1, N + 1)]
ans = []

# N명을 을 두 팀으로 나누되, 각각의 팀은 한명 이상이어야 하므로
# i명만큼 뽑아서 한 팀을 만들고 나머지 N-i명으로 한 팀을 만든다.
# 이때, i는 N의 절반보다 1 클때까지
for i in range(1, N // 2 + 1):
  for start_team in combinations(people, i):
    team1, team2 = 0, 0
    # 1명일때는 무조건 0점
    if len(start_team) >= 2:
      for ii, jj in combinations(start_team, 2):
        team1 += data[ii - 1][jj - 1] + data[jj - 1][ii - 1]
    link_team = [person for person in people if person not in start_team]
    if len(link_team) >= 2:
      for ii, jj in combinations(link_team, 2):
        team2 += data[ii - 1][jj - 1] + data[jj - 1][ii - 1]
    ans.append(abs(team1 - team2))
print(min(ans))
