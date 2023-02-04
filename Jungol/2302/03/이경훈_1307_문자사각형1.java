import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_1307_문자사각형1
 */
public class 이경훈_1307_문자사각형1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		char ch = 'A';
		char[][] arr = new char[n][n];
		
		for (int i = n-1; i >= 0; i--) {
			for (int j = n-1; j >= 0; j--) {
				arr[j][i] =  ch++;
				if(ch > 'Z') ch = 'A';
			}			
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.printf("%c", arr[i][j]);
				if(j != n-1) System.out.print(" ");
			}
			System.out.println();
		}
	}
}
