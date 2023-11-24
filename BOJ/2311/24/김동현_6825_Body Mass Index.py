weight = float(input())
height = float(input())

ans = weight/height**2
if ans > 25:
    print("Overweight")
elif 18.5 <= ans <= 25:
    print("Normal weight")
else:
    print("Underweight")