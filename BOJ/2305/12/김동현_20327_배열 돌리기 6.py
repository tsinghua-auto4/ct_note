

def command_1(graph: list, l: int):
    global N, R
    for cr in range(0, 2**N, 2**l):
        for dr in range(0, 2**l//2):
            tr_1 = cr+dr
            tr_2 = cr+2**l-1-dr
            graph[tr_1], graph[tr_2] = graph[tr_2], graph[tr_1]

def command_2(graph: list, l: int):
    global N, R
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            for tr in range(cr, cr+2**l):
                for dc in range(0, 2**l//2):
                    tc_1 = cc + dc
                    tc_2 = cc + 2**l - 1 - dc
                    graph[tr][tc_1], graph[tr][tc_2] = graph[tr][tc_2], graph[tr][tc_1]

def command_3(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            target = []
            for row in graph[cr:cr+2**l]:
                target.append(row[cc:cc+2**l])
            new_target = [[0]*2**l for _ in range(2**l)]
            for i in range(2**l):
                for j in range(2**l):
                    new_target[i][j] = target[2**l-1-j][i]

            for tr in range(cr, cr+2**l):
                for tc in range(cc, cc+2**l):
                    new_graph[tr][tc] = new_target[tr-cr][tc-cc]
    return new_graph

def command_4(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            target = []
            for row in graph[cr:cr+2**l]:
                target.append(row[cc:cc+2**l])
            new_target = [[0]*2**l for _ in range(2**l)]
            for i in range(2**l):
                for j in range(2**l):
                    new_target[i][j] = target[j][2**l-1-i]

            for tr in range(cr, cr+2**l):
                for tc in range(cc, cc+2**l):
                    new_graph[tr][tc] = new_target[tr-cr][tc-cc]
    return new_graph

def command_5(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        new_graph[2**N-(cr//2**l+1)*2**l: 2**N-(cr//2**l+1)*2**l + 2**l] = graph[cr:cr+2**l]
    return new_graph

def command_6(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            for dr in range(2**l):
                new_graph[cr+dr][2**N-(cc//2**l+1)*2**l: 2**N-(cc//2**l+1)*2**l + 2**l] = graph[cr+dr][cc:cc+2**l]
    return new_graph

def command_7(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            target = []
            for row in graph[cr:cr+2**l]:
                target.append(row[cc:cc+2**l])
            new_target = [[0]*2**l for _ in range(2**l)]
            for i in range(2**l):
                for j in range(2**l):
                    new_target[i][j] = target[j][2**l-1-i]

            for tr in range(cr, cr+2**l):
                for tc in range(cc, cc+2**l):
                    new_graph[tc][2**N-1-tr] = new_target[tr-cr][tc-cc]
    return new_graph

def command_8(graph: list, l: int):
    global N, R
    new_graph = [[0]*2**N for _ in range(2**N)]
    for cr in range(0, 2**N, 2**l):
        for cc in range(0, 2**N, 2**l):
            target = []
            for row in graph[cr:cr+2**l]:
                target.append(row[cc:cc+2**l])
            new_target = [[0]*2**l for _ in range(2**l)]
            for i in range(2**l):
                for j in range(2**l):
                    new_target[i][j] = target[2**l-1-j][i]

            for tr in range(cr, cr+2**l):
                for tc in range(cc, cc+2**l):
                    new_graph[2**N-1-tc][tr] = new_target[tr-cr][tc-cc]
    return new_graph


def solution(k: int, l: int):
    global N, R, graph

    if k == 1:
        command_1(graph, l)
    elif k == 2:
        command_2(graph, l)
    elif k == 3:
        graph = command_3(graph, l)
    elif k == 4:
        graph = command_4(graph, l)
    elif k == 5:
        graph = command_5(graph, l)
    elif k == 6:
        graph = command_6(graph, l)
    elif k == 7:
        graph = command_7(graph, l)
    elif k == 8:
        graph = command_8(graph, l)



N, R  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**N)]

command = [list(map(int, input().split())) for _ in range(R)]

for k, l in command:
    solution(k, l)

for row in graph:
    print(*row)