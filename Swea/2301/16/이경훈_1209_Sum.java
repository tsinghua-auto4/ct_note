import java.io.*;
import java.util.*;

public class 이경훈_1209_Sum {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] data = new int[100][100];
		for (int tc = 0; tc < 10; tc++) {
			int t = Integer.parseInt(br.readLine());

			for (int i = 0; i < 100; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 100; j++) {
					data[i][j] = Integer.parseInt(st.nextToken());
				}
			}
      
			int max = 0;

			for (int i = 0; i < 100; i++) {
				int sum = 0;
				for (int j = 0; j < 100; j++) {
					sum += data[i][j];
				}
				if (sum > max) {
					max = sum;
				}
			}

			for (int i = 0; i < 100; i++) {
				int sum = 0;
				for (int j = 0; j < 100; j++) {
					sum += data[j][i];
				}
				if (sum > max) {
					max = sum;
				}
			}

			int sum1 = 0;
			for (int i = 0; i < 100; i++) {
				sum1 += data[i][i];
			}
			if (sum1 > max) {
				max = sum1;
			}

			int sum2 = 0;
			for (int i = 0; i < 100; i++) {
				sum2 += data[i][99 - i];
			}
			if (sum2 > max) {
				max = sum2;
			}

			System.out.println("#" + t + " " + max);

		}
	}
}
