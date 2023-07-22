N, M = map(int, input().split())

mem_hash = {}
for _ in range(N):
    cur = input()
    if len(cur) < M:
        continue
    if cur not in mem_hash:
        mem_hash[cur] = 1
    else:
        mem_hash[cur] += 1

mem_sort = sorted(mem_hash.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for ans in mem_sort:
    print(ans[0])