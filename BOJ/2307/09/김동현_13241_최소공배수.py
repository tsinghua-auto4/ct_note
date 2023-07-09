a, b = map(int, input().split())
ans  = a*b

while b:
    if a > b:
        a, b = b, a
    b %= a

print(ans//a)