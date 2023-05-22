def solution(array, commands):
    answer = []
    for i, j, k in commands:
        A = sorted(array[i-1: j])[k-1]
        answer.append(A)
    return answer