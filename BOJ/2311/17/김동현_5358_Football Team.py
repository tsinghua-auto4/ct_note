while True:
    try:
        s = input()
        for i in range(len(s)) :
            if s[i] == 'e' : print("i", end = "")
            elif s[i] == 'i' : print("e", end = "")
            elif s[i] == 'E' : print("I", end = "")
            elif s[i] == 'I' : print("E", end = "")
            else : print(s[i], end = "")
        print()
    except EOFError:
        break