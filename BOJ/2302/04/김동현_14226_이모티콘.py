import sys
from collections import deque

def solution(s, visited):
    queue = deque()
    queue.append((1, 0))

    while queue:
        n, c = queue.popleft()
        
        if n == s:
            return visited[(n, c)]
        
        if (n,n) not in visited.keys():
            visited[(n,n)] = visited[(n,c)] + 1
            queue.append((n,n))
        if (n-1,c) not in visited.keys():
            visited[(n-1,c)] = visited[(n,c)] + 1
            queue.append((n-1, c))
        if (n+c,c) not in visited.keys():
            visited[(n+c,c)] = visited[(n,c)] + 1
            queue.append((n+c, c))


if __name__ == "__main__":
    s               = int(sys.stdin.readline())
    visited         = dict()
    visited[(1, 0)] = 0

    print(solution(s, visited))
