from itertools import combinations

parents = None

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y:
        return False
    else:
        if x < y:
            x, y = y, x
        parents[y] = x
        return True

def solution(n, wires):
    answer = int(1e9)
    length = len(wires)
    for candi in combinations(wires, length-1):
        global parents
        parents = [i for i in range(n + 1)]
        
        for x, y in candi:
            union_set(x, y)
            
        for i in range(n):
            find_set(i)
            
        temp = parents[1]
        first, second = 0, 0
        
        for ele in parents[1:]:
            if ele == temp:
                first += 1
            else:
                second += 1
        
        answer = min(answer, abs(first-second))
    
    return answer