for _ in range(3):
    data = list(map(int, input().split()))
    len_0 = data.count(0)
    if len_0 == 1:
        print("A")
    elif len_0 == 2:
        print("B")
    elif len_0 == 3:
        print("C")
    elif len_0 == 4:
        print("D")
    else:
        print("E")