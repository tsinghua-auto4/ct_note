import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    hear = set()
    for _ in range(n):
        hear.add(input().rstrip())
    
    see  = set()
    for _ in range(m):
        see.add(input().rstrip())
    
    ans = sorted(list(hear&see))

    print(len(ans))
    for i in ans:
        print(i)