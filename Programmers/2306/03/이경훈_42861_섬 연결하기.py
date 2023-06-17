parents = []

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if x >= y:
            parents[y] = x
        else:
            parents[x] = y
        return True
            
def solution(n, costs):
    answer = 0
    global parents
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    for fr, to, cost in costs:
        if union(fr, to):
            answer += cost
    return answer