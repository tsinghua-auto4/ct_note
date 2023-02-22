import sys
input = sys.stdin.readline

def check(data):
    leng = len(data)
    for i in range(leng):
        if data[i] != data[leng - 1 - i]:
            return False
    return True

while(True):
    data = input().rstrip()
    if data == '0':
        break
    if(check(data)):
        print('yes')
    else:
        print('no')
