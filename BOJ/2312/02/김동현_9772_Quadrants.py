while True:
    a, b = map(float, input().split())
    if a == 0 and b == 0:
        print("AXIS")
        break
    elif a > 0 and b > 0:
        print("Q1")
    elif a < 0 and b > 0:
        print("Q2")
    elif a < 0 and b < 0:
        print("Q3")
    elif a > 0 and b < 0:
        print("Q4")
    else:
        print("AXIS")