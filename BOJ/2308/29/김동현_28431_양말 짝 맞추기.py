socks = dict()

for _ in range(5):
    cur = int(input())
    if cur not in socks.keys():
        socks[cur] = 0
    elif socks[cur] == 0:
        socks[cur] = 1
    elif socks[cur] == 1:
        socks[cur] = 0

for cur in socks.keys():
    if socks[cur] == 0:
        print(cur)
        break