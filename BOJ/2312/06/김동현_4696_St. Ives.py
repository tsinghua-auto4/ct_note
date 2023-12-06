while True:
    cur = float(input())
    if cur == 0.:
        break

    ans = 1 + cur + cur**2 + cur**3 + cur**4
    print("%.2f" %(ans))