import java.io.*;
import java.util.*;

class Main {
  static HashSet<Integer> set = new HashSet<Integer>(); // set 선언

  static boolean rowCheck(int[][] sudoku) { // 스도쿠의 행 유효성 검증
    for (int i = 0; i < 9; i++) { 
      set.clear(); // set 객체 비우기
      for (int j = 0; j < 9; j++) { // set에 추가
        set.add(sudoku[i][j]);
      }
      if(set.size() < 9) return false; // 9개가 아니라면 중복된 숫자가 있다는 것
    }
    return true;
  }

  static boolean colCheck(int[][] sudoku) { // 스도쿠의 열 유효성 검증
    for (int i = 0; i < 9; i++) { 
      set.clear();
      for (int j = 0; j < 9; j++) {
        set.add(sudoku[j][i]);
      }
      if(set.size() < 9) return false;    
    }
    return true;
  }

  static boolean diaCheck(int[][] sudoku) { // 스도쿠의 부분 사각형 검증
    for (int i = 0; i < 9; i += 3) {
      for (int j = 0; j < 9; j += 3) {
        set.clear();
        for (int r = 0; r < 3; r++) {
          for (int c = 0; c < 3; c++) {
            set.add(sudoku[r + i][c + j]);
          }          
        }
        if(set.size() < 9) return false;
      }
    }
    return true;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int tc = Integer.parseInt(br.readLine());
    int[][] sudoku;

    for (int t = 1; t < tc + 1; t++) { // Test_Case
      boolean flag; // 유효성 체크용 flag
      sudoku = new int[9][9];
      for (int i = 0; i < 9; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < 9; j++) {
          sudoku[i][j] = Integer.parseInt(st.nextToken());
        }
      }
      flag = rowCheck(sudoku) && colCheck(sudoku) && diaCheck(sudoku); // 세 조건을 만족하면 true

      if (flag) {
        System.out.println("#" + t + " " + 1);
      } else {
        System.out.println("#" + t + " " + 0);
      }
    }
  }
}