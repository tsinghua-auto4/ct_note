
while True:
    a, b = map(int, input().split())
    if a+b == 0:
        break

    if a > b and a%b == 0:
        print("multiple")
    elif a < b and b%a == 0:
        print("factor")
    else:
        print("neither")