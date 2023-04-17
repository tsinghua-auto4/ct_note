import sys

input = sys.stdin.readline

global_arr = []
is_answer = False


def generate_max(k, combi, chosed):
    global global_arr, is_answer

    if is_answer:
        return

    if len(combi) == k:
        # 부등호 확인해보자
        is_answer = True

        for i in range(len(combi) - 1):
            if global_arr[i] == "<":
                if combi[i] > combi[i + 1]:
                    is_answer = False
                    break
            else:
                if combi[i] < combi[i + 1]:
                    is_answer = False
                    break
        if is_answer:
            print("".join(list(map(str, combi))))
            return
        return

    for i in range(9, -1, -1):
        if not chosed[i]:
            combi.append(i)
            chosed[i] = True
            generate_max(k, combi, chosed)
            if is_answer:
                return
            chosed[i] = False
            combi.pop()


def generate_min(k, combi, chosed):
    global global_arr, is_answer

    if is_answer:
        return

    if len(combi) == k:
        # 부등호 확인해보자
        is_answer = True

        for i in range(len(combi) - 1):
            if global_arr[i] == "<":
                if combi[i] > combi[i + 1]:
                    is_answer = False
                    break
            else:
                if combi[i] < combi[i + 1]:
                    is_answer = False
                    break
        if is_answer:
            print("".join(list(map(str, combi))))
            return
        return

    for i in range(10):
        if not chosed[i]:
            combi.append(i)
            chosed[i] = True
            generate_min(k, combi, chosed)
            if is_answer:
                return
            chosed[i] = False
            combi.pop()


def solution(k, arr):
    global global_arr, is_answer
    global_arr = arr

    generate_max(k + 1, [], [False] * 10)
    is_answer = False
    generate_min(k + 1, [], [False] * 10)


solution(int(input()), input().strip().split())
