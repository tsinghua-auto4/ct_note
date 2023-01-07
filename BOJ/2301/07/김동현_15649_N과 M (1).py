import sys
import itertools

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = [i for i in range(1, n+1)]

    # itertools로 모든 경우의 수 다 뽑고
    ans = list(itertools.permutations(data, m))
    # 출력할 때만 형식을 가다듬자
    for cur in ans:
        tmp = list(cur)
        print(*tmp)

solution()