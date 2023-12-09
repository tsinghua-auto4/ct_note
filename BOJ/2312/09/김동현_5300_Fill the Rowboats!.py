target = int(input())
ans = []
for iter in range(1, target+1):
    ans.append(iter)
    if iter%6 == 0:
        ans.append("Go!")

if ans[-1] != 'Go!':
    ans.append("Go!")

print(*ans)