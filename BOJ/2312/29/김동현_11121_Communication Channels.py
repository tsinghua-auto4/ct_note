T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    if a == b:
        print("OK")
    else:
        print("ERROR")