def solution(answers):
    answer = []

    n = len(answers)
    a = [1, 2, 3, 4, 5] * (n // 5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (n // 8 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n // 10 + 1)

    cnt_a, cnt_b, cnt_c = 0, 0, 0
    for i, ans in enumerate(answers):
        if a[i] == ans:
            cnt_a += 1
        if b[i] == ans:
            cnt_b += 1
        if c[i] == ans:
            cnt_c += 1

    max_cnt = max(cnt_a, cnt_b, cnt_c)
    if cnt_a == max_cnt:
        answer.append(1)
    if cnt_b == max_cnt:
        answer.append(2)
    if cnt_c == max_cnt:
        answer.append(3)

    return sorted(answer)
