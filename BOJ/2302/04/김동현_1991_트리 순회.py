import sys
from collections import deque

def preorder(root, tree):
    if root != '.':
        print(root, end='')            # root
        preorder(tree[root][0], tree)  # left
        preorder(tree[root][1], tree)  # right

def inorder(root, tree):
    if root != '.':
        inorder(tree[root][0], tree)  # left
        print(root, end='')           # root
        inorder(tree[root][1], tree)  # right

def postorder(root, tree):
    if root != '.':
        postorder(tree[root][0], tree)  # left
        postorder(tree[root][1], tree)  # right
        print(root, end='')             # root


if __name__ == "__main__":
    n    = int(sys.stdin.readline())
    tree = {}

    for _ in range(n):
        root, lft, rgt = map(str, sys.stdin.readline().split())
        tree[root] = [lft, rgt]
    
    preorder('A', tree)
    print()
    inorder('A', tree)
    print()
    postorder('A', tree)
    print()