"""
- 입력:
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.
테스트 케이스의 개수는 100,000개를 넘지 않는다.
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
입력의 마지막 줄에는 0이 하나 주어진다.

- 출력:
각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.
이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

- 풀이:
0. 에라토스테네스의 체 방법으로 소수 구하기: 소수의 배수는 소수가 아니니, 소수의 배수가 되는 모든 합성수를 지우는 방법
1. 테스트 케이스가 많을 수 있으니, 시간을 고려해 소수 리스트를 만든다.
2.
"""

import sys

input = sys.stdin.readline

MAX = 1000000
prime = [True] * (MAX+1)

# 소수 리스트 구하기
for i in range(2, int(MAX**0.5+1)):
    if prime[i]:
        for j in range(i*2, MAX+1, i):
            prime[j] = False    # 소수의 배수는 합성수, 배제

# n = a + b 구하기
while True:
    n = int(input())
    if n == 0:  # 입력 종료 조건
        break

    for a in range(3, len(prime)): # 홀수 소수는 3부터
        b = n - a
        if b < a:   # 추측 검증 오류
            print("Goldbach's conjecture is wrong.")
        if prime[a] and prime[b]: # 둘 다 소수라면 True & True
            print(n, "=", a, "+", b)
            break
