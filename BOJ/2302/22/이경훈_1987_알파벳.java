package _230221;

import java.util.Scanner;

public class Main_1987_G4_알파벳_이경훈 {
	static int R, C, cnt = -1;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static boolean[] alphabet;
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		alphabet = new boolean[26];
		map = new int[R][C];
		for (int i = 0; i < R; i++) {
			String temp = sc.next();
			for (int j = 0; j < C; j++) {
				map[i][j] = temp.charAt(j) - 'A';
			}
		}
		backtrack(0, 0, 0);
		System.out.println(cnt);
	}

	private static void backtrack(int x, int y, int _cnt) {

		if (alphabet[map[x][y]] == true) {
			cnt = Math.max(cnt, _cnt);
			return;
		}

		alphabet[map[x][y]] = true;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (-1 < nx && nx < R && -1 < ny && ny < C) {
				backtrack(nx, ny, _cnt + 1);
			}
		}
		alphabet[map[x][y]] = false;
	}
}
package _230221;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_3109_G2_빵집_이경훈 {
	static int R, C;
	static int[][] map;
	static int[] dx = { -1, 0, 1 };
	static int[] dy = { 1, 1, 1 };
	static boolean[][] visited;
	static int totalCnt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new int[R][C];
		for (int i = 0; i < R; i++) {
			String temp = br.readLine();
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == '.')
					map[i][j] = 0;
				else
					map[i][j] = 1;
			}
		}
		visited = new boolean[R][C];

		for (int i = 0; i < R; i++) {
			backtrack(0, i, 0);
		}
		System.out.println(totalCnt);
	}

	private static void backtrack(int cnt, int x, int y) {
		visited[x][y] = true;
		if (cnt == C - 1) {
			totalCnt++;
			return;
		}
		int temp = totalCnt;

		for (int i = 0; i < 3; i++) {
			if (temp != totalCnt)
				break;
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (-1 < nx && nx < R && -1 < ny && ny < C) {
				if (map[nx][ny] != 1 && !visited[nx][ny]) {
					backtrack(cnt + 1, nx, ny);
				}
			}
		}
	}
}
