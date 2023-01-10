import java.io.*;
import java.util.*;

class Main {
  static boolean rowcolCheck(int[][] sudoku) { // 스도쿠의 행, 열 유효성 검증
    for (int i = 0; i < 9; i++) { 
      int[] visited1 = new int[10];
      int[] visited2 = new int[10];
      for (int j = 0; j < 9; j++) { // 배열을 0으로 초기화
        visited1[j] = 0;
        visited2[j] = 0;
      }
      for (int j = 0; j < 9; j++) { // 나온 갯수 파악
        visited1[sudoku[i][j]]++;
        visited2[sudoku[j][i]]++;
      }
      for (int k = 1; k < 10; k++) { // 한번도 안나오거나 두번 이상 나오면 return false
        if (visited1[k] != 1 || visited2[k] != 1) {
          return false;
        }
      }
    }
    return true;
  }

  static boolean diaCheck(int[][] sudoku) { // 스도쿠의 부분 사각형 검증
    for (int i = 0; i < 9; i += 3) {
      for (int j = 0; j < 9; j += 3) {
        int[] visited = new int[10];
        for (int k = 0; k < 9; k++) { // 배열을 0으로 초기화
        visited[k] = 0;
        }
        for (int r = 0; r < 3; r++) { // 나온 갯수 파악
          for (int c = 0; c < 3; c++) {
            visited[sudoku[r + i][c + j]]++;
          }
        }
        for (int k = 1; k < 10; k++) { // 한번도 안나오거나 두번 이상 나오면 return false
          if (visited[k] != 1) {
            return false;
          }
        }
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

      flag = rowcolCheck(sudoku) && diaCheck(sudoku); // 두 조건을 만족하면 true

      if (flag) {
        System.out.println("#" + t + " " + 1);
      } else {
        System.out.println("#" + t + " " + 0);
      }
    }
  }
}
