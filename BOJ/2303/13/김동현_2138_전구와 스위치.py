# well-known greedy 문제라는데, 난 처음에 몰라서 이해가 안갔음.
import sys

def change(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        if L[i-1] == B[i-1]:
            continue
        press += 1
        for j in range(i-1, i+2):
            if j < n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9


n    = int(sys.stdin.readline())
asis = list(map(int, sys.stdin.readline().rstrip()))
tobe = list(map(int, sys.stdin.readline().rstrip()))

# 첫 번째 switch on/off 를 나눠서 돌리는 이유는, 첫 번째 스위치는 그 전의 순서의 전구와 비교할 수 없기 때문
# 위에 change 함수를 보면 항상 지금 on/off하는 switch 의 전 순서의 전구와 비교하고 있음
res = change(asis, tobe) # case1: 첫 번째 switch off
asis[0] = 1 - asis[0]    # case2: 두 번째 switch off
asis[1] = 1 - asis[1]
res = min(res, change(asis, tobe) + 1) # 최적의 해
print(res if res != 1e9 else -1)