import sys
import itertools

_input = sys.stdin.readline

while True:
    case = _input()
    if case == "0":     # 테스트 종료
        break

    case = case.split()
    k = int(case[0])
    s = list(map(int, case[1:]))

    for i in itertools.combinations(s, 6):      # 6개 조합 찾아서 반환
        print(*i)       # 배열을 풀어서 출력

    print()             # 케이스 사이에 빈 줄
