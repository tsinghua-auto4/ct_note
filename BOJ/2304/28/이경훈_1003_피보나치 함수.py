T = int(input())

check = [[0, 0] for _ in range(41)]

check[0] = [1, 0]
check[1] = [0, 1]

for i in range(2, 41):
    check[i][0] = check[i-1][0] + check[i-2][0]
    check[i][1] = check[i-1][1] + check[i-2][1]

for _ in range(T):
    a = int(input())
    print(*check[a])
