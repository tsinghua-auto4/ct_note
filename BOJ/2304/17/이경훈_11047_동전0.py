import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [0]
for i in range(N):
   coin.append(int(input()))

cnt = 0
while(K!=0):
   cnt += K // coin[N]
   K %= coin[N]
   N -= 1

print(cnt)