import java.io.*;
import java.util.*;

class Solution{
    public static void main(String[] args) throws IOException {
      // Scanner 클래스보다는 BufferedReader 클래스를 권장!
      // BufferedReader가 Scanner 보다 Buffer Size가 커서 속도가 상대적으로 빠름!
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      // 테스트케이스마다 print 하는 것 보다 sb에 저장해놓고 마지막에 한번에 print하는게 훨씬 빠름!
      StringBuilder sb = new StringBuilder();
      int t = Integer.parseInt(br.readLine());
      
      for(int tc=1; tc<t+1; tc++){
        int max = 0;
        
        //String[] token = br.readLine().split(" ");
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        //int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] a = new int[n]; // n개 만큼 배열 int 배열 생성
        st = new StringTokenizer(br.readLine()); // 공백을 구분자로 스트링토큰을 만듦
        for(int i=0; i<n; i++){
          a[i] = Integer.parseInt(st.nextToken()); // 토큰으로 배열 초기화
        }
        //int[] b = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); 
        int[] b = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<m; i++){
          b[i] = Integer.parseInt(st.nextToken());
        }        
        if(n >= m){
          for(int i=0; i<n-m+1; i++){
            int sum = 0;
            for(int j=0; j<m; j++){
              sum += a[j+i] * b[j];
            }
            if(sum > max){
              max = sum;
            }
          }
        }else{
          for(int i=0; i<m-n+1; i++){
            int sum = 0;
            for(int j=0; j<n; j++){
              sum += a[j] * b[j+i];
            }
            if(sum > max){
              max = sum;
            }
          }                    
        }
        sb.append("#" + tc + " " + max + "\n");
      }
      System.out.println(sb.toString()); // toSting메소드를 통해 StringBuilder의 값을 String으로 변환 

      br.close(); // 메모리 관리 위해 br 해제
    }
}
