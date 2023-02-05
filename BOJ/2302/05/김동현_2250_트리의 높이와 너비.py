import sys
sys.setrecursionlimit(10**6)

def inorder(root, tree, depth, visited):
    global cnt
    if root != -1:
        inorder(tree[root][0], tree, depth+1, visited)
        visited[depth].append(cnt)
        cnt += 1
        inorder(tree[root][1], tree, depth+1, visited)

def maxFinder(visited):
    ans = (-1, -1)
    for cur in visited:
        if len(visited[cur]) > 0: #노드가 1개인 특수한 상황까지 고려
            if ans[1] < visited[cur][-1] - visited[cur][0] + 1:
                ans = (cur, visited[cur][-1] - visited[cur][0] + 1)
    return ans


if __name__ == "__main__":
    n       = int(sys.stdin.readline())
    tree    = {} # dict 형식 root: left right 저장
    visited = {} # dict 형식 depth: col 저장
    child   = {} # root 제외 모든 child node 저장, hash 구조 사용
    for i in range(n):
        root, left, right = map(int, sys.stdin.readline().split())
        tree[root]   = [left, right]
        visited[i+1] = []
        child[left]  = 0
        child[right] = 0
    
    root = -1
    for i in range(1, n+1):
        if i not in child:
            root = i
            break

    cnt   = 1 # col counter
    depth = 1 # depth counter, 밑줄 inorder에는 그냥 상수 1 넣어줘도 됨
    inorder(root, tree, depth, visited)
    print(*maxFinder(visited))
