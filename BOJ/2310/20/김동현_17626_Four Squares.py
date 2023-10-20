import math

N  = int(input())
dp = [0, 1]

for i in range(2, N+1):
    minim = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minim = min(minim, dp[i - j**2])
    dp.append(minim+1)

print(dp[N])