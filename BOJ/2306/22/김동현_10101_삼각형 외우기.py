
angle = []
for _ in range(3):
    angle.append(int(input()))

if angle.count(60) == 3:
    print("Equilateral")
elif sum(angle) == 180:
    if angle.count(angle[0]) == 2 or angle.count(angle[1]) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")