while True:
    try:
        n = int(input())
        for i in range(n+1):
            if i == 0:
                ans = '-'
            else:
                ans = ans + ' '*len(ans) + ans
        print(ans)
    except EOFError:
        break