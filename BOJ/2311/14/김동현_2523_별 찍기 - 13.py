N = int(input())

cur = ''
for _ in range(N):
    cur += '*'
    print(cur)
for _ in range(N-1):
    cur = cur[:-1]
    print(cur)