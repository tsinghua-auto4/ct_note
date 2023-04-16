# 참고 블로그: https://codable.tistory.com/4

def distance(a, b):
    return pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)

# 각 분할의 mid 포인트에서 가장 가까운 점들을 모아서 서로의 거리를 계산 -> 모아서 제일 작은 것 계산
def solution(start, end):
    global points

    # 같은 점이면 거리가 없지
    if start == end:
        return float('inf')
    
    # 바로 옆 점이면 계산 ㄱㄱ
    if end - start == 1:
        return distance(points[start], points[end])
    
    # 범위가 아직 안좁혀졌을 때, 분할로 들어가서 mid 기준으로 제일 가까운 점의 거리를 계산해보자
    mid         = (start+end)//2
    minDistance = min(solution(start, mid), solution(mid, end))

    # 위에서 계산한 points[mid]~(minDistance)를 기준으로, x축 좌우로 minDistance만큼 탐색
    candidates = []
    for i in range(start, end+1):
        if pow(points[mid][0]-points[i][0], 2) < minDistance:
            candidates.append(points[i])
    # y축을 기준으로 정렬
    candidates.sort(key= lambda x: x[1])

    # 추린 후보 포인트 내에서 최소 거리도 계산해주자
    t = len(candidates)
    # 위에서 이미 y축 기준으로 정렬을 했으니, 버블순서로(순차적) 거리를 계산함
    for i in range(t-1):
        for j in range(i+1, t):
            if pow(candidates[i][1] - candidates[j][1], 2) < minDistance:
                minDistance = min(minDistance, distance(candidates[i], candidates[j]))
            else:
                break

    return minDistance


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()

print(solution(0, N-1))