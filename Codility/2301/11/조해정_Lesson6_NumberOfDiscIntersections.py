"""
이 문제는 좀 어려웠다...
각 원마다 왼쪽 좌표, 오른쪽 좌표를 기록한다.
제일 작은 오른쪽 좌표부터 본인을 포함해 왼쪽에 왼쪽 좌표가 총 몇 개 있는 지 센다.
-> 왼쪽 좌표가 오른쪽 좌표 오른쪽에 있으면 겹치지 않지만, 그 외에는 겹친다는 소리이기 때문.
본인은 제외시켜야 하기에 -1을 해준다.
다음 오른쪽 좌표는 그 전의 중복된 값을 제외해야 해서 하나 더 감소시킨다. (누적)

Detected time complexity:
O(N*log(N)) or O(N)
"""


def solution(arr):
    n = len(arr)
    if n <= 1:
        return 0

    coord = []
    for i, r in enumerate(arr):
        coord.append((i-r, -1))     # 왼쪽 좌표
        coord.append((i+r, 1))      # 오른쪽 좌표

    coord.sort(key=lambda x: (x[0], x[1]))

    cnt = 0     # 여태 센 원의 누적 수
    ans = 0
    left = 0    # 기준점 오른쪽 좌표의 왼쪽 또는 겹치는 왼쪽 좌표 수

    for val in coord:
        if val[1] == -1:
            left += 1
        else:
            cnt += 1
            ans += (left - cnt)
            if ans > 10000000:
                ans = -1
                break
    return ans
