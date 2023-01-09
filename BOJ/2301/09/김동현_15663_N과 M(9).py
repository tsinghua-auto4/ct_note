import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs():
    # 탈출조건은 다 찾은 경우
    if len(ans) == m:
        print(*ans)
        return
    memory = 0
    # loop 돌면서 숫자 하나씩 추가
    for i in range(n):
        if not mark[i] and memory != data[i]:
            mark[i] = True
            ans.append(data[i])
            memory = data[i]
            dfs()
            mark[i] = False
            ans.pop()



if __name__ == "__main__":
    n, m = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    mark = [False] * n
    
    ans  = []

    dfs()