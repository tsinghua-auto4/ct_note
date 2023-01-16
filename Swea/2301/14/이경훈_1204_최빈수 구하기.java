import java.io.*;
import java.util.*;
 
public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());

    for(int tc=1; tc<t+1; tc++){
      br.readLine();
      StringTokenizer st = new StringTokenizer(br.readLine());
      int[] grade = new int[101]; // 0 ~ 100의 점수 범위
      for (int i = 0; i < 1000; i++) { // 학생이 1000명
        grade[Integer.parseInt(st.nextToken())]++; // 점수가 나오면 1 추가
      }

      int max = 0;
      for(int i = 0; i < 101; i++){
        if(grade[i] >= grade[max]){
          max = i;
        }
      }
      System.out.println("#"+tc+" "+max);
    }
  }
}