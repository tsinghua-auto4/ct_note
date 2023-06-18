def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    camera = -30001
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
    return answer