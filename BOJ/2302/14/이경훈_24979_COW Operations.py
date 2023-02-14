import sys
input = sys.stdin.readline

# 입력
s = input()
ans = []

c = [0] * len(s)
o = [0] * len(s)
w = [0] * len(s)

prefix_sum_c = [0] * len(s)
prefix_sum_o = [0] * len(s)
prefix_sum_w = [0] * len(s)

# 문자열에서 c, o, w를 찾을 때 마다 각각의 리스트에 넣어줌
for i in range(len(s)):
  if s[i] == 'C':
    c[i] = 1
  elif s[i] == 'O':
    o[i] = 1
  else:
    w[i] = 1

# 누적합의 첫번째 값 셋팅
prefix_sum_c[0] = c[0]
prefix_sum_o[0] = o[0]
prefix_sum_w[0] = w[0]

# 각각의 리스트로부터 누적합 구함
for i in range(1, len(s)):
  prefix_sum_c[i] = prefix_sum_c[i-1] + c[i]
  prefix_sum_o[i] = prefix_sum_o[i-1] + o[i]
  prefix_sum_w[i] = prefix_sum_w[i-1] + w[i]
  
# 테스트케이스 시작
for _ in range(int(input())):
  flag = False
  i, j = map(int, input().split())

  # 처음부터 시작이라면 누적합 리스트의 끝값만 구하면 되고 중간부분을 구하고 싶다면 누적합의 끝값 - (시작값 - 1)
  if i == 1:
    c_len = prefix_sum_c[j-1]
    o_len = prefix_sum_o[j-1]
    w_len = prefix_sum_w[j-1]
  else:
    c_len = prefix_sum_c[j-1] - prefix_sum_c[i-2]
    o_len = prefix_sum_o[j-1] - prefix_sum_o[i-2]
    w_len = prefix_sum_w[j-1] - prefix_sum_w[i-2]

  # w 문자들을 모두 c와 o로 변환해줌
  if w_len > 0:
    c_len += w_len
    o_len += w_len

  # 오직 o 문자들이 짝수개 존재하고 c 문자들이 홀수개 있을 때 'c' 도출 가능.
  if o_len % 2 == 0:
    if c_len % 2 == 1:
      flag = True
  ans.append('Y') if flag else ans.append('N')

print(''.join(ans))
