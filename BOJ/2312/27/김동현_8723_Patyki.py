data = list(map(int, input().split()))
data.sort()
a, b, c = data

if c**2 == b**2+a**2 and c!=b!=a:
    print(1)
elif c == b == a and c**2 != b**2 + a**2:
    print(2)
else:
    print(0)