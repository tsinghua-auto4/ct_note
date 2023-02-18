package com.ssafy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_9229_D3_한빈이와SpotMart_이경훈 {
	static int ans;
	static int sum;
	static int N;
	static int M;
	static int[] snacks;
	static int[] idxs;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			snacks = new int[N];

			// 데이터 입력
			for (int i = 0; i < N; i++) {
				snacks[i] = Integer.parseInt(st.nextToken());
			}
			ans = -1;
			sum = 0;
			idxs = new int[2];
			combi(0, 0);

			System.out.printf("#%d %d", tc, ans);
			System.out.println();
		}
	}

	// 비트마스킹 조합
	static void combi(int cnt, int flag) {
		if (cnt == 2) {
			sum = snacks[idxs[0]] + snacks[idxs[1]];
			if (sum <= M && sum > ans) {
				ans = sum;
			}
			return;
		}
		for (int i = 0; i < N; i++) {
			if ((flag & 1 << i) == 0) { // 아직 안고름
				idxs[cnt] = i;
				combi(cnt + 1, flag | 1 << i); // 고르고 방문처리
			}
		}
	}
}
