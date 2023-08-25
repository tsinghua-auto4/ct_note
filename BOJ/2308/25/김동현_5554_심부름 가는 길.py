
target = [int(input()) for _ in range(4)]
a, b = sum(target)//60, sum(target)%60
print(a)
print(b)