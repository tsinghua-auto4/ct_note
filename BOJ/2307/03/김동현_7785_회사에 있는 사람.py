ans = set()
T = int(input())
for _ in range(T):
    target, op = map(str, input().split())
    if op == 'enter':
        ans.add(target)
    else:
        ans.discard(target)

ans = list(ans)
ans = sorted(ans, reverse=True)
for iter in ans:
    print(iter)