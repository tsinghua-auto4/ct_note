
a, b, c = map(int, input().split())

while True:
    flag1, flag2, flag3 = False, False, False
    if a < b+c:
        flag1 = True
    else:
        a = b+c-1
    
    if b < a+c:
        flag2 = True
    else:
        b = a+c-1
    
    if c < a+b:
        flag3 = True
    else:
        c = a+b-1
    
    if flag1 == True and  flag2 == True and flag3 == True:
        print(a+b+c)
        break