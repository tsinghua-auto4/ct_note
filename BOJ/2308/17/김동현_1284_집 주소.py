
length = {}
for iter in range(10):
    length[iter] = 3
length[0] = 4
length[1] = 2

while True:
    target = input()
    if target == '0':
        break
    ans = 2 + len(target)-1
    for cur in target:
        ans += length[int(cur)]
    print(ans)