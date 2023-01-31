import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_1339_문자삼각형2
 */
public class 이경훈_1339_문자삼각형2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());

		if (N % 2 == 0 || N <= 0 || N > 100) {
			System.out.println("INPUT ERROR");
			return;
		}
		char[][] arr = new char[N][N];
		char ch = 'A';

		for (int j = N / 2, k = 1; j >= 0; j--, k += 2) {
			for (int i = j; i < j + k; i++) {
				arr[i][j] = ch++;
				if (ch > 'Z')
					ch = 'A';
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == '\0') {
					System.out.print("  ");
				} else {
					System.out.print(arr[i][j] + " ");
				}
			}
			System.out.println();
		}
	}

}
