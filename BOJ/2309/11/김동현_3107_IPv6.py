target = list(map(str, input().split(":")))
if target[0] == "":
    target = target[1:]
if target[-1] == "":
    target = target[:-1]

ans = ""
for cur in target:
    if cur == "":
        ans += '0000:'*(8-len(target)+1)
    else:
        ans += cur.zfill(4) + ":"

print(ans[:-1])