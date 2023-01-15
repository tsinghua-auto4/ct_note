import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(depth, cur):
    global answer, half_n

    if depth == half_n:
        mem_s = [i for i in range(n) if i not in mem_m]
        tmp1  = 0
        tmp2  = 0

        for i in range(half_n):
            for j in range(half_n):
                tmp1 += data[mem_m[i]][mem_m[j]]
                tmp2 += data[mem_s[i]][mem_s[j]]
        answer = min(answer, abs(tmp1-tmp2))

        return

    for i in range(cur, n):
        mem_m.append(i)
        dfs(depth+1, i+1)
        mem_m.pop()



if __name__ == "__main__":
    n      = int(input())
    data   = [list(map(int, input().split())) for _ in range(n)]
    
    half_n = int(n/2)
    answer = sys.maxsize
    mem_m  = []
    
    dfs(0,0)
    print(answer)