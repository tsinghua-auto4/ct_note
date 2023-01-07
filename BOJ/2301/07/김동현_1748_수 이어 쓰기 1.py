import sys

input = sys.stdin.readline


def solution():
    # 1~9(9개), 10~99(90개), 100~999(900개) ~~~ 자리수가 올라가면 10의 배수로 증가 
    unit   = [9, 1] # [갯수, 자리수]
    target = int(input())
    answer = 0

    while target > 0:
        # 이번에 계산할 수의 갯수
        temp = unit[0]
        target -= unit[0]

        # 갯수보다 모자라다면 빼주기
        if target < 0:
            temp += target

        # 출력할 정답에 이번 숫자길이 더해주기
        answer += temp*unit[1]

        # 단위 갱신
        unit[0] *= 10
        unit[1] += 1

    print(answer)


solution()