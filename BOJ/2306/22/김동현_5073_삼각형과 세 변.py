
while True:
    a, b, c = map(int, input().split())
    if a + b + c == 0:
        break

    if not(a < b+c and b < a+c and c < a+b):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")