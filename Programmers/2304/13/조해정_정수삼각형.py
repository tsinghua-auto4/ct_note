def solution(triangle):
    answer = triangle[0]
    h = len(triangle)

    for i in range(1, h):
        temp = triangle[i]
        for j in range(i + 1):
            left = j - 1 if j != 0 else 0
            right = j if j != i else -1
            temp[j] += max(answer[left], answer[right])
        answer = temp[:]

    return max(answer)


"""
방법2
def solution(triangle):
    for h in range(len(triangle)-1, 0, -1):
        for i in range(h):
            triangle[h-1][i] += max([triangle[h][i], triangle[h][i+1]])
    return triangle[0][0]
"""
