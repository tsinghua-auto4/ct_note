import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	static class Point {
		int x;
		int y;
		int horse;

		public Point() {
		}

		public Point(int x, int y, int horse) {
			this.x = x;
			this.y = y;
			this.horse = horse;
		}
	}

	static int[] ho_dx = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] ho_dy = { 1, 2, 2, 1, -1, -2, -2, -1 };
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	static int K, W, H;
	static int[][][] visited;
	static int[][] graph;

	static int bfs() {
		ArrayDeque<Point> q = new ArrayDeque<>();
		q.offer(new Point(0, 0, 0));
		visited[0][0][0] = 1;

		while (!q.isEmpty()) {
			Point temp = q.poll();
			int x = temp.x, y = temp.y, horse = temp.horse;

			if (x == H - 1 && y == W - 1) {
				return visited[x][y][horse] - 1;
			}

			for (int i = 0; i < 4; i++) { // 일반 움직임
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (outside(nx, ny))
					continue;

				if (graph[nx][ny] == 1)
					continue;

				if (visited[nx][ny][horse] != 0)
					continue;

				visited[nx][ny][horse] = visited[x][y][horse] + 1;
				q.offer(new Point(nx, ny, horse));
			}

			if (horse < K) { // 말 점프 다 안 씀
				for (int i = 0; i < 8; i++) {
					int nx = x + ho_dx[i];
					int ny = y + ho_dy[i];

					if (outside(nx, ny))
						continue;

					if (graph[nx][ny] == 1)
						continue;

					if (visited[nx][ny][horse + 1] != 0)
						continue;

					visited[nx][ny][horse + 1] = visited[x][y][horse] + 1;
					q.offer(new Point(nx, ny, horse + 1));
				}
			}
		}
		return -1;
	}

	private static boolean outside(int nx, int ny) {
		if (nx < 0 || nx >= H || ny < 0 || ny >= W)
			return true;
		return false;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());

		graph = new int[H][W];
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		visited = new int[H][W][K + 1];

		System.out.println(bfs());

	}

}