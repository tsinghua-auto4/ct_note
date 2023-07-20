
T = int(input())

ans = 0
mem = set()

for _ in range(T):
    cur = str(input())

    if cur == "ENTER":
        ans += len(mem)
        mem = set()
    else:
        mem.add(cur)

ans += len(mem)
print(ans)