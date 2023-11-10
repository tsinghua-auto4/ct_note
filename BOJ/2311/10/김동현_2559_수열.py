N, K = map(int, input().split())
data = list(map(int, input().split()))

ans = 100000*(-100)-1

tmp = sum(data[:K])
ans = max(ans, tmp)
for iter in range(K, N):
    tmp -= data[iter-K]
    tmp += data[iter]
    ans = max(ans, tmp)

print(ans)