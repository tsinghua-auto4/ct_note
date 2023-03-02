import sys
from collections import deque

def solution(_num, _tar, _visit):
    queue = deque([(_num, "")])

    while queue:
        cur, path = queue.popleft()
        if cur == _tar:
            return path
        
        nxt = (cur*2)%10000
        if not _visit[nxt]:
            _visit[nxt] = True
            queue.append((nxt, path + 'D'))

        nxt = (cur-1)%10000
        if not _visit[nxt]:
            _visit[nxt] = True
            queue.append((nxt, path + 'S'))
        
        nxt = (10*cur+(cur//1000))%10000
        if not _visit[nxt]:
            _visit[nxt] = True
            queue.append((nxt, path + 'L'))
        
        nxt = (cur//10+(cur%10)*1000)%10000
        if not _visit[nxt]:
            _visit[nxt] = True
            queue.append((nxt, path + 'R'))



T     = int(sys.stdin.readline().rstrip())
visit = [False]*10000

for _ in range(T):
    num, tar = map(int, sys.stdin.readline().split())
    
    visit = [False]*10000

    print(solution(num, tar, visit))