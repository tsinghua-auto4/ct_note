l, p = map(int, input().split())
data = list(map(int, input().split()))
ans  = []
for cur in data:
    ans.append(cur-l*p)
print(*ans)