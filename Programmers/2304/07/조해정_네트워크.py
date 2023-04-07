from collections import deque

visited = []
answer = 0


def solution(n, computers):
    global visisted, answer

    visited = [False] * n
    coms = deque([i for i in range(n)])
    dic = {}

    for i in range(n):
        dic[i] = []
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                dic[i].append(j)

    while coms:
        nets = []
        nodes = deque([])
        nodes.append(coms.popleft())

        while nodes:
            v = nodes.popleft()
            if not visited[v]:
                for d in dic[v]:
                    if not visited[d]:
                        nodes.append(d)
                visited[v] = True
            nets.append(v)

        coms = deque(list(set(coms) - set(nets)))
        answer += 1

    return answer
