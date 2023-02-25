package com.ssafy._230225;

import java.util.Scanner;

public class Solution_1949_모의_등산로조성_이경훈 {
	static int[][] map, copyMap;
	static int N, K;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int[][][] dist;
	static boolean[][] visited;
	static int ans;
	static int high;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			K = sc.nextInt();
			map = new int[N][N];
			copyMap = new int[N][N];
			ans = 0;
			high = 0;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
					high = Math.max(high, map[i][j]);
				}
			}

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j] == high) {
						initMap();
						dist = new int[N][N][2];
						visited = new boolean[N][N];
						dfs(i, j, 0);

						ans = Math.max(ans, findMaxVal());
					}
				}
			}
			System.out.printf("#%d %d%n", tc, ans + 1);
		}

	}

	private static void initMap() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				copyMap[i][j] = map[i][j];
			}
		}
	}

	private static void dfs(int x, int y, int flag) {
		visited[x][y] = true;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (-1 < nx && nx < N && -1 < ny && ny < N && copyMap[nx][ny] < copyMap[x][y] && !visited[nx][ny]) {
				if (dist[nx][ny][flag] <= dist[x][y][flag] + 1) {
					dist[nx][ny][flag] = dist[x][y][flag] + 1;
					dfs(nx, ny, flag);
					visited[nx][ny] = false;
				}

			} else if (-1 < nx && nx < N && -1 < ny && ny < N && flag == 0 && copyMap[x][y] > copyMap[nx][ny] - K
					&& !visited[nx][ny]) {
				dist[nx][ny][flag + 1] = dist[x][y][flag] + 1;
				int temp = copyMap[nx][ny];
				copyMap[nx][ny] = copyMap[x][y] - 1;
				dfs(nx, ny, flag + 1);
				visited[nx][ny] = false;
				copyMap[nx][ny] = temp;
			}
		}
	}

	private static int findMaxVal() {
		int ans = 0;

		for (int[][] iss : dist) {
			for (int[] is : iss) {
				for (int i : is) {
					ans = Math.max(ans, i);
				}
			}
		}
		return ans;
	}

}
