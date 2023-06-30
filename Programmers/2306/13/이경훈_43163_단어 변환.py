def dfs(word, target, words, depth, visited, answer):
    if word == target:
        return min(answer, depth)
    
    for i in range(len(words)):
        if not visited[i] and check(word, words[i]):
            visited[i] = True
            answer = dfs(words[i], target, words, depth+1, visited, answer)
            visited[i] = False
    
    return answer

def check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    answer = dfs(begin, target, words, 0, visited, float('inf'))
    return answer if answer != float('inf') else 0

## 아래와 같이 bfs로도 가능
from collections import deque

def check(a, b):
    return sum([1 for x, y in zip(a,b) if x != y]) == 1

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append((begin, 0))
    while q:
        cur, depth = q.popleft()
        if cur == target:
            return depth
        
        for idx, word in enumerate(words):
            if not visited[idx] and check(cur, word):
                visited[idx] = True
                q.append((word, depth+1))
    return 0