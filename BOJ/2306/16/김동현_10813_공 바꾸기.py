N, M = map(int, input().split())
mem  = list(range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    mem[a], mem[b] = mem[b], mem[a]

print(*mem)