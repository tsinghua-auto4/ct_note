import sys
sys.setrecursionlimit(10**8)

def solution(s_in, e_in, s_po, e_po):
    if (s_in > e_in) or (s_po > e_po):
        return
    
    # post order의 마지막 node는 정점
    node = order_post[e_po]
    ans.append(node)

    lft = pos_inorder[node] - s_in # 좌측 노드 덩어리 길이
    rgt = e_in - pos_inorder[node] # 우측 노드 덩어리 길이

    solution(s_in, s_in+lft-1, s_po, s_po+lft-1) # 왼쪽
    solution(e_in-rgt+1, e_in, e_po-rgt, e_po-1) # 오른쪽


n          = int(sys.stdin.readline().rstrip())
order_in   = list(map(int, sys.stdin.readline().split()))
order_post = list(map(int, sys.stdin.readline().split()))

# element 위치가 in-order에서 어딘지?
pos_inorder = [0]*(n+1)
for i in range(n):
    pos_inorder[order_in[i]] = i

# pre order 저장
ans = []
solution(0, n-1, 0, n-1)
print(*ans)