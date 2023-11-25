data    = list(map(int, input().split()))
x, y, r = map(int, input().split())

flag = False
for iter in range(4):
    if data[iter] == x:
        print(iter+1)
        flag = True
        break
if not flag:
    print(0)