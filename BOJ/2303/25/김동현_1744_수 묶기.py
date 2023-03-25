import sys

n    = int(sys.stdin.readline().rstrip())
posi = []
nega = [] # 0 포함

for idx in range(n):
    cur = int(sys.stdin.readline().rstrip())
    if cur > 0:
        posi.append(cur)
    else:
        nega.append(cur)

posi.sort(reverse=True)
nega.sort()

ans = 0
idx = 0
# 음수는 음수끼리 곱하거나, 0과 곱해서 최대로 만들고
while idx < len(nega):
    if idx + 1 < len(nega):
        ans += nega[idx]*nega[idx + 1]
        idx = idx + 2
    else:
        ans += nega[idx]
        idx += 1

# 양수는 양수끼리 곱하거나 냅두자
idx = 0
while idx < len(posi):
    if idx + 1 < len(posi) and posi[idx+1] != 1:
        ans += posi[idx]*posi[idx + 1]
        idx = idx + 2
    else:
        ans += posi[idx]
        idx += 1

print(ans)