"""
Detected time complexity:
O(N*log(N)) or O(N)
"""


def solution(a):
    cnt = 0
    dic = {}
    ans = -1

    for i, n in enumerate(a):
        if n not in dic:
            dic[n] = 0
        dic[n] += 1
        if cnt < dic[n]:    # 배열의 최대 횟수 등장 요소가 리더 후보
            cnt = dic[n]
            ans = i

    if cnt <= len(a) // 2:  # n/2 보다 적게 있으면 리더 아님
        ans = -1

    return ans
