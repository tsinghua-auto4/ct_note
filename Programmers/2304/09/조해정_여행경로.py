def solution(tickets):
    routes = {}
    for a, b in tickets:
        routes[a] = routes.get(a, []) + [b]

    for a in routes.keys():
        routes[a].sort(reverse=True)

    answer = ["ICN"]
    path = []

    while answer:
        cur = answer[-1]
        if cur not in routes or not routes[cur]:
            path.append(answer.pop())
        else:
            answer.append(routes[cur].pop())

    return path[::-1]