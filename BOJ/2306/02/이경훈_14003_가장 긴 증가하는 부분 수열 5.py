from bisect import bisect_left as bl
N = int(input())
A = list(map(int, input().split()))

lis = []
temp = []
ans = []
for a in A:
    if not lis or lis[-1] < a:
        lis.append(a)
        temp.append((len(lis)-1, a))
    else:
        lis[bl(lis, a)] = a
        temp.append((bl(lis, a), a))

num = len(lis) - 1

for i in reversed(range(len(temp))):
    if num == -1:
        break

    if temp[i][0] == num:
        ans.append(temp[i][1])
        num -= 1
print(len(lis))
print(*reversed(ans))