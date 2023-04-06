import sys

def solution():
    global n, students, favor, pos, ans

    for idx in range(len(students)):
        cur = students[idx] # 지금 자리 배치하는 학생
        tmp = [] # 학생의 자리 후보 저장 리스트
        # 모든 자리를 다 돌아보면서, 좋아하는 학생이 있는지, 빈자리가 얼마나 있는지 확인하고 후보 리스트에 저장하자
        for i in range(n):
            for j in range(n):
                if pos[i][j] == 0:
                    like  = 0
                    blank = 0
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i+dx, j+dy
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        if pos[nx][ny] in favor[cur]:
                            like += 1
                        if pos[nx][ny] == 0:
                            blank += 1
                    tmp.append([like, blank, i, j])
        # 후보 중에서, like/blank 가 많은 순 + i/j가 작은 순으로 정렬을 해보자
        tmp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
        x, y = tmp[0][2], tmp[0][3]
        pos[x][y] = cur

    for i in range(n):
        for j in range(n):
            cur = pos[i][j]
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i+dx, j+dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if pos[nx][ny] in favor[cur]:
                    cnt += 1
            if cnt != 0:
                ans += 10**(cnt-1)

n        = int(sys.stdin.readline().rstrip())
students = [] # 여기에 자리를 정해줄 학생을 순서대로 넣을 예정
favor    = {} # 각 학생이 좋아하는 학생 리스트를 넣어줄 예정
pos      = [[0]*n for _ in range(n)] # 학생들의 자리를 저장할 메모리
ans      = 0 # 출력할 답

for _ in range(n**2):
    tmp = list(map(int, sys.stdin.readline().split()))
    students.append(tmp[0])
    favor[tmp[0]] = tmp[1:]

solution()
print(ans)