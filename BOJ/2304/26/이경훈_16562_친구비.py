import sys

input = sys.stdin.readline

N, M, k = map(int, input().split())
parents = [i for i in range(N+1)]
check = [False for i in range(N+1)]
sum_val = 0

def find(v):
   if v == parents[v]:
       return v
   parents[v] = find(parents[v])
   return parents[v]

def union(u, v):
   u = find(u)
   v = find(v)
   if u == v:
       return False
   if(cost[u] >= cost[v]):
       parents[u] = v
   else:
       parents[v] = u
   return True

cost = [0]+ list(map(int, input().split()))
for _ in range(M):
   u, v = map(int, input().split())
   union(u, v)

for i in range(1, N+1):
   find(i)

for i in range(1, N+1):
   if check[parents[i]]:
       continue
   sum_val += cost[parents[i]]
   check[parents[i]] = True

if k >= sum_val:
   print(sum_val)
else:
   print('Oh no')