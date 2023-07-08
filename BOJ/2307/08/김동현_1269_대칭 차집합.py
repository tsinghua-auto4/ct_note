size_a, size_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

cnt = 0
for iter in a:
    if iter not in b:
        cnt += 1
for iter in b:
    if iter not in a:
        cnt += 1
print(cnt)