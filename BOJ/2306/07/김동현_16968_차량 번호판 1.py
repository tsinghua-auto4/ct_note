

num, alp = 10, 26

target = ' ' + input()
ans = 1

for idx in range(1, len(target)):
    cur = target[idx]
    if cur == 'c':
        if target[idx-1] == 'c':
            ans *= (alp-1)
        else:
            ans *= alp
    elif cur == 'd':
        if target[idx-1] == 'd':
            ans *= (num-1)
        else:
            ans *= num

print(ans)