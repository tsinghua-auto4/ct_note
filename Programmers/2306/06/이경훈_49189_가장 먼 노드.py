from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for (a, b) in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque()
    q.append(1)
    visited[1] = 0
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] != -1:
                continue
            visited[next] = visited[now] + 1
            q.append(next)
            
    max_val = max(visited)
    answer = visited.count(max_val)
    return answer