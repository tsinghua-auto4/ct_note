def solution(citations):
    answer = 0

    n = len(citations)
    nn = n
    citations.sort(reverse=True)
    if n < citations[-1]:
        return n

    cnt = [0 for i in range(1001)]
    for c in citations:
        if c > 1000:
            cnt[1000] += 1
        else:
            cnt[c] += 1

    cnt_sum = sum(cnt[n + 1:])
    while n >= 0:
        cnt_sum += cnt[n]
        if cnt_sum >= n and nn - cnt_sum <= n:
            answer = n
            break
        n -= 1

    return answer
