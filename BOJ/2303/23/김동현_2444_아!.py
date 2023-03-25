import sys

jaehwan = str(sys.stdin.readline().rstrip())
doctor  = str(sys.stdin.readline().rstrip())

if len(jaehwan) >= len(doctor):
    print("go")
else:
    print("no")
