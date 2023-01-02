import sys
input = sys.stdin.readline
n_list = list(map(int, input().split()))
cnt = 0
m = max(n_list)
minors = [2]
for i in range(3, m+1):
    if i % 2 == 0:
        continue
    else:
        is_minor = True
    for j in range(2, i):
        if i % j == 0:
            is_minor = False
            break
    if is_minor:
        minors.append(i)
for n in n_list:
    if n in minors:
        cnt += 1
print(cnt)
