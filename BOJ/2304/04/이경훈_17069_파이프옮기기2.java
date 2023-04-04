package _230329;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_17069_G4_파이프옮기기2_이경훈 {
	static final int garo = 0;
	static final int sero = 1;
	static final int diag = 2;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] graph = new int[N + 1][N + 1];
		for (int i = 1; i <= N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		long[][][] dp = new long[N + 1][N + 1][3];
		dp[1][2][garo] = 1;

		for (int r = 1; r <= N; r++) {
			for (int c = 2; c <= N; c++) {
				if (r == 1 && c == 2)
					continue;
				if (graph[r][c] == 1)
					continue;

				dp[r][c][garo] = dp[r][c - 1][garo] + dp[r][c - 1][diag];
				dp[r][c][sero] = dp[r - 1][c][sero] + dp[r - 1][c][diag];

				if (graph[r - 1][c] == 1 || graph[r][c - 1] == 1)
					continue;
				dp[r][c][diag] = dp[r - 1][c - 1][garo] + dp[r - 1][c - 1][sero] + dp[r - 1][c - 1][diag];
			}
		}
		System.out.println(dp[N][N][garo] + dp[N][N][sero] + dp[N][N][diag]);
	}
}
