package _230405;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_4014_모의_활주로건설_이경훈 {
	static int N, X, rowCnt, colCnt;
	static boolean[] visited;
	static int[][] map;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
//			System.out.println();
//			System.out.println(tc + "번째 테케 : ");
			rowCnt = 0;
			for (int i = 0; i < N; i++) {
				visited = new boolean[N + 1];
				checkRow(i, 0, 0);
			}

//			System.out.println("rowCnt :" + rowCnt);
			colCnt = 0;
			for (int i = 0; i < N; i++) {
				visited = new boolean[N + 1];
				checkCol(0, i, 0);
			}

//			System.out.println("colCnt :" + colCnt);
			System.out.println("#" + tc + " " + (rowCnt + colCnt));
		}

	}

	private static void checkRow(int r, int c, int cnt) {
		if (cnt == N - 1) {
//			System.out.println("행이 " + r + "일때 활주로 가능");
			rowCnt++;
			return;
		}

		int nc = c + 1;

		if (!inside(r, nc))
			return;

		if (map[r][nc] == map[r][c])
			checkRow(r, nc, cnt + 1);

		// 갈곳이 현재보다 1 높을 때
		else if (map[r][nc] == map[r][c] + 1) {
			// 현재의 전 높이를 구해서 같다면 경사로 설치 가능
			if (inside(r, c - (X - 1)) && rowDownEqualcheck(r, c)) {
				for (int i = c - (X - 1); i <= c; i++) {
					visited[i] = true;
				}
				checkRow(r, nc, cnt + 1);
			}
		}

		// 갈곳이 현재보다 1 낮을 때
		else if (map[r][nc] == map[r][c] - 1) {
			// 갈곳과 갈곳 다음의 높이를 구해서 같다면 경사로 설치 가능
			if (inside(r, c + X) && rowUpEqualcheck(r, c)) {
				for (int i = c + 1; i <= c + X; i++) {
					visited[i] = true;
				}
				checkRow(r, nc, cnt + 1);
			}

		}
	}

	private static void checkCol(int r, int c, int cnt) {
		if (cnt == N - 1) {
//			System.out.println("열이 " + c + "일때 활주로 가능");
			colCnt++;
			return;
		}

		int nr = r + 1;

		if (!inside(nr, c))
			return;

		if (map[nr][c] == map[r][c])
			checkCol(nr, c, cnt + 1);

		// 갈곳이 현재보다 1 높을 때
		else if (map[nr][c] == map[r][c] + 1) {
			// 현재의 전 높이를 구해서 같다면 경사로 설치 가능
			if (inside(r - (X - 1), c) && colDownEqualcheck(r, c)) {
				for (int i = r - (X - 1); i <= r; i++) {
					visited[i] = true;
				}
				checkCol(nr, c, cnt + 1);
			}
		}

		// 갈곳이 현재보다 1 낮을 때
		else if (map[nr][c] == map[r][c] - 1) {
			// 갈곳과 갈곳 다음의 높이를 구해서 같다면 경사로 설치 가능
			if (inside(r + X, c) && colUpEqualcheck(r, c)) {
				for (int i = r + 1; i <= r + X; i++) {
					visited[i] = true;
				}
				checkCol(nr, c, cnt + 1);
			}
		}
	}

	private static boolean rowDownEqualcheck(int r, int c) {
		int temp = map[r][c];
		for (int i = 1; i < X; i++) { // 현재 값이랑 전 값들을 X의 길이만큼 비교함
			if (map[r][c - i] != temp)
				return false;
		}
		for (int i = c - (X - 1); i <= c; i++) {
			if (visited[i])
				return false;
		}
		return true;
	}

	private static boolean rowUpEqualcheck(int r, int c) {
		int temp = map[r][c + 1];
		for (int i = 1; i < X; i++) { // 현재 값이랑 전 값들을 X의 길이만큼 비교함
			if (map[r][c + 1 + i] != temp)
				return false;
		}
		for (int i = c + 1; i <= c + X; i++) {
			if (visited[i])
				return false;
		}
		return true;
	}

	private static boolean colDownEqualcheck(int r, int c) {
		int temp = map[r][c];
		for (int i = 1; i < X; i++) { // 현재 값이랑 전 값들을 X의 길이만큼 비교함
			if (map[r - i][c] != temp)
				return false;
		}
		for (int i = r - (X - 1); i <= r; i++) {
			if (visited[i])
				return false;
		}
		return true;
	}

	private static boolean colUpEqualcheck(int r, int c) {
		int temp = map[r + 1][c];
		for (int i = 1; i < X; i++) { // 현재 값이랑 전 값들을 X의 길이만큼 비교함
			if (map[r + 1 + i][c] != temp)
				return false;
		}
		for (int i = r + 1; i <= r + X; i++) {
			if (visited[i])
				return false;
		}
		return true;
	}

	private static boolean inside(int r, int c) {
		return -1 < r && r < N && -1 < c && c < N;
	}
}
