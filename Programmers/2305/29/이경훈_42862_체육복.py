# 내가 짠 코드 - set를 이용해서 해결
def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    a = reserve - lost
    b = lost - reserve
    cnt = 0
    
    for student in b:
        if student-1 in a:
            a.remove(student-1)
            continue
        elif student+1 in a:
            a.remove(student+1)
            continue
        else:
            cnt += 1
            
    return n - cnt

# GPT가 짜준 코드 - 배열로 처리
def solution(n, lost, reserve):
    students = [1] * n # 체육복 수를 기록하는 리스트 생성

    # 도난당한 학생들과 여벌 체육복 있는 학생들 처리
    for l in lost: 
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    # 체육복을 빌려 주기
    for i, s in enumerate(students):
        if s == 0: # 체육복이 없는 학생일 경우
            if i > 0 and students[i-1] > 1: # 앞 번호의 학생이 여벌 체육복을 가지고 있는 경우
                students[i-1] -= 1
                students[i] += 1
            elif i < n-1 and students[i+1] > 1: # 뒷 번호의 학생이 여벌 체육복을 가지고 있는 경우
                students[i+1] -= 1
                students[i] += 1

    answer = n - students.count(0) # 참여 가능한 학생들의 수 계산
    return answer