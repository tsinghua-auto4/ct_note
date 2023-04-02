import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int INF = (int) 1e9;
	static int N;
	static int[][] graph, dist;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = 1;
		while (true) {

			N = sc.nextInt();
			if (N == 0)
				break;
			graph = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					graph[i][j] = sc.nextInt();
				}
			}
			dist = new int[N][N];
			for (int[] i : dist) {
				Arrays.fill(i, INF);
			}
			dist[0][0] = graph[0][0];
			bfs();
			System.out.printf("Problem %d: %d", tc++, dist[N - 1][N - 1]);
			System.out.println();
		}
	}

	private static void bfs() {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.offer(new int[] { 0, 0 });
		while (!q.isEmpty()) {

			int[] temp = q.poll();
			int x = temp[0];
			int y = temp[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (!inside(nx, ny))
					continue;
//				if (dist[nx][ny] <= dist[x][y] + graph[nx][ny])
//					continue;
//				dist[nx][ny] = dist[x][y] + graph[nx][ny];

				for (int j = 0; j < 4; j++) {
					int nnx = nx + dx[j];
					int nny = ny + dy[j];
					if (!inside(nnx, nny))
						continue;
					if (dist[nnx][nny] + graph[nx][ny] < dist[nx][ny]) {
						dist[nx][ny] = dist[nnx][nny] + graph[nx][ny];
						q.offer(new int[] { nx, ny });
					}
				}

			}
		}
	}

	private static boolean inside(int x, int y) {
		if (-1 < x && x < N && -1 < y && y < N)
			return true;
		return false;
	}
}
