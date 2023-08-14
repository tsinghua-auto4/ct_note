a, b = map(int, input().split())
A = (a+b)//2
B = int(a-A)

if A >= 0 and B >= 0:
    if A > B:
        print(A, B)
    else:
        print(B, A)
if A<0 or B<0 or (a+b)%2:
    print(-1)