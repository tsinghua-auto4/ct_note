def row_valid(sudoku): # 가로 검증
  for row in range(9):
    visited = [0] * 10
    for col in range(9):
      visited[sudoku[row][col]] += 1
    for val in range(1, 10):
      if visited[val] != 1:
        return False
  return True

def col_valid(sudoku): # 세로 검증
  for col in range(9):
    visited = [0] * 10
    for row in range(9):
      visited[sudoku[row][col]] += 1
    for val in range(1, 10):
      if visited[val] != 1:
        return False
  return True

def dia_valid(sudoku): #부분 리스트 검증
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      visited = [0] * 10
      for row in range(3):
        for col in range(3):
          visited[sudoku[row+i][col+j]] += 1
      for val in range(1, 10):
        if visited[val] != 1:
          return False
  return True

test_case = int(input())

for tc in range(1, test_case+1):
  sudoku = []
  for _ in range(9):
    sudoku.append(list(map(int, input().split())))
  if row_valid(sudoku) and col_valid(sudoku) and dia_valid(sudoku): # 만약 세가지 검증을 모두 통과하면
    print(f'#{tc} 1')
  else: # 그렇지 않으면
    print(f'#{tc} 0')
  