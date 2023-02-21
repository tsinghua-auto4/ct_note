package _230221;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1992_S1_쿼드트리_이경훈 {

	static int N;
	static int[][] map;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			String temp = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = temp.charAt(j) - '0';
			}
		}
		cut(0, 0, N);
		System.out.println(sb.toString());
	}

	private static void cut(int r, int c, int size) {
		if (isPossible(r, c, size)) {
			sb.append(map[r][c]);
			return;
		}

		int half = size / 2;

		sb.append('(');

		cut(r, c, half);
		cut(r, c + half, half);
		cut(r + half, c, half);
		cut(r + half, c + half, half);
		sb.append(')');

	}

	private static boolean isPossible(int r, int c, int size) {
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (map[i][j] != map[r][c]) {
					return false;
				}
			}
		}
		return true;
	}
}
