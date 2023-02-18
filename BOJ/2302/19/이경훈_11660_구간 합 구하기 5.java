package com.ssafy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_11660_S1_구간합구하기5_이경훈 {
	static int N;
	static int M;
	static int[][] prefix_sum;
	static int[][] N_data;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		N_data = new int[N + 1][N + 1];
		prefix_sum = new int[N + 1][N + 1];

		StringBuilder sb = new StringBuilder();

		// 입력
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				N_data[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 구간합 구하기
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
						+ N_data[i][j];
			}
		}

		for (int i = 0; i < M; i++) {
			int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
			int ans = 0;
			st = new StringTokenizer(br.readLine());
			x1 = Integer.parseInt(st.nextToken());
			y1 = Integer.parseInt(st.nextToken());
			x2 = Integer.parseInt(st.nextToken());
			y2 = Integer.parseInt(st.nextToken());

			ans += prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1];

			sb.append(ans).append("\n");
		}
		System.out.println(sb.toString());
	}
}
