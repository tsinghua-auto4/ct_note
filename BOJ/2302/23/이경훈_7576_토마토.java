package _230222;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main_7576_G5_토마토_이경훈 {
	static int[][] map;
	static int M, N;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	static ArrayDeque<int[]> queue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		List<int[]> riped = new ArrayList<int[]>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int temp = Integer.parseInt(st.nextToken());
				if (temp == 1)
					riped.add(new int[] { i, j });
				map[i][j] = temp;
			}
		}
		queue = new ArrayDeque<>();
		for (int i = 0; i < riped.size(); i++) {
			queue.add(new int[] { riped.get(i)[0], riped.get(i)[1] });
		}

		int ans = bfs(0);

		if (!check()) {
			System.out.println(-1);
		} else {
			System.out.println(ans);
		}

	}

	private static boolean check() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 0) {
					return false;
				}
			}
		}
		return true;
	}

	private static int bfs(int cnt) {
		while (!queue.isEmpty()) {
			int q = queue.size();
			while (q-- > 0) {
				int[] temp = queue.pop();
				int x = temp[0];
				int y = temp[1];
				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (-1 < nx && nx < N && -1 < ny && ny < M) {
						if (map[nx][ny] == 0) {
							map[nx][ny] = 1;
							queue.add(new int[] { nx, ny });
						}
					}
				}
			}
			cnt++;
		}
		return cnt - 1;
	}
}