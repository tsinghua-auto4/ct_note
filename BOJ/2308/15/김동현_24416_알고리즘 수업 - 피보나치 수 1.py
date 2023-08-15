res = 0
def code1(n):
    global res
    if n == 1 or n == 2:
        res += 1
        return 1
    else:
        return code1(n-1) + code1(n-2)

def code2(n):
    res = 0
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        res += 1
    return res

n = int(input())
code1(n)
print(res, code2(n))