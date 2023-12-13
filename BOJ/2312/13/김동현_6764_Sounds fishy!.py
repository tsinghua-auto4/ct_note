data = [int(input()) for _ in range(4)]
r    = 0
for iter in range(3):
    if data[iter] < data[iter+1]:
        r += 1
    elif data[iter] > data[iter+1]:
        r -= 1

if len(set(data)) == 1: 
    print("Fish At Constant Depth")
elif r == 3:
    print("Fish Rising")
elif r == -3:    
    print("Fish Diving")
else:
    print("No Fish")