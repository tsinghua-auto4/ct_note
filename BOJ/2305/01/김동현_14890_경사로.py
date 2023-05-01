
def logic(target: list):
    global N, L
    slope = [False]*N
    
    # 하나씩 돌면서 높이가 맞는지 확인
    for idx in range(1, N):
        # 붙어있는 칸의 높이 차이가 1보다 크다면 보상 불가
        if abs(target[idx-1]-target[idx]) > 1:
            return False
        

        # 현재 칸이 전 칸보다 낮은 경우
        if target[idx-1] > target[idx]:
            # 세모(경사)블록으로 보상해주자
            for comp in range(L):
                # 만약 깔 블록이 범위를 넘어섰거나/이미 블록을 깔았거나/블록의 길이가 낮은 칸의 길이보다 길다면 깔 수 없음
                if not(0 <= idx+comp < N) or slope[idx+comp] or target[idx] != target[idx+comp]:
                    return False
                if target[idx] == target[idx+comp]:
                    slope[idx+comp] = True

        # 현재 칸이 전 칸보다 높은 경우, 반대로 생각해보면 됨
        elif target[idx-1] < target[idx]:
            for comp in range(L):
                if not(0 <= idx-1-comp < N) or slope[idx-1-comp] or target[idx-1] != target[idx-1-comp]:
                    return False
                if target[idx-1] == target[idx-1-comp]:
                    slope[idx-1-comp] = True

    return True

def solution():
    global N, L, graph

    cnt = 0

    # 행 처리
    for cr in range(N):
        # 현재 처리해야할 행
        cur = graph[cr].copy()
        # 판단로직 함수를 넣어보자
        if logic(cur):
            cnt += 1

    # 열 처리
    for cc in range(N):
        # 현재 처리해야할 열
        cur = [graph[cr][cc] for cr in range(N)]
        # 판단로직 함수를 넣어보자
        if logic(cur):
            cnt += 1

    return cnt


N, L  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

print(solution())