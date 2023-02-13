import sys

def dfs(depth, total, plus, minus, multiply, divide):
    global ans_max, ans_min

    if depth == n:
        ans_max = max(ans_max, total)
        ans_min = min(ans_min, total)
        return

    if plus:
        dfs(depth+1, total+data[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-data[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*data[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/data[depth]), plus, minus, multiply, divide-1)


if __name__ == "__main__":
    n    = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    oper = list(map(int, sys.stdin.readline().split()))

    ans_max = -1e9
    ans_min = 1e9

    dfs(1, data[0], oper[0], oper[1], oper[2], oper[3])
    print(ans_max)
    print(ans_min)