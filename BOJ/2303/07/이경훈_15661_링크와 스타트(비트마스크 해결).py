import sys

input = sys.stdin.readline


def combi(cnt, start, team):
  global sum_val
  if cnt == 2:
    sum_val += ability[combiList[0]][combiList[1]]
    sum_val += ability[combiList[1]][combiList[0]]
    return
  for i in range(start, len(team)):
    combiList.append(team[i])
    combi(cnt + 1, i + 1, team)
    combiList.pop(-1)


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
combiList = []
ans = []
a_list = []
b_list = []
for i in range(1, 1 << N - 1):
  teamA = []
  teamB = []
  sum_val = 0
  for j in range(N):
    if (i & 1 << j) == 0:
      teamA.append(j)
    else:
      teamB.append(j)
  if len(teamA) > 1:
    combi(0, 0, teamA)
    sumA = sum_val
  else:
    sumA = 0
  sum_val = 0
  if len(teamB) > 1:
    combi(0, 0, teamB)
    sumB = sum_val
  else:
    sumB = 0

  ans.append(abs(sumA - sumB))
print(min(ans))
