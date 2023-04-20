
def solution():
    target = 0
    for _ in range(int(input())):
        target += int(input())
    if target > 0:
        print("+")
    elif target == 0:
        print("0")
    else:
        print("-")

for _ in range(3):
    solution()