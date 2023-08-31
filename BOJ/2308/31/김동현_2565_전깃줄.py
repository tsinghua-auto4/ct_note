import heapq

N     = int(input())
dp    = [1]*N
lines = []
datas = []

# 정렬로 하자, sort쓰면 bigO가 커서 그냥 pq로 때려버림
for _ in range(N):
    cur = list(map(int, input().split()))
    heapq.heappush(datas, cur)
for _ in range(N):
    lines.append(heapq.heappop(datas))

# dp 로직, A 정렬한 데이터의 B가 계속 커져야 교차안함, 그래서 앞순서의 B가 뒷순서의 B보다 작은 경우만 카운팅을 늘린다
for i in range(1, N):
    for j in range(i):
        # 앞순서의 B가 더 작을때, 로직 수행
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

# N에서 제일 긴 DP값을 뻬면 잘라야 하는 전깃줄 수
print(N-max(dp))