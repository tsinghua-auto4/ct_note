N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

answer = []
num = max(dp)

for i in reversed(range(N)):
    if num == 0:
        break
    if dp[i] == num:
        answer.append(A[i])
        num -= 1
answer.reverse()
print(*answer)