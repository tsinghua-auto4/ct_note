

s, n = map(int, input().split())
n = str(n)

h, v = '-', '|'
def construct(n):
    lcd = [[' ']*(s+2) for _ in range(2*s + 3)]
    for i in range(1, s+1):
        if n in '02356789':
            lcd[0][i] = h
        if n in '01234789':
            lcd[i][-1] = v
        if n in '013456789':
            lcd[s+1+i][-1] = v
        if n in '0235689':
            lcd[2*s+2][i] = h
        if n in '0268':
            lcd[s+1+i][0] = v
        if n in '045689':
            lcd[i][0] = v
        if n in '2345689':
            lcd[s+1][i] = h
    return lcd

display = [construct(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()