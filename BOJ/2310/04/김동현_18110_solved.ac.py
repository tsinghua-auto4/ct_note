n = int(input())

if n != 0:
    data = [int(input()) for _ in range(n)]
    data.sort()

    ran = round(float(n)*0.15+0.0000001)
    ans = round(sum(data[ran:n-ran])/(len(data[ran:n-ran])) +0.0000001)
    print(ans)
else:
    print(0)