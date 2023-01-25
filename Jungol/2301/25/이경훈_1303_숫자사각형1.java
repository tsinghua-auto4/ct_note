import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_1303_숫자사각형1
 */
public class 이경훈_1303_숫자사각형1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int num = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.printf("%d ", num++);
			}
			System.out.println();
		}
	}
}
