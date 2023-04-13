def solution(N, number):
    idx = 0
    dic = {}

    while idx < 8:
        idx += 1
        NNN = int(str(N) * idx)
        if NNN == number:
            return idx
        dic[idx] = {NNN}

        for i in range(1, idx // 2 + 1):
            j = idx - i
            for x in dic[i]:
                for y in dic[j]:
                    temp = {x + y, x - y, -x + y, x * y}
                    temp.update({0} if not x or not y else {x // y, y // x})
                    if number in temp:
                        return idx
                    dic[idx].update(temp)

    return -1
