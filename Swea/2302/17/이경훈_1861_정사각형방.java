package com.ssafy;

import java.util.Scanner;

public class Solution_1861_D4_정사각형방_이경훈 {
	static class point {
		int r;
		int c;

		public point() {
		}

		public point(int r, int c) {
			this.r = r;
			this.c = c;
		}

	}

	static int[][] map;
	static int n;
	static int[] dr = { -1, 1, 0, 0 }; // 상하좌우
	static int[] dc = { 0, 0, -1, 1 };
	static int totalCnt;
	static int number;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();
			map = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			totalCnt = 0;
			number = n * n + 1;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					dfs(new point(i, j), 1, new point(i, j));
				}
			}

			System.out.printf("#%d %d %d", tc, number, totalCnt);
			System.out.println();
		}
	}

	private static void dfs(point p, int cnt, point origin) {
		if (cnt > totalCnt) {
			totalCnt = cnt;
			number = map[origin.r][origin.c];
		} else if (cnt == totalCnt) {
			number = Math.min(number, map[origin.r][origin.c]);
		}
		for (int i = 0; i < 4; i++) {
			int nr = p.r + dr[i];
			int nc = p.c + dc[i];
			if (-1 < nr && nr < n && -1 < nc && nc < n) {
				if (map[nr][nc] == map[p.r][p.c] + 1) {
					dfs(new point(nr, nc), cnt + 1, origin);
				}
			}
		}
		return;
	}
}
