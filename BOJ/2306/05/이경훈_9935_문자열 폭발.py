String = input().rstrip()
bomb = input().rstrip()
stk = []
last = bomb[-1]
for s in String:
    stk.append(s)
    if s == last:
        if len(stk) >= len(bomb):
            if ''.join(stk[-len(bomb):]) == bomb:
                for i in range(len(bomb)):
                    stk.pop()

if stk:
    print(''.join(stk))
else:
    print('FRULA')