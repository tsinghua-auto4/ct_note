import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution():
    n    = int(input())
    data = list(map(int, input().split()))
    flag = False

    for i in range(n-1, 0, -1):
        if data[i-1] > data[i]:
            for j in range(n-1, 0, -1):
                if data[i-1] > data[j]:
                    data[i-1], data[j] = data[j], data[i-1]
                    data = data[:i] + sorted(data[i:], reverse=True)
                    flag = True
                    break
        if flag:
            print(*data)
            break
    
    if not flag:
        print(-1)



solution()