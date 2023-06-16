N, M = map(int, input().split())
mem  = list(range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tmp = list(reversed(mem[a:b+1]))
    for idx in range(a, b+1):
        mem[idx] = tmp[idx-a]

print(*mem)