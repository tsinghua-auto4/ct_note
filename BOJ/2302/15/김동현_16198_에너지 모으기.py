import sys

def solution(left, bead, total):
    global val_max

    if left == 2:
        val_max = max(val_max, total)
        return

    for i in range(1, left-1):
        solution(left-1, bead[0:i] + bead[i+1: left+1], total + bead[i-1] * bead[i+1])


if __name__ == "__main__":
    n     = int(sys.stdin.readline())
    beads = list(map(int, sys.stdin.readline().split()))

    val_max = 0

    solution(n, beads, 0)

    print(val_max)