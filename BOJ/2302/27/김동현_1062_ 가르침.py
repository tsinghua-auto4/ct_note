import sys

def solution(idx, cnt):
    global ans

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            flag = True
            for c in word:
                if not bitmsk[ord(c) - ord('a')]:
                    flag = False
                    break
            if flag:
                readcnt += 1
        ans = max(ans, readcnt)
        return
    
    for i in range(idx, 26):
        if bitmsk[i] == 0:
            bitmsk[i] = 1
            solution(i, cnt+1)
            bitmsk[i] = 0


n, k  = map(int, sys.stdin.readline().split())
if k < 5:
    print(0)
    exit()
if k == 26:
    print(n)
    exit()
words = [] # a,n,t,i,c (anta, tica)
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

ans       = 0
bitmsk    = [0] * 26
anta_tica = {'a','n','t','i','c'}
for cur in anta_tica:
    bitmsk[ord(cur) - ord('a')] = 1

solution(0, 0)
print(ans)