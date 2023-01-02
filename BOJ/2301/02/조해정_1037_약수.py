import sys
input = sys.stdin.readline

n = int(input())    # 진짜 약수의 개수

divs = list(map(int, input().split()))    # 진짜 약수 리스트
divs.sort()     # 가장 크고 작은 약수 찾기 위한 정렬

print(divs[0] * divs[-1])    # 가장 큰 약수 * 가장 작은 약수 = Num
