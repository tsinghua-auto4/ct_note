for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())

    h = h2 - h1
    m = m2 - m1
    s = s2 - s1

    if s < 0:
        m -= 1
        s += 60

    if m < 0:
        h -= 1
        m += 60

    print(h, m, s)