from collections import deque

N, K = map(int, input().split())
tar  = deque(list(range(1, N+1)))

ans = []
while len(tar):
    for _ in range(K-1):
        tar.append(tar.popleft())
    ans.append(str(tar.popleft()))

print('<'+', '.join(ans)+'>')