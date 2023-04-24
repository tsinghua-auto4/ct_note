import sys

limit = 1000000

dp_each = [0]*(limit+1)
dp_accu = [0]*(limit+1)

for i in range(1, limit+1):
    j = 1
    while i*j <= limit:
        dp_each[i*j] += i
        j += 1
    dp_accu[i] = dp_accu[i-1] + dp_each[i]

for _ in range(int(sys.stdin.readline())):
    sys.stdout.write(str(dp_accu[int(sys.stdin.readline())])+'\n')