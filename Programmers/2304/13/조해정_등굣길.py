def solution(m, n, puddles):
    graph = [[0 for _ in range(m + 1)]] + [[-1 for i in range(m + 1)] for j in range(n)]
    for _ in range(n + 1):
        graph[_][0] = 0

    for i, j in puddles:
        graph[j][i] = 0

    graph[1][1] = 1
    # 길 찾기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == -1:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    return graph[-1][-1] % 1000000007
