

N = int(input())
K = int(input())

prime = [0 for _ in range(N+1)]
for cur in range(2, N+1):
    if prime[cur] == 0:
        for t in range(cur, N+1, cur):
            if t % cur == 0:
                prime[t] = max(prime[t], cur)

ans = 0
for cur in prime:
    if cur <= K:
        ans += 1
print(ans-1)