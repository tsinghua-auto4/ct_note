import sys

def solution():
    data = {}
    data["A+"] = 4.3
    data["A0"] = 4.0
    data["A-"] = 3.7

    data["B+"] = 3.3
    data["B0"] = 3.0
    data["B-"] = 2.7

    data["C+"] = 2.3
    data["C0"] = 2.0
    data["C-"] = 1.7

    data["D+"] = 1.3
    data["D0"] = 1.0
    data["D-"] = 0.7

    data["F"] = 0.0

    print(data[sys.stdin.readline().rstrip()])

solution()