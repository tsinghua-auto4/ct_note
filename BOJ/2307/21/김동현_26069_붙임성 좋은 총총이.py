T = int(input())

ans = 0
mem = dict()
mem['ChongChong'] = 1

for _ in range(T):
    a, b = map(str, input().split())
    if a not in mem:
        mem[a] = 0
    if b not in mem:
        mem[b] = 0
    
    if mem[a] == 1 or mem[b] == 1:
        mem[a] = 1
        mem[b] = 1

for key in mem.keys():
    ans += mem[key]

print(ans)