
def factorial(N):
    global p
    n = 1
    for i in range(2, N+1):
        n = (n*i)%p
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return tmp**2 * n % p
    else:
        return tmp**2 % p


N, K = map(int, input().split())
p    = 1000000007

# 페르마의 소정리와 조합공식을 보면 알 수 있음, 약간의 수학이 필요함
top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

print(top * square(bot, p-2) % p)