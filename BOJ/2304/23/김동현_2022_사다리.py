
def binary(x:float, y:float, d:float):
    h1 = pow((pow(x, 2) - pow(d, 2)), 0.5)
    h2 = pow((pow(y, 2) - pow(d, 2)), 0.5)
    c  = h1*h2/(h1+h2)
    return c


x, y, c    = map(float, input().split())
start, end = 0, min(x, y)

ans = 0
while end-start > 0.000001:
    mid = (start+end)/2
    if binary(x, y, mid) >= c:
        ans   = mid
        start = mid
    else:
        end = mid

print("%.3f" % ans)