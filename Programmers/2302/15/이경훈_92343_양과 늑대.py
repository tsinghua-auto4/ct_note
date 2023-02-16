import copy
# 양의 최대 마릿수
cnt = 0

def solution(info, edges):    
    global cnt
    graph = [[] for _ in range(len(info))]
    # 인접리스트 만듦
    for edge in edges:
        parent, sub = edge
        graph[parent].append(sub)
        
    # 현재노드, 양의 마릿수, 늑대 마릿수, 탐색 가능한 후보군
    def dfs(x, sheep, wolf, capa):
        global cnt
        
        # 만약 현재 노드가 양이라면 양의 마릿수 +1
        if info[x] == 0:
            sheep += 1
        # 만약 현재 노드가 늑대라면 늑대의 마릿수 +1
        else:
            wolf += 1
        
        # 늑대가 양보다 많거나 같다면 종료
        if sheep <= wolf:
            return
        
        # 양 마릿수 최대일때 cnt 갱신
        if sheep > cnt:
            cnt = sheep
        
        # dfs로 다음 탐색 가능한 후보군들을 돌려야하는데 후보군을 그대로 보내면 
        # 얕은 복사로 가기 때문에 현재의 세트가 바뀔 수 있다.
        # 고로 깊은 복사로 보내야 함
        capa = copy.deepcopy(capa)
        
        # 인접리스트에서 연결되어 있는 후보군, 즉 현재 노드의 자식 노드들 전부 추가
        capa.update(graph[x])
        
        # 후보군중에서 하나씩 골라서 dfs 보내되
        # 그 후보군을 빼서 현재 노드로 넣고
        # 재귀를 마치고 오면 다시 후보군을 넣어야 함
        for node in capa:
            capa.remove(node)
            dfs(node, sheep, wolf, capa)
            capa.add(node)
        return
    
    dfs(0, 0, 0, set())
    
    return cnt
