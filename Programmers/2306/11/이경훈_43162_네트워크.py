def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return False
    else:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y
        return True
    
def solution(n, computers):
    global parents
    answer = set()
    parents = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)
    for p in parents:
        answer.add(find(p))
    return len(answer)