ans = []
for iter in range(1,6):
    cur = str(input())
    if "FBI" in cur:
        ans.append(iter)
if len(ans) > 0:
    print(*ans)
else:
    print("HE GOT AWAY!")