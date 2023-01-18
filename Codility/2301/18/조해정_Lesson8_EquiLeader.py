"""
시퀀스를 왼쪽 오른쪽으로 나눠서 각각의 값의 개수를 기록한다.
이 때 왼쪽 시퀀스의 리더 후보를 왼쪽 시퀀스의 리더가 맞는지 확인하고,
그냥 동일한 리더를 가지고 있는지 확인만 하면 되기에,
오른쪽 시퀀스의 해당 값 개수가 과반수인지 확인을 한다.
과반수가 맞다면 +1, 아니면 패스
값의 개수를 바로 찾기 위해, dictionary 로 자료 생성

Detected time complexity:
O(N)
"""


def solution(a):
    n = len(a)
    if n == 1:
        return 0
    elif n == 2:
        if a[0] == a[1]:
            return 1
        else:
            return 0

    ans = 0

    left, right = {}, {}
    left_leader, right_leader = a[0], a[0]

    for i in range(n):
        if a[i] not in right:
            right[a[i]] = 1
        else:
            right[a[i]] += 1
        if right_leader != a[i] and right[a[i]] > right[right_leader]:
            right_leader = a[i]

    # 좌 시퀀스 사이즈 s, 우 시퀀스 사이즈 n-s
    for s in range(1, n):   # 좌우 갈라놓을 위치, n-1까지
        val = a[s-1]

        if val not in left:
            left[val] = 1
        else:
            left[val] += 1
        if left_leader != val and left[val] > left[left_leader]:
            left_leader = val

        right[val] -= 1

        # 먼저 왼쪽 시퀀스의 리더가 맞는지 확인
        leader = left_leader
        if left[leader] > s//2:
            # 그 다음 해당 값이 오른쪽 시퀀스의 리더가 맞는지 확인
            if right[leader] > (n-s)//2:
                ans += 1
    return ans
