N = int(input())
target = input()

ans = 0
for idx in range(N):
    c = target[idx]
    tmp = ord(c)-96
    ans += tmp*31**idx
print(ans%1234567891)