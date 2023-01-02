"""
- 입력:
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)가 주어진다.
둘째 줄부터 테스트 케이스가 한 줄에 하나씩 주어지며 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.


- 출력:
각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.


- 풀이:
0. MAX = 최대 N = 1,000,000
1. gx = [0, g(1), ... , g(MAX)], fx = [f(1), ..., f(MAX)]
2. g(N) = g(N-1) + f(N)
3. f(N) = 1*N + 2*(N//2) + ... + N*1

"""

import sys

input = sys.stdin.readline

MAX = 1000000
gx = [0] * (MAX+1)  # idx = [0, 1, ..., MAX]
fx = [1] * (MAX+1)  # idx = [0, 1, ..., MAX]

# fx 구하기
for i in range(2, MAX+1):
    j = i
    while j <= MAX:
        fx[j] += i
        j += i

# gx 구하기
for i in range(1, MAX+1):
    gx[i] = gx[i-1] + fx[i]

t = int(input())
for _ in range(t):
    n = int(input())
    print(gx[n])
