D, H, M = map(int, input().split())
time = (D-11)*60*24 + (H-11)*60 + (M-11)
print(time if time >= 0 else -1)