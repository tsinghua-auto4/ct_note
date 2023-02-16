import java.util.Scanner;

public class Solution_5215_D3_햄버거다이어트_이경훈 {
	static int MAXVAL;
	static int N, L;
	static int[][] data;
	static boolean isSelected[];
	static int limit;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			L = sc.nextInt();
			data = new int[N][2];
			for (int i = 0; i < N; i++) {
				data[i][0] = sc.nextInt();
				data[i][1] = sc.nextInt();
			}
			isSelected = new boolean[N];
			MAXVAL = 0;
			subSet(0, 0, 0);
			System.out.printf("#%d %d", tc, MAXVAL);
			System.out.println();
		}
	}

	static void subSet(int cnt, int yum_sum, int cal_sum) {
		if (cal_sum > L)
			return;
		if (cnt == N) {
			if (yum_sum > MAXVAL)
				MAXVAL = yum_sum;
			return;
		}
		subSet(cnt + 1, yum_sum + data[cnt][0], cal_sum + data[cnt][1]);
		subSet(cnt + 1, yum_sum, cal_sum);
	}
}
