for _ in range(int(input())):
    target = int(input())
    ans = []
    for cur in [25, 10, 5, 1]:
        ans.append(target//cur)
        target -= cur * (target//cur)
    print(*ans)