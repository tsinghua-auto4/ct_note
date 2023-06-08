

def solution(n: int, x: int):
    global d, p
    if n == 0: # edge case 처리
        if x == 0:
            return 0
        else:
            return 1
    else:
        if x == 1: # 맨 밑층은 패티가 없음
            return 0
        
        elif 1 < x <= 1+d[n-1]: # 아래 레벨의 햄버거라면 재귀로 풀자
            return solution(n-1, x-1)
        
        elif x == d[n-1] + 2: # 먹는 버거가 아래 레벨 햄버거보다 2가 많다면, 빵+버거+패티 조합이다
            return p[n-1]+1
        
        elif d[n-1]+2 < x <= 2*d[n-1]+2: # 전체레벨보다 1개 적은 경우라면, 위의 경우에서 위에 못먹은 버거도 더해주자
            return p[n-1] + 1 + solution(n-1, x-1-d[n-1]-1)
        
        else: # 전체라면 다먹음
            return 2*p[n-1]+1


N, X = map(int, input().split()) # 레벨, 레벨 N 버거의 레이어 수

d, p       = [0]*N, [0]*N # 레벨 n 의 햄버거 길이, 패티 개수
d[0], p[0] = 1, 1

for i in range(1, N):
    d[i] = 2*d[i-1]+3
    p[i] = 2*p[i-1]+1

print(solution(N, X))