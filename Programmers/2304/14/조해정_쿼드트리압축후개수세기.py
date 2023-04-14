answer = [0, 0]


def solution(arr):
    global answer
    check(arr, len(arr), 0, 0)
    return answer


def check(arr, size, x, y):
    global answer

    num = arr[x][y]
    if size == 1:
        answer[num] += 1
        return

    half = size // 2
    for dx in range(size):
        for dy in range(size):
            if num != arr[x + dx][y + dy]:
                check(arr, half, x, y)
                check(arr, half, x, y + half)
                check(arr, half, x + half, y)
                check(arr, half, x + half, y + half)
                return

    answer[num] += 1
