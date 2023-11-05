A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    time = -A * C + D + B * E
else:
    time = (B - A) * E

print(time)