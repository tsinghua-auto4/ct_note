import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        m, n, x, y = map(int, input().split())

        flag = False
        # x는 최대 m*n을 넘지 못하기에 루프 탈출 조건으로 설정
        while x <= m*n:
            # x는 m진법으로 증가, y는 n진법으로 증가
            # 하지만 같은 수가 증가하기 때문에 y를 인자로 보고 n으로 기준을 잡는다
            if x%n == y%n:
                flag = True
                print(x)
                break
            x += m

        # 다 돌았는데도 없는 경우라면 -1로 예외처리
        if not flag:
            print(-1)


solution()