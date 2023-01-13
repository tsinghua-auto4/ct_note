import sys
from itertools import combinations


def check(target):
    n = len(target)
    ans = 1

    for i in range(n):

        # col
        cnt = 1
        for j in range(1, n):
            if target[j][i] == target[j-1][i]:
                cnt += 1
            else: 
                cnt = 1

            if cnt > ans:
                ans = cnt

        # row
        cnt = 1
        for j in range(1, n):
            if target[i][j] == target[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt

    return ans

def solution():

    n = int(sys.stdin.readline())
    candy = [list(sys.stdin.readline().strip()) for _ in range(n)]

    ans = 1
    for i in range(n-1):
        for j in range(1, n):
            candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
            tmp = check(candy)
            if ans < tmp:
                ans = tmp
            if ans == n:
                print(ans)
                exit()
            candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]

            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            tmp = check(candy)
            if ans < tmp:
                ans = tmp
            if ans == n:
                print(ans)
                exit()
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

    print(ans)

solution()