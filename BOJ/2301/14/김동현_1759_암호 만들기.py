import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(depth, cur, num_vow, num_con):
    if depth == L and num_vow >= 1 and num_con >= 2:
        print(''.join(ans))

    for i in range(cur, C):
        if not mark[i]:
            mark[i] = True
            ans.append(data[i])

            if data[i] in Vowels:
                dfs(depth+1, i+1, num_vow+1, num_con)
            else:
                dfs(depth+1, i+1, num_vow, num_con+1)
            
            ans.pop()
            mark[i] = False


if __name__ == "__main__":
    L, C    = map(int, input().split())
    data    = list(map(str, input().split()))
    data.sort()

    Vowels  = ['a', 'e', 'i', 'o', 'u']
    mark    = [False] * C
    ans     = []

    dfs(0, 0, 0, 0)