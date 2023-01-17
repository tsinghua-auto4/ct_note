# pypy로 해결함

def cal(target):
    sum = 0
    for i in range(len(target)):
        for j in range(len(target)):
            if i != j:
                sum += data[target[i]][target[j]]
    return sum

def comb(s, cnt, n):
    global ans, mark
    if cnt == n:
        link, start = [], []
        for i in range(N):
            if mark[i]:
                link.append(i)
            else:
                start.append(i)
        if len(link) * len(start) == 0:
            return
        ans = min(ans, abs(cal(link) - cal(start)))
        return
    for i in range(s, N):
        mark[i] = True
        comb(i+1, cnt+1, n)
        mark[i] = False

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
link, start = [], []

mark = [False] * N
for i in range(1, N//2+1):
    comb(0, 0, i)
print(ans)