import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visit        = [-1] * (n+1)
    visit[start] = 0
    ans = [0, 0] # [distance, node]

    while queue: # 흔한 bfs, 마지막에 내가 찾는 가장 먼 거리의 노드를 갱신해주는 로직만 이해하자
        cur = queue.popleft()
        for p, w in graph[cur]:
            if visit[p] == -1:
                visit[p] = visit[cur] + w
                queue.append(p)
                if ans[0] < visit[p]:
                    ans = visit[p], p
    return ans

if __name__ == "__main__":
    n     = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        cur = list(map(int, sys.stdin.readline().split()))
        graph[cur[0]].append((cur[1], cur[2])) # 현재노드 - (연결 된 노드, 길이) 관계 저장
        graph[cur[1]].append((cur[0], cur[2]))
    
    dist, node = bfs(1) #1에서 가장 먼 노드를 찾자
    dist, node = bfs(node) # 1에서 가장 먼 노드에서 가장 먼 노드의 거리를 구하면 지름!
    print(dist)
