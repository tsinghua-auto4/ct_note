moum = {}
moum['a'] = 0
moum['e'] = 0
moum['i'] = 0
moum['o'] = 0
moum['u'] = 0
moum['A'] = 0
moum['E'] = 0
moum['I'] = 0
moum['O'] = 0
moum['U'] = 0

while True:
    cur = input()
    if cur == "#":
        break
    ans = 0
    for c in cur:
        if c in moum:
            ans += 1
    print(ans)