L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

while True:
    L -= 1
    A -= C
    B -= D
    if A <= 0 and B <= 0:
        break

print(L)