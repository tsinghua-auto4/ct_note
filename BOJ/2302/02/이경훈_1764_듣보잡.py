import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
not_heard = {input().rstrip() for _ in range(n)}
not_seen = {input().rstrip() for _ in range(m)}
cnt = 0
ans = []

# 듣잡의 요소가 듣보 중에 있다면 cnt를 하나 증가시키고 ans에 그 요소를 추가함
for h in not_heard:
  if h in not_seen:
    cnt += 1
    ans.append(h)

# 사전순서대로 정렬
ans.sort()

print(cnt)
for i in range(len(ans)):
  print(ans[i])