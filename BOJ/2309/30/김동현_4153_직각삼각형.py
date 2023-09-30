import sys

while True:
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    data.sort()
    a, b, c = data
    if a + b + c == 0:
        break
    else:
        if a**2 + b**2 == c**2:
            sys.stdout.write("right" + "\n")
        else:
            sys.stdout.write("wrong" + "\n")