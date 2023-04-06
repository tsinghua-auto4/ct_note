def solution(word):
    answer = 0
    dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    idx_num = [781, 156, 31, 6, 1]
    for i, w in enumerate(list(word)):
        answer += (dict[w] - 1) * idx_num[i]
    answer += len(word)
    return answer
