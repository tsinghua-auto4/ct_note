import sys
input = sys.stdin.readline

# 입력
s = input().rstrip()
ans = set()

# s_len으로 부분 문자열의 길이 조절, i로 시작 인덱스 조정
for s_len in range(1, len(s)+1):
  for i in range(len(s)-s_len+1):
    ans.add(s[i:i+s_len])

# 출력
print(len(ans))
