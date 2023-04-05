answer = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if dungeons[i][0] <= k and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = False  # 돌아오면 다시 False


def solution(k, dungeons):
    global visited
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer
