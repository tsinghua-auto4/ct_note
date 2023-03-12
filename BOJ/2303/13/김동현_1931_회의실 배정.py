import sys

n           = int(sys.stdin.readline().rstrip())
reservation = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    reservation.append([s, e])

reservation = sorted(reservation, key=lambda a:a[0]) # 시작 시간이 빠른 순 정렬
reservation = sorted(reservation, key=lambda a:a[1]) # 한번 더 끝나는 시간이 빠른 순으로 정렬

cnt, pe = 0, 0
for cs, ce in reservation:
    if pe <= cs:
        cnt += 1
        pe = ce
print(cnt)