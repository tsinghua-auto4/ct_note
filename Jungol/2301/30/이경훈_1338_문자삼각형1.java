import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_1338_문자삼각형1
 */
public class 이경훈_1338_문자삼각형1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		
		char[][] arr = new char[n][n];
		char ch = 'A';

		for (int i = 0; i < n; i++) {
			for (int j = i, k = n-1; j < n; j++, k--) {
				arr[j][k] = ch++;
				if(ch > 'Z') ch = 'A';
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(arr[i][j] == '\0') {
					System.out.print("  ");
				} else {
					System.out.print(arr[i][j] + " ");
				}
			}
			System.out.println();
		}
	}
}
