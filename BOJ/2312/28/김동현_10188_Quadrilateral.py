T = int(input())
for _ in range(T):
    c, r = map(int, input().split())
    stars = 'X'*c
    for _ in range(r):
        print(stars)
    print()