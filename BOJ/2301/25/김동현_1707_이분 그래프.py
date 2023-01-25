import sys
from collections import deque

input = sys.stdin.readline

def solution(start):#bfs
    global link, mark

    queue = deque([start])
    if mark[start] == 0:
        mark[start] = 1
    
    while queue:
        cur = queue.popleft()
        status = mark[cur]
        
        for i in link[cur]:
            if mark[i] == 0:
                queue.append(i)
                if status == 1:
                    mark[i] = 2
                else:
                    mark[i] = 1
            elif mark[i] == status:
                print("NO")
                return False
    return True


if __name__ == "__main__":
    k = int(input().rstrip())
    mark = []
    link = []

    for _ in range(k):
        v, e = map(int, input().split())
        mark = [0] * (v + 1)
        link = [[] for __ in range(v+1)]
        for ___ in range(e):
            a, b = map(int, input().split())
            link[a].append(b)
            link[b].append(a)
        flag = 0
        for i in range(1, v+1):
            if not solution(i):
                flag = 1
                break
        if flag == 0:
            print("YES")
