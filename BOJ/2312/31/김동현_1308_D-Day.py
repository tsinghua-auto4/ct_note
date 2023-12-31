from datetime import *

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

if d1[0] + 1000 < d2[0]:
    print("gg")
elif d1[0] + 1000 == d2[0] and (d1[1], d1[2]) <= (d2[1], d2[2]):
    print("gg")
else:
    d1 = date(*d1)
    d2 = date(*d2)
    print("D-{}".format(d2.toordinal()-d1.toordinal()))