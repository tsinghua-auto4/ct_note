package _230330;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1278_IM_배낭채우기2_이경훈 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		int[] weights = new int[N + 1];
		int[] profits = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			weights[i] = Integer.parseInt(st.nextToken());
			profits[i] = Integer.parseInt(st.nextToken());
		}

		// dp[i번째까지의 보석을 고려][가방의 최대 용량이 j]
		int dp[][] = new int[N + 1][W + 1];

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= W; j++) {
				if (weights[i] > j) { // 이번에 고려한 보석의 무게가 가방의 최대 용량보다 크면 전 보석까지 고려한 값을 넣어줌
					dp[i][j] = dp[i - 1][j];
				} else {
					dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weights[i]] + profits[i]);
				}
			}
		}
		System.out.println(dp[N][W]);
	}
}
