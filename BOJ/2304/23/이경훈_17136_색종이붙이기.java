import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static final int N = 10;
	static final int EMPTY = 0;
	static final int COVER = 1;
	static int[][] map;
	static int[] limit;
	static int ans = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		map = new int[N][N];
		limit = new int[6];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		dfs(0, 0, 0);
		if (ans == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(ans);
		}

	}

	private static void dfs(int r, int c, int cnt) { // r,c 좌표 cnt 사용한 종이 개수

		if (r == N && c == 0) {

			if (ans > cnt)
				ans = cnt;
			return;
		}

		int nr, nc;

		if (c == 9) {
			nr = r + 1;
			nc = 0;
		} else {
			nr = r;
			nc = c + 1;
		}
		if (map[r][c] == EMPTY) {
			dfs(nr, nc, cnt);
		} else { // 종이로 덮어야 하는 칸
			// 다음 값으로 진행
			for (int i = 5; i > 0; i--) {
				if (check(r, c, i) && limit[i] < 5) {
					limit[i]++;
					cover(r, c, i);
					dfs(nr, nc, cnt + 1);
					init(r, c, i);
					limit[i]--;
				}
			}
		}
	}

	private static void init(int r, int c, int size) {
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				map[i][j] = COVER;
			}
		}
	}

	private static void cover(int r, int c, int size) {
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				map[i][j] = EMPTY;
			}
		}
	}

	private static boolean check(int r, int c, int size) {
		if (r + size > N || c + size > N)
			return false;
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (map[i][j] == EMPTY)
					return false;
			}
		}
		return true;
	}
}