leaves = {0: [1]}
wwires = []
cnt = []


def leaf_graph(v):
    leaves[v] = []
    pop_idx = []

    for i, val in enumerate(wwires):
        if v in val:
            pop_idx.append(i)
            leaves[v].append(sum(val) - v)

    for i, val in enumerate(pop_idx):
        wwires.pop(val - i)

    for i in leaves[v]:
        leaf_graph(i)


def count_node(v):
    if not leaves[v]:
        return 1

    cnt_total = 1
    for leaf in leaves[v]:
        temp = count_node(leaf)
        cnt_total += temp
        cnt[leaf] += temp
    return cnt_total


def solution(n, wires):
    global leaves, wwires, cnt

    visited = [False] * (n + 1)  # index 편하게 보려고
    visited[0] = True

    wwires = wires[:]
    leaf_graph(1)
    # print(leaves)

    cnt = [0] * (n + 1)
    cnt[1] += count_node(1)
    # print(cnt)

    answer = n
    for v1, v2 in wires:
        v = min(cnt[v1], cnt[v2])
        answer = min(answer, abs(2 * v - n))

    return answer
