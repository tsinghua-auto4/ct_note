
target = int(input())

ans = 0
for i in range(1, target+1):
    ans += (target//i)*i
print(ans)