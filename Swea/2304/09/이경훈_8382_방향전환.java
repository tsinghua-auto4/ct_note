package _230406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution_8382_D4_방향전환_이경훈 {

	static class Pos {
		int x, y, dir;

		public Pos(int x, int y, int dir) {
			super();
			this.x = x;
			this.y = y;
			this.dir = dir;
		}

		@Override
		public String toString() {
			return x + " " + y + " " + dir;
		}

	}

	static int min, sX, sY, eX, eY;
	static final int Garo = 0, Sero = 1;
	static int scaleX;
	static int scaleY;
	static int[] dx = { -1, 1, 0, 0 }; // 가로 세로
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			min = Integer.MAX_VALUE;
			st = new StringTokenizer(br.readLine());

			sX = Integer.parseInt(st.nextToken()) + 100;
			sY = Integer.parseInt(st.nextToken()) + 100;
			eX = Integer.parseInt(st.nextToken()) + 100;
			eY = Integer.parseInt(st.nextToken()) + 100;

			scaleX = Math.abs(sX - eX + 1);
			scaleY = Math.abs(sY - eY + 1);

			bfs();
			System.out.println("#" + tc + " " + (min - 1));

		}
	}

	private static void bfs() {

		Deque<Pos> q = new ArrayDeque<>();
		q.offer(new Pos(sX, sY, Garo));
		q.offer(new Pos(sX, sY, Sero));
		int[][][] visited = new int[201][201][2];
		visited[sX][sY][Garo] = 1;
		visited[sX][sY][Sero] = 1;
		while (!q.isEmpty()) {
			Pos pos = q.poll();
			int x = pos.x;
			int y = pos.y;
			int dir = pos.dir;

			if (x == eX && y == eY) {
				min = Math.min(min, visited[x][y][dir]);
				return;
			}

			if (dir == Garo) { // 전에 가로로 뛰었음
				for (int i = 2; i < 4; i++) { // 세로로 뛰어야 함
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (!inside(nx, ny))
						continue;

					if (visited[nx][ny][(dir + 1) % 2] != 0)
						continue;

					visited[nx][ny][(dir + 1) % 2] = visited[x][y][dir] + 1;
					q.offer(new Pos(nx, ny, (dir + 1) % 2));
				}
			}

			if (dir == Sero) { // 전에 가로로 뛰었음
				for (int i = 0; i < 2; i++) { // 세로로 뛰어야 함
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (!inside(nx, ny))
						continue;

					if (visited[nx][ny][(dir + 1) % 2] != 0)
						continue;

					visited[nx][ny][(dir + 1) % 2] = visited[x][y][dir] + 1;
					q.offer(new Pos(nx, ny, (dir + 1) % 2));
				}
			}
		}
	}

	private static boolean inside(int x, int y) {
		return -1 < x && x < 201 && -1 < y && y < 201;
	}
}
