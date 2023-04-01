import sys

def solution(n, r, c):
    if n == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*solution(n-1, r//2, c//2)


n, r, c = map(int, sys.stdin.readline().split())
print(solution(n, r, c))