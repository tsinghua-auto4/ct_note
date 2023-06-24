def solution(n, results):
    answer = 0
    table = [['?' for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][i] = 'SELF'
    for a, b in results:
        table[a][b] = 'WIN'
        table[b][a] = 'LOSE'
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if table[i][k] == table[k][j] and table[i][k] != '?':
                    table[i][j] = table[i][k]

    for i in range(1, n+1):
        if '?' not in table[i][1:]:
            answer += 1
    return answer