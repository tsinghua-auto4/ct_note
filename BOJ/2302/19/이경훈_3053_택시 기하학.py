import sys
import math
input = sys.stdin.readline

# 입력
n = int(input())

# 출력
ans1 = n**2*math.pi
ans2 = (2*n)**2/2

print(round(ans1, 6))
print(round(ans2, 6))