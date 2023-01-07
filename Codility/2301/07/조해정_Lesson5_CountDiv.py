"""
풀이:
1 ~ a-1 사이인 자연수 중 K의 배수가 몇 개 있는지 = da
1 ~ b 사이인 자연수 중 K의 배수가 몇 개 있는지 = db
그 차이가 a ~ b 사이의 K의 배수의 총 개수
만약 a가 0이라면, 0은 어떤 자연수로도 나눠 떨어지기 때문에 1 추가

Detected time complexity:
O(1)
"""


def solution(a, b, k):
    da = 0
    db = b // k

    if a == 0:
        db += 1
    else:
        da = (a - 1) // k

    return db - da
