while True:
    try:
        a, b = map(int, input().split())
        print(int(b//(a+1)))
    except EOFError:
        break