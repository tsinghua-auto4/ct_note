a = int(input())
b = int(input())

c = b-a
fine = 0
if c <= 0:
    print("Congratulations, you are within the speed limit!")
    exit()
elif c <= 20:
    fine = 100
elif c <= 30:
    fine = 270
else:
    fine = 500
print("You are speeding and your fine is $%d." %fine)