import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def reset():
    global mem, mark
    mem = []
    mark = [False]*10
    return

def decision(n1, n2, s):
    result = False
    if s == '<':
        if n1 < n2:
            result = True
    if s == '>':
        if n1 > n2:
            result = True
    return result

def dfs(depth, start, end, step):
    global k, sign, mem, ans, mark, flag_min, flag_max

    if depth == k+1:
        flag = True
        for i in range(k):
            if not decision(mem[i], mem[i+1], sign[i]):
                flag = False
                break
        if flag:
            ans.append(''.join(str(_) for _ in mem))
            if start < end:
                flag_min = True
            else:
                flag_max = True
        return

    for i in range(start, end, step):
        if not mark[i]:
            mark[i] = True
            mem.append(i)
            dfs(depth+1, start, end, step)
            mark[i] = False
            mem.pop()

            if (start < end and flag_min) or (start > end and flag_max):
                break


if __name__ == "__main__":
    k    = int(input())
    sign = list(map(str, input().split()))

    mem  = []
    ans  = []
    mark = [False]*10

    flag_min = False
    flag_max = False

    dfs(0, 0, 10, 1)
    reset()
    dfs(0, 9, -1, -1)
    print(ans[-1], '\n', ans[0], sep='')