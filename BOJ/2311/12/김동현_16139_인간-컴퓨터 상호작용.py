import sys; input=sys.stdin.readline

s   = input().rstrip()
arr = [[0]*26]

arr[0][ord(s[0])-97] = 1
for iter in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[iter][ord(s[iter])-97] += 1

for _ in range(int(input())):
    c, l, r = list(input().split())
    l, r = int(l), int(r)
    if l == 0:
        print(arr[r][ord(c)-97])
    else:
        print(arr[r][ord(c)-97]-arr[l-1][ord(c)-97])