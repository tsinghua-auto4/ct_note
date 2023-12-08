from copy import deepcopy

print("Gnomes:")
for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = deepcopy(a)
    c = deepcopy(a)
    b.sort()
    c.sort(reverse=True)
    if a == b or a == c:
        print("Ordered")
    else:
        print("Unordered")