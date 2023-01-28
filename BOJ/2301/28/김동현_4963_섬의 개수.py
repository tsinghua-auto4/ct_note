import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def if_inrange(x, y):
    global w, h
    if 0 <= x and x < h:
        if 0 <= y and y < w:
            return True
    return False

def solution(x, y):
    global cnt, move

    if graph[x][y] == 0:
        return False
    
    else:
        cnt += 1
        graph[x][y] = 0

        for next in move:
            nx, ny = x + next[0], y + next[1]
            if if_inrange(nx, ny):
                solution(nx, ny)
        return True


if __name__ == "__main__":
    w, h, cnt = 0, 0, 0
    graph     = []
    move      = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    while True:
        w, h = map(int, input().split())
        if w == 0:
            break
        graph  = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        num = 0

        for i in range(h):
            for j in range(w):
                if solution(i, j):
                    num += 1
        print(num)