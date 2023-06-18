target = []
length = 0
for _ in range(5):
    tmp    = list(input())
    length = max(length, len(tmp))
    target.append(tmp)

for idx in range(5):
    if len(target[idx]) < length:
        for _ in range(length-len(target[idx])):
            target[idx].append(' ')

ans = ''
for r in range(length):
    for c in range(5):
        if target[c][r] != ' ':
            ans += target[c][r]
print(ans)