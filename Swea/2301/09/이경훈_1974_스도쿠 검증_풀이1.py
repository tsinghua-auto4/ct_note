# set에 넣고 개수를 파악해서 중복되지 않고 1부터 9까지 있는지 파악 가능

def valid_check(sudoku):
  for r in range(9):
    row = set()
    col = set()
    for c in range(9):
      row.add(sudoku[r][c])
      col.add(sudoku[c][r])
    if len(row) != 9 or len(col) != 9:
      return False
  
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      test = set()
      for r in range(3):
        for c in range(3):
          test.add(sudoku[r+i][c+j])
      if len(test) != 9:
        return False
  return True

T = int(input()) # 테스트케이스
for test_case in range(1, T + 1):  
  sudoku = [list(map(int, input().split())) for _ in range(9)]  
  print(f'#{test_case} {1 if valid_check(sudoku) else 0}') # f string