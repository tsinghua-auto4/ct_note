cur = 666
cnt = 0
tar = int(input())
while True:
    if '666' in str(cur):
        cnt += 1
        if cnt == tar:
            print(cur)
            break
    cur += 1