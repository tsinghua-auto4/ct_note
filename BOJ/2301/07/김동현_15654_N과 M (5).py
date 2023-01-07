import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution(depth, N, M):
    # 탈출조건은 다 찾은 경우
    if depth == M:
        print(' '.join(map(str, ans)))
        return

    # loop 돌면서 숫자 하나씩 추가
    for i in range(len(data)):
        tmp  = data[i]
        ans.append(tmp)
        data.remove(tmp)
        solution(depth+1, N, M)
        data.insert(i, tmp)
        ans.pop()



if __name__ == "__main__":
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    ans  = []
    solution(0, n ,m)