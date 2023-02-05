import sys
input = sys.stdin.readline

# 입력
x, y, w, h = map(int, input().split())

# x, y, w-x, h-y중 최솟값을 구한다
ans = min(x, y, w-x, h-y)

# 출력
print(ans)
