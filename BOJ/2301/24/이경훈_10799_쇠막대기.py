data = list(input())
st = []
ans = 0
for i in range(len(data)):
  # '(' 라면 스택에 넣음
  if data[i] == '(':
    st.append('(')
  else: # ')' 라면
    # 그 전의 값이 '(' 였다면 하나 빼주고 스택에 있는 갯수만큼 더해줌
    if data[i-1] == '(': 
      st.pop()
      ans += len(st)
    # 그 전의 값이 ')' 였다면 1만 더해줌
    else:
      st.pop()
      ans += 1
print(ans)