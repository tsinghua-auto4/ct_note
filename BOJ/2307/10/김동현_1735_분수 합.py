
a, b = map(int, input().split())
c, d = map(int, input().split())

A, B = a*d+c*b, b*d

e, f = A, B
while e != 0:
    t=f%e
    f=e
    e=t

print(A//f, B//f)