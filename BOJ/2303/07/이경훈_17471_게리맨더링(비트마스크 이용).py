import sys

input = sys.stdin.readline


# 부모노드집합 초기화
def makeSet():
  parents.clear()
  for i in range(N):
    parents.append(i)


# 부모노드 찾기
def findSet(i):
  if parents[i] != i:
    parents[i] = findSet(parents[i])
  return parents[i]


# 병합하기
def unionSet(a, b):
  if findSet(a) == findSet(b):
    return False
  else:
    parents[findSet(b)] = findSet(a)
    return True


N = int(input())
population = list(map(int, input().split()))
adj_matrix = [[False for _ in range(N)] for _ in range(N)]
parents = []
ans = []

for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(1, len(temp)):
    adj_matrix[i][temp[j] - 1] = True

# 비트마스킹으로 두 그룹으로 만들고
for i in range(1, 1 << N - 1):
  temp1 = 0
  temp2 = 0
  fst = []
  snd = []
  fail = False
  for j in range(N):
    if (i & 1 << j) == 0:
      fst.append(j)
    else:
      snd.append(j)
  makeSet()
  # 그룹안에서 부모노드를 갱신하면서 다른 친구가 있다면 결과에 포함하지 않음
  for f1 in fst:
    for f2 in fst:
      if adj_matrix[f1][f2]:
        unionSet(f1, f2)
  temp = findSet(fst[0])
  for f in fst:
    if temp != findSet(f):
      fail = True

  for s1 in snd:
    for s2 in snd:
      if adj_matrix[s1][s2]:
        unionSet(s1, s2)
  temp = findSet(snd[0])
  for s in snd:
    if temp != findSet(s):
      fail = True
  # 실패가 아니라면 인구수 차를 ans에 넣어줌
  if not fail:
    for f in fst:
      temp1 += population[f]
    for s in snd:
      temp2 += population[s]
    ans.append(abs(temp1 - temp2))
if ans:
  print(min(ans))
else:
  print(-1)
