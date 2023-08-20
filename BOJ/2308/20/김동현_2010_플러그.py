N = int(input())

ans = -(N-1)
for _ in range(N):
    ans += int(input())

print(ans)