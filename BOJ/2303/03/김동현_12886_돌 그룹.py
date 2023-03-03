import sys
from collections import deque

def solution():
    queue = deque([(A,B)])
    visited[A][B] = True
    while queue:
        a, b = queue.popleft()
        c = TOTAL - (a+b)
        if a == b == c:
            return 1

        for X, Y in [(a,b), (a,c), (b,c)]:
            if X == Y:
                continue
            if X > Y:
                X, Y = Y, X

            X, Y = X+X, Y-X        
            min_ = min(X, Y, TOTAL - (X+Y))
            max_ = max(X, Y, TOTAL - (X+Y))
            if visited[min_][max_]:
                continue
            queue.append((min_, max_))
            visited[min_][max_] = True
    return 0


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())

    TOTAL = A+B+C
    if TOTAL%3 != 0:
        print(0)
        exit()

    visited = [[False]*TOTAL for _ in range(TOTAL)]
    print(solution())