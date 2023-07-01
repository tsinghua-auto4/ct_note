target = int(input())
ans = 0
for i in range(1, 1000000+1):
    if i + sum(map(int, list(str(i)))) == target:
        ans = i
        break
print(ans)