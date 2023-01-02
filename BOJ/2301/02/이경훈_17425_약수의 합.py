import sys

input = sys.stdin.readline

MAX = 1000000 # 최대값 설정

f = [1] * (MAX+1) # f(x)의 값

g = [0] * (MAX+1) # g(x)의 값

for i in range(2, MAX+1):
  for j in range(i, MAX+1, i): # 에라토스테네스의 채를 이용
    f[j] += i

for i in range(1, MAX+1):
  g[i] = g[i-1] + f[i] # g[i]의 누적 값을 구함

n = int(input())
ans = []

for i in range(n):
  n = int(input())
  ans.append(g[n])
print('\n'.join(map(str, ans))) # 그냥 매번 print 하는 것 보다 이렇게 append해서 한번에 print 해주는게 훨씬 빠름