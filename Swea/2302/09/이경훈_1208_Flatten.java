import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 이경훈_1208_Flatten {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int dump;
		int[] boxes = new int[100];

		for (int tc = 1; tc <= 10; tc++) {
			dump = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());

			for (int i = 0; i < 100; i++) {
				boxes[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 0; i < dump; i++) {
				Arrays.sort(boxes);
				if (boxes[99] - boxes[0] < 2) {
					break;
				}
				boxes[0]++;
				boxes[99]--;
			}
			Arrays.sort(boxes);
			System.out.printf("#%d %d\n", tc, boxes[99] - boxes[0]);
		}
	}
}
