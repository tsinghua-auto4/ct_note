import math

iter = 0
while True:
    iter += 1
    a, b, c = map(float, input().split())
    if b == 0.:
        break
    
    mile = a/63360*math.pi*b
    mph = 3600*mile/c
    print("Trip #%d: %.2f %.2f" %(iter, mile, mph))