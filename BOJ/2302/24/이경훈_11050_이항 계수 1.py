import sys
input = sys.stdin.readline

def fac(x):
    sum = 1
    for i in range(1, x+1):
        sum *= i
    return sum

def C(n, k):
    return int(fac(n)/(fac(k) * fac(n-k)))

N, K = map(int, input().split())
print(C(N,K))
