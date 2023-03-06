package com.ssafy._230305;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution_2115_모의_벌꿀채취_이경훈 {
	static int N, M, newM, C;
	static int[][] map;
	static boolean[] visited;
	static int MAX_PROFIT;
	static int profit;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			M = sc.nextInt();
			newM = N - M + 1;
			C = sc.nextInt();

			map = new int[N][N];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			MAX_PROFIT = 0;
			combi(0, 0);

			System.out.println("#" + tc + " " + MAX_PROFIT);
		}
	}

	static List<Integer> idxList = new ArrayList<>();

	private static void combi(int depth, int start) {
		if (depth == 2) {
			if ((idxList.get(1) / (newM) != idxList.get(0) / (newM))
					|| (idxList.get(1) / (newM) == idxList.get(0) / (newM)
							&& idxList.get(1) - idxList.get(0) >= newM)) {
				visited = new boolean[M];
				int r = idxList.get(0) / (newM);
				int c = idxList.get(0) % (newM);

				profit = 0;
				getHoney(0, r, c); // 시작좌표

				int first_profit = profit;

				visited = new boolean[M];
				r = idxList.get(1) / (newM);
				c = idxList.get(1) % (newM);

				profit = 0;
				getHoney(0, r, c); // 시작좌표

				int second_profit = profit;

				MAX_PROFIT = Math.max(MAX_PROFIT, first_profit + second_profit);

			}
			return;
		}
		for (int i = start; i < N * (N - M + 1); i++) {
			idxList.add(i);
			combi(depth + 1, i + 1);
			idxList.remove(idxList.size() - 1);
		}
	}

	private static void getHoney(int depth, int r, int c) {
		if (depth == M) {
			int sum = 0;
			int _profit = 0;
			for (int i = 0; i < M; i++) {
				if (visited[i]) {
					sum += map[r][c + i];
					if (sum > C)
						return;
					_profit += map[r][c + i] * map[r][c + i];
				}
			}
			if (_profit > profit) {
				profit = _profit;
			}
			profit = Math.max(profit, _profit);
			return;
		}

		visited[depth] = true;
		getHoney(depth + 1, r, c);
		visited[depth] = false;
		getHoney(depth + 1, r, c);
	}
}
