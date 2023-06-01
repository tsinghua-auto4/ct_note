
def solution(bag_size: int, item_len: int, items: list[list]):
    # dp 배열 선언
    dp = [[0 for _ in range(bag_size+1)] for _ in range(item_len+1)]

    for a in range(1, item_len+1):
        for b in range(1, bag_size+1):
            w, v = items[a]

            if b < w: # 가방 무게가 지금 조회한 것 보다 작다면, 바로 [이전물건][같은무게]를 입력
                dp[a][b] = dp[a-1][b]
            else: # 그렇지 않다면, 가장 가치 있는 것으로 채우자
                dp[a][b] = max(dp[a-1][b], v + dp[a-1][b-w])
    
    return dp[item_len][bag_size]


N, K  = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, input().split())))

print(solution(K, N, items))