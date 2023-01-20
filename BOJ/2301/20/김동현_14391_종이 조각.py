import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():#bitmask
    global n, m, data, ans

    # 모든 경우를 우에서 좌로 2진법 표기, 1->row / 0->col
    for i in range(1 << n*m): #shift 방식으로 나타낸 2 ** n*m, n*m개의 2진 메모리의 모든 경우의 수
        total = 0

        # 모든 메모리를 순회한다, 이번엔 행 계산을 해보자
        for row in range(n):
            rowSum = 0
            for col in range(m):
                # 2차원 배열의 메모리를 1차원으로 길게 늘렸을 때, 현재 조회하고 있는 메모리의 새로운 주소다
                idx = row * m + col
                # 최상위 for 문에서 정의하는 현재 경우에서, 지금 조회하고 있는 메모리가 row 형태인지 확인
                # 1 << idx 는 우리가 조회하고 있는 메모리가 1이고 나머지는 다 0이다, & 연산으로 해당 위치 메모리의 경우만 추출가능
                if i & (1 << idx) != 0:
                    # 맞다면 우리는 좌에서 우로 수를 읽고 있기 때문에 기존 합의 단위를 올려주고(*10) 새로운 1의 자리 수를 더한다
                    rowSum = rowSum * 10 + data[row][col]
                else:
                    # 아니라면 중간 정산을 하자
                    total += rowSum
                    rowSum = 0
            # 1 row가 끝나면 total에 정산을 해주자
            total += rowSum

        # col 도 같은 로직으로 처리하자, 다만 1->row / 0->col으로 정의한 것을 주의하면서 코드를 전개하자
        for col in range(m):
            colSum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    colSum = colSum * 10 + data[row][col]
                else:
                    total += colSum
                    colSum = 0
            total += colSum
        
        ans = max(ans, total)

if __name__ == "__main__":
    n, m = map(int, input().split())
    data = [list(map(int, input().rstrip())) for _ in range(n)]

    ans = 0
    solution()

    print(ans)