import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static boolean[][] visited;
	static int N;
	static char map_rgb[][];
	static char map_rb[][];
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map_rgb = new char[N][N];
		map_rb = new char[N][N];
		sc.nextLine();
		for (int i = 0; i < N; i++) {
			String temp = sc.nextLine();
			for (int j = 0; j < N; j++) {
				map_rgb[i][j] = temp.charAt(j);
				map_rb[i][j] = temp.charAt(j);
				if (temp.charAt(j) == 'G') {
					map_rb[i][j] = 'R';
				}
			}
		}

		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				bfs(i, j, map_rgb);
			}
		}

		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				bfs(i, j, map_rb);
			}
		}
		System.out.println(count(map_rgb) + " " + count(map_rb));
	}

	private static int count(char[][] map) {
		int cnt = 0;
		for (char[] cs : map) {
			for (char c : cs) {
				if (c != '\0') {
					cnt++;
				}
			}
		}
		return cnt;
	}

	private static void bfs(int x, int y, char[][] _map) {
		if (_map[x][y] == '\0')
			return;
		char LETTER = _map[x][y];
		Queue<int[]> q = new ArrayDeque<int[]>();
		q.offer(new int[] { x, y });
		visited[x][y] = true;
		while (!q.isEmpty()) {
			int[] temp = q.poll();
			int sx = temp[0];
			int sy = temp[1];

			for (int i = 0; i < 4; i++) {
				int nx = sx + dx[i];
				int ny = sy + dy[i];

				if (-1 < nx && nx < N && -1 < ny && ny < N) {
					if (!visited[nx][ny] && (_map[nx][ny] == LETTER)) {
						q.offer(new int[] { nx, ny });
						visited[nx][ny] = true;
						_map[nx][ny] = '\0';
					}
				}
			}
		}
	}
}