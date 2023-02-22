import sys

def solution(depth, r, c, graph, visited):
    global max_len, dx, dy
    max_len = max(max_len, depth)
    
    for i in range(4):
        cx, cy = r + dx[i], c + dy[i]
        if 0<= cx < R and 0<= cy < C and visited[graph[cx][cy]] == 0:
                visited[graph[cx][cy]] = 1
                solution(depth+1, cx, cy, graph, visited)
                visited[graph[cx][cy]] = 0
    return max_len


R, C  = map(int, sys.stdin.readline().split())
graph = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [0]*26
visited[graph[0][0]] = 1

max_len = 1

solution(1, 0, 0, graph, visited)
print(max_len)