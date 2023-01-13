import java.util.*;
import java.io.*;

public class Main {

  static int[][] turn90(int[][] arr, int n) { // 이차원 배열을 90도 회전시키는 함수
    int[][] new_arr = new int[n][n];
    for (int r = 0; r < n; r++) {
      for (int c = 0; c < n; c++) {
        new_arr[c][n - 1 - r] = arr[r][c];
      }
    }
    return new_arr;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    StringTokenizer st;
    int T = Integer.parseInt(br.readLine());
    for (int i = 1; i < T + 1; i++) { // 테스트 케이스만큼 실행
      int n = Integer.parseInt(br.readLine());      

      int[][] arr = new int[n][n]; // n*n의 배열 선언
      for (int r = 0; r < n; r++) {
        st = new StringTokenizer(br.readLine());
        for (int c = 0; c < n; c++) {
          arr[r][c] = Integer.parseInt(st.nextToken()); // 주어진 배열의 값을 받아옴
        }
        // for (int x=0; x<n; x++
        // System.out.println(Arrays.toString(arr[x]));
        //
      }

      int[][] arr90 = turn90(arr, n); // 90도 회전한 배열
      // for (int x=0; x<n; x++){
      // stem.out.println(Arrays.toString(arr90[x]));
      // }

      int[][] arr180 = turn90(arr90, n); // 180도 회전한 배열
      // for (int x=0; x<n; x++){
      // stem.out.println(Arrays.toString(arr180[x]));
      // }

      int[][] arr270 = turn90(arr180, n); // 270도 회전한 배열
      // for (int x=0; x<n; x++){
      // stem.out.println(Arrays.toString(arr270[x]));
      // }
      sb.append("#").append(i).append("\n");
      for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
          sb.append(arr90[r][c]);
        }
        sb.append(" ");
        for (int c = 0; c < n; c++) {
          sb.append(arr180[r][c]);
        }
        sb.append(" ");
        for (int c = 0; c < n; c++) {
          sb.append(arr270[r][c]);
        }
        sb.append("\n");
      }      
    }System.out.println(sb.toString());
  }
}