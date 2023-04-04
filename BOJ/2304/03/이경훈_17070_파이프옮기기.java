package _230329;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_17070_G5_파이프옮기기1_이경훈_BFS {
	static int N;
	static int[] dr = { 0, 1, 1 };
	static int[] dc = { 1, 0, 1 };
	static final int garo = 0;
	static final int sero = 1;
	static final int diag = 2;
	static int[][] graph;
	static int totalCnt;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		graph = new int[N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dfs(0, 1, 0);
		System.out.println(totalCnt);
	}

	private static void dfs(int r, int c, int dir) {
		if (r == N - 1 && c == N - 1) {
			totalCnt++;
			return;
		}

		if (dir == garo) {
			int nr = r + dr[0];
			int nc = c + dc[0];

			if (inside(nr, nc) && graph[nr][nc] == 0)
				dfs(nr, nc, garo);

			nr = r + dr[2];
			nc = c + dc[2];

			if (inside(nr, nc) && graph[nr][nc] == 0 && graph[nr - 1][nc] == 0 && graph[nr][nc - 1] == 0)
				dfs(nr, nc, diag);

		} else if (dir == sero) {
			int nr = r + dr[1];
			int nc = c + dc[1];

			if (inside(nr, nc) && graph[nr][nc] == 0)
				dfs(nr, nc, sero);

			nr = r + dr[2];
			nc = c + dc[2];

			if (inside(nr, nc) && graph[nr][nc] == 0 && graph[nr - 1][nc] == 0 && graph[nr][nc - 1] == 0)
				dfs(nr, nc, diag);

		} else {
			int nr = r + dr[0];
			int nc = c + dc[0];

			if (inside(nr, nc) && graph[nr][nc] == 0)
				dfs(nr, nc, garo);

			nr = r + dr[1];
			nc = c + dc[1];

			if (inside(nr, nc) && graph[nr][nc] == 0)
				dfs(nr, nc, sero);

			nr = r + dr[2];
			nc = c + dc[2];

			if (inside(nr, nc) && graph[nr][nc] == 0 && graph[nr - 1][nc] == 0 && graph[nr][nc - 1] == 0)
				dfs(nr, nc, diag);
		}
	}

	private static boolean inside(int nr, int nc) {
		if (-1 < nr && nr < N && -1 < nc && nc < N)
			return true;
		return false;
	}
}
