n = int(input())
ans = 0

for i in range(1, n+1): # 1부터 n까지
  ans += i * (n // i) # i와 n을 i로 나눈 몫을 곱해서 계속 더한다
print(ans)