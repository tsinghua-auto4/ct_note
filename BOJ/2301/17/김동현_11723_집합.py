import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(n, s):
    for _ in range(n):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'add':
            s[int(cmd[1])-1] = 1
        elif cmd[0] == 'remove':
            s[int(cmd[1])-1] = 0
        elif cmd[0] == 'check':
            if s[int(cmd[1])-1] == 1:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            if s[int(cmd[1])-1] == 1:
                s[int(cmd[1])-1] = 0
            else:
                s[int(cmd[1])-1] = 1
        elif cmd[0] == 'all':
            s = [1] * 20
        elif cmd[0] == 'empty':
            s = [0] * 20

if __name__ == "__main__":
    s = [0] * 20
    n = int(input())

    solution(n, s)