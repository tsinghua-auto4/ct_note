target = []
for _ in range(7):
    cur = int(input())
    if cur%2 == 1:
        target.append(cur)
if len(target):
    target.sort()
    print(sum(target))
    print(target[0])
else:
    print(-1)