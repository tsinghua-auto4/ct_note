import sys
sys.setrecursionlimit(10**6)

def find(depth):
    for i in range(depth):
        if row[depth] == row[i] or abs(depth - i) == abs(row[depth] - row[i]):
            return False
    return True

def solution(depth): #dfs
    global ans

    if depth == n:
        ans += 1
    else:
        for i in range(n):
            row[depth] = i
            if find(depth):
                solution(depth+1)


n   = int(sys.stdin.readline().rstrip())
row = [0]*n
ans = 0

solution(0)

print(ans)