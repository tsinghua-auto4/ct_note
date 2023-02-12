import sys
input = sys.stdin.readline

# 입력
input()
a = set(map(int, (input().split())))
b = set(map(int, (input().split())))

# 대칭 차집합
union = a | b
intersection = a & b
complement = a - b
sym_diff = a ^ b

# 출력
print(len(sym_diff))
