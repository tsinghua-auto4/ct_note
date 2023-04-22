package _230403;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main_3055_G4_탈출_이경훈{
	static class Pos {
		int r, c, status;

		public Pos(int r, int c, int status) {
			super();
			this.r = r;
			this.c = c;
			this.status = status;
		}
	}

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static final char BLANK = '.';
	static final char WATER = '*';
	static final char STONE = 'X';
	static final char END = 'D';
	static final char START = 'S';
	static int R, C, sR, sC, eR, eC;
	static char[][] map;
	static int[][][] visited;
	static int ans;

	static List<Pos> water_list;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];
		visited = new int[R][C][2];
		water_list = new ArrayList<>();
		for (int i = 0; i < R; i++) {
			String temp = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = temp.charAt(j);
				if (map[i][j] == START) {
					sR = i;
					sC = j;
					map[i][j] = BLANK;
				}
				if (map[i][j] == WATER) {
					water_list.add(new Pos(i, j, 1));
				}
				if (map[i][j] == END) {
					eR = i;
					eC = j;
				}
			}
		}
		bfs();
		if (ans == 0) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(ans - 1);
		}
	}

	private static void bfs() {
		ArrayDeque<Pos> q = new ArrayDeque<>();
		for (Pos pos : water_list) {
			q.offer(new Pos(pos.r, pos.c, pos.status));
			visited[pos.r][pos.c][pos.status] = 1;
		}
		q.offer(new Pos(sR, sC, 0));
		visited[sR][sC][0] = 1;

		while (!q.isEmpty()) {
			Pos pos = q.poll();
			int r = pos.r;
			int c = pos.c;
			int status = pos.status;

			if (r == eR && c == eC && status == 0) {
				ans = visited[r][c][0];
				return;
			}

			if (status == 0) { // 고슴도치면
				for (int i = 0; i < 4; i++) {
					int nr = r + dr[i];
					int nc = c + dc[i];

					if (!inside(nr, nc))
						continue;

					if (visited[nr][nc][status] != 0)
						continue;

					if (map[nr][nc] == STONE)
						continue;

					if (map[nr][nc] == WATER)
						continue;

					q.offer(new Pos(nr, nc, status));
					visited[nr][nc][status] = visited[r][c][status] + 1;

				}
			} else { // 물이면
				for (int i = 0; i < 4; i++) {
					int nr = r + dr[i];
					int nc = c + dc[i];

					if (!inside(nr, nc))
						continue;

					if (visited[nr][nc][status] != 0)
						continue;

					if (map[nr][nc] == STONE)
						continue;

					if (map[nr][nc] == END)
						continue;

					q.offer(new Pos(nr, nc, status));
					map[nr][nc] = WATER;
					visited[nr][nc][status] = 1;

				}
			}
		}
	}

	private static boolean inside(int nr, int nc) {
		return -1 < nr && nr < R && -1 < nc && nc < C;
	}
}
