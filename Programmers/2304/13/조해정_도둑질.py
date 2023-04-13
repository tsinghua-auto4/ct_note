def solution(money):
    f = [money[0]] * 2
    b = [0, money[1]]

    for i, v in enumerate(money):
        if i < 2:
            continue
        f.append(max(money[i] + f[i - 2], f[i - 1]))
        b.append(max(money[i] + b[i - 2], b[i - 1]))

    return max(f[-2], b[-1])