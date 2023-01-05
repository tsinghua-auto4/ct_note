def solution(N):
    gap = 0     # binary gap
    if N >= 5:  # 5보다 작으면 gap이 나올 수 없다.
        # 이진수로 변환하고, 1사이의 "0"을 추출하기 위해 문자열을 "1"로 split한다.
        lst = bin(N).split("1")
        # 맨 앞은 0을 제외하고 모든 이진수는 1로 시작해서 gap 세는데 필요없다.
        # 맨 뒤는 1로 끝나서 ''인 경우나 0으로 끝나서 '000'이라도 gap에 해당하지 않는다.
        # 그래서 범위가 lst[1:-1]
        for i in lst[1:-1]:
            if i != '':     # ''을 제외하고는 gap인 '0'*n만 리스트에 들어가 있다.
                gap = max(gap, len(i))
    return gap
