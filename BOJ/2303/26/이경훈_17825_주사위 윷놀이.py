import sys

input = sys.stdin.readline

GRAPH = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12],
         [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23],
         [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]

SCORE = [
  0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
  40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0
]

dice = list(map(int, input().split()))
answer = 0


def backtracking(cnt, horse, sum_val):
  global answer
  if cnt == 10:
    answer = max(answer, sum_val)
    return

  for i in range(4):
    x = horse[i]
    if len(GRAPH[x]) == 2:
      nx = GRAPH[x][1]
    else:
      nx = GRAPH[x][0]
    for j in range(1, dice[cnt]):
      nx = GRAPH[nx][0]
      if nx == 32:
        break
    if nx == 32 or nx not in horse:
      temp = horse[i]
      horse[i] = nx
      backtracking(cnt + 1, horse, sum_val + SCORE[nx])
      horse[i] = temp


backtracking(0, [0, 0, 0, 0], 0)
print(answer)
