N = int(input())
datas = list(map(int, input().split()))

Y, M = 0, 0
for data in datas:
    Y += (data//30 + 1) * 10
    M += (data//60 + 1) * 15

if Y < M:
    print("Y", Y)
elif M < Y:
    print("M", M)
else:
    print("Y M", M)