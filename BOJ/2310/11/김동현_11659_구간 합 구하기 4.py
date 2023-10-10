n, m = map(int, input().split())
data = list(map(int, input().split()))

memo = [0]
tmp = 0
for iter in data:
    tmp += iter
    memo.append(tmp)

for _ in range(m):
    a, b = map(int, input().split())
    ans = memo[b] - memo[a-1]
    print(ans)