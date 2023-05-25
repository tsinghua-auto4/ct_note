

a, b, c = map(int, input().split())

ops = ['+', '-', '*', '/']

for op in ops:
    if op == '+':
        if a == b+c:
            print("{}={}+{}".format(a,b,c))
            break
        elif a+b == c:
            print("{}+{}={}".format(a,b,c))
            break
    elif op == '-':
        if a == b-c:
            print("{}={}-{}".format(a,b,c))
            break
        elif a-b == c:
            print("{}-{}={}".format(a,b,c))
            break
    elif op == '*':
        if a == b*c:
            print("{}={}*{}".format(a,b,c))
            break
        elif a*b == c:
            print("{}*{}={}".format(a,b,c))
            break
    elif op == '/':
        if a == b//c:
            print("{}={}/{}".format(a,b,c))
            break
        elif a//b == c:
            print("{}/{}={}".format(a,b,c))
            break