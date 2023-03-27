import sys

n, m, k = map(int, sys.stdin.readline().split()) # num, LIS, LDS

if n < m+k-1 or n > m*k:
    print(-1)
else:
    l = list(range(k, 0, -1)) # 먼저 감소하는 수열을 넣자
    n -= k # 총 수량에서 넣은 감소 수열을 빼면, 미래에 넣을 숫자의 개수만 남음
    m -= 1 # 앞으로 만들 행의 갯수가 최신화
    while m:
        l.extend(range(k+n//m, k, -1)) # [k+1, k+n//m]을 역순으로 l 뒤에 넣음, n//m 다음에 만들 행의 크기
        k += n//m # k 값 최신화
        n -= n//m # n 값 최신화
        m -= 1    # m 값 최신화
    print(*l)