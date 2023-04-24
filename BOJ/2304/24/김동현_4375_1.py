
while True:
    try:
        target = int(input())
    except:
        break

    num = 0
    i = 1

    while True:
        num = num*10 + 1
        num %= target # (a*b)%c == (a%c*b%c)%c

        if num == 0:
            print(i)
            break
        i += 1