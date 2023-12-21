N    = int(input())
data = list(map(int, input().split()))

point = 0
ans   = 0

for cur in data:
    if cur == 0:
        point = 0
    else:
        point += 1
        ans += point

print(ans)