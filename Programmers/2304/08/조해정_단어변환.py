from collections import deque


def is1diff(word, compare):
    if len(word) != len(compare):
        return False

    ans = 0
    for i in range(len(word)):
        if word[i] != compare[i]:
            ans += 1

    if ans == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    dic = {begin: []}
    for word in words:
        if is1diff(begin, word):
            dic[begin].append(word)

    for word in words:
        dic[word] = []
        for word2 in words:
            if word == word2:
                continue
            if is1diff(word, word2):
                dic[word].append(word2)

    visited = {w: False for w in words}
    q = deque([[begin, 0]])

    while q:
        w, i = q.popleft()
        if w == target:
            return i

        for t in dic[w]:
            if not visited[t]:
                visited[t] = True
                q.append([t, i+1])

    return answer
