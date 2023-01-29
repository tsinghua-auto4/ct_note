import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_2046_숫자사각형4
 */
public class 이경훈_2046_숫자사각형4 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		if (m == 1) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					System.out.printf("%d ", i);
				}
				System.out.println();
			}
		} else if (m == 2) {
			for (int i = 1; i <= n; i++) {
				if (i % 2 != 0) {
					for (int j = 1; j <= n; j++) {
						System.out.printf("%d ", j);
					}
					System.out.println();
				} else {
					for (int j = n; j > 0; j--) {
						System.out.printf("%d ", j);
					}
					System.out.println();
				}

			}
		} else {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					System.out.printf("%d ", i * j);
				}
				System.out.println();
			}
		}

	}
}