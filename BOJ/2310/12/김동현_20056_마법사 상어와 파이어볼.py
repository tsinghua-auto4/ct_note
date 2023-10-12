import sys

def moving():
    global move, N, M, graph
    n_graph = [[[] for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for fireball in graph[r][c]:
                cr, cc = r, c
                cm, cs, cd = fireball

                dr, dc = move[cd]
                nr, nc = (cr+dr*cs)%N, (cc+dc*cs)%N

                n_graph[nr][nc].append([cm, cs, cd])
    
    return n_graph

def fusion():
    global move, N, M, graph

    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) <= 1:
                continue
            nm = 0
            ns = 0
            nd = []
            ds = []
            
            for fireball in graph[r][c]:
                cm, cs, cd = fireball
                nm += cm
                ns += cs
                ds.append(cd%2)

            nm //= 5
            if nm == 0:
                graph[r][c] = []
                continue
            ns //= len(graph[r][c])

            nd = [0, 2, 4, 6]
            for iter in range(1, len(graph[r][c])):
                if ds[iter-1] != ds[iter]:
                    nd = [1, 3, 5, 7]
                    break
            
            graph[r][c] = []
            for iter_nd in nd:
                graph[r][c].append([nm, ns, iter_nd])


move  = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph   = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())

    graph[r-1][c-1].append([m, s, d])

for _ in range(K):
    graph = moving()
    fusion()

ans = 0
for r in range(N):
    for c in range(N):
        for fireball in graph[r][c]:
            ans += fireball[0]
print(ans)