import sys

input = sys.stdin.readline

N, L, R, X = map(int, input().split())

quest = list(map(int, input().split()))
quest.sort()
cnt = 0

for i in range(1, 1 << N):
   sum = 0
   check = []
   for j in range(0, N):
       if (i & 1 << j) == 0:
           continue
       check.append(j)
       sum += quest[j]

   if sum > R:
       continue

   if sum < L:
       continue

   if quest[check[-1]] - quest[check[0]] < X:
       continue
   cnt += 1
print(cnt)