def Op_R(target: list[list]):
    graph = []
    for cr in range(len(target)):
        cur = target[cr]
        # [숫자, 개수] 형식으로 리스트를만들자
        elems = set(cur)
        mem = []
        for elem in elems:
            if elem == 0:
                continue
            mem.append((elem, cur.count(elem)))
        # 그 다음 lambda로 정렬
        mem.sort(key = lambda x: (x[1], x[0]))
        # 새로운 리스트 생성해서 extend로 넣어주자
        new_cur = []
        for iter in mem:
            new_cur.append(iter[0])
            new_cur.append(iter[1])
        # graph에 넣어줌
        graph.append(new_cur)
    
    # 길이 맞춰줌
    max_len = max(map(len,graph))
    for i in range(len(graph)):
        while len(graph[i]) != max_len:
            graph[i].append(0)

    target.clear()
    for cr in range(len(graph)):
        target.append(list(graph[cr]))


def Op_C(target: list[list]):
    # target 시계 반대 방향 회전
    graph = list(map(list, zip(*target)))[::-1]
    # Op_R 호출
    Op_R(graph)
    # target 시계 방향 회전
    new_graph = list(map(list, zip(*graph[::-1])))
    
    target.clear()
    for cr in range(len(new_graph)):
        target.append(new_graph[cr])


def solution(r: int, c: int, k: int, target: list[list]):
    time = 0
    if r < len(target) and c < len(target[0]):
        if target[r][c] == k: 
            return time
    while True:
        if len(target) >= len(target[0]):
            Op_R(target)
        else:
            Op_C(target)
        time += 1
        if time > 100: 
            return -1
        if r < len(target) and c < len(target[0]):
            if target[r][c] == k: 
                return time


r, c, k = map(int, input().split())
graph   = [list(map(int, input().split())) for _ in range(3)]

print(solution(r-1, c-1, k, graph))