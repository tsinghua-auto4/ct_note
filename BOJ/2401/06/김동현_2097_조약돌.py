N = int(input())
if N < 3:
    print(4)
    exit()
for iter in range(2, N):
    if N <= iter**2:
        print((iter-1)*4)
        break
    elif N <= iter*(iter+1):
        print((iter-1)*4+2)
        break