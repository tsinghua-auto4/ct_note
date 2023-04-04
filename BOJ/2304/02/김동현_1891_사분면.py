import sys
sys.setrecursionlimit(10**8)

# 숫자로 좌표 찾기
def pos(n1, m1, n2, m2, idx):
    if idx == len(num):
        return n1, m1
    
    # 1분면이면, 행은 작은 수, 열은 큰 수 (다른 분면도 같은 원리)
    # -> 이해가 안간다면 2차원 배열의 좌표를 상상해보자, 1분면의 위치는 (0, 1)
    # 타겟 변수: 행 변수 n1 유지, 열 변수 m1 확장
    # 범위 변수: 행 변수 n2 축소, 열 변수 m1 유지
    if num[idx] == '1': 
        return pos(n1, (m1+m2)//2, (n1+n2)//2, m2, idx+1)
    elif num[idx] == '2':
        return pos(n1, m1, (n1+n2)//2, (m1+m2)//2, idx+1)
    elif num[idx] == '3':
        return pos((n1+n2)//2, m1, n2, (m1+m2)//2, idx+1)
    elif num[idx] == '4':
        return pos((n1+n2)//2, (m1+m2)//2, n2, m2, idx+1)

# 좌표로 숫자 찾기
def solution(n1, m1, n2, m2):
    global ans
    if len(ans) == int(d):
        return ans

    # 행이 작은 수이고 열이 큰 수라면 (0, 1), 즉 1분면, 다른 분면의 연산도 같은 의미
    if n1 <= nx < (n1+n2)//2 and (m1+m2)//2 <= ny < m2:
        ans += '1'
        return solution(n1, (m1+m2)//2, (n1+n2)//2, m2)
    elif n1 <= nx < (n1+n2)//2 and m1 <= ny < (m1+m2)//2:
        ans += '2'
        return solution(n1, m1, (n1+n2)//2, (m1+m2)//2)
    elif (n1+n2)//2 <= nx < n2 and m1 <= ny < (m1+m2)//2:
        ans += '3'
        return solution((n1+n2)//2, m1, n2, (m1+m2)//2)
    elif (n1+n2)//2 <= nx < n2 and (m1+m2)//2 <= ny < m2:
        ans += '4'
        return solution((n1+n2)//2, (m1+m2)//2, n2, m2)



d, num = map(str, sys.stdin.readline().split())

# 2, 1이면 2열 우측으로(+), 1행 위로 올라감(-)
# -> dx를 사용할 때 +-를 바꿔야함
dy, dx = map(int, sys.stdin.readline().split())

n, m   = 2**int(d), 2**int(d) # 조각의 총 길이는 2**d, 3번 나누면 2**3 == 8개의 칸

x, y   = pos(0, 0, n, m, 0) # num의 사분면 조각 좌표
nx, ny = x - dx, y + dy # 새로운 사분면 조각의 좌표

ans = ''
if 0 <= nx < n and 0 <= ny < m:
    print(int(solution(0, 0, n, m)))
else:
    print(-1)