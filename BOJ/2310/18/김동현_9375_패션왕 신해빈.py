T = int(input())
for _ in range(T):
    n = int(input())
    cloth = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if b in cloth.keys():
            cloth[b] += 1
        else:
            cloth[b] = 2
    ans = 1
    for key in cloth.keys():
        ans *= cloth[key]
    print(ans-1)