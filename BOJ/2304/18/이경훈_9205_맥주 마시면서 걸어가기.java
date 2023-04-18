package _230405;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class _9205 {
	static class Pos {
		int x, y;

		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static List<Pos> pos_list;
	static int[][] adj;
	static final int INF = (int) 1e7;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			// 테케 시작
			pos_list = new ArrayList<>();

			int n = Integer.parseInt(br.readLine()); // 편의점 개수 n
			adj = new int[n + 2][n + 2];

			for (int i = 0; i < n + 2; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				pos_list.add(new Pos(x, y));
			}

			for (int i = 0; i < n + 2; i++) {
				for (int j = 0; j < n + 2; j++) {
					int x = Math.abs(pos_list.get(i).x - pos_list.get(j).x);
					int y = Math.abs(pos_list.get(i).y - pos_list.get(j).y);
					if (x + y <= 1000)
						adj[i][j] = x + y;
					else {
						adj[i][j] = INF;
					}
				}
			}

			for (int k = 0; k < n + 2; k++) {
				for (int i = 0; i < n + 2; i++) {
					for (int j = 0; j < n + 2; j++) {
						adj[i][j] = Math.min(adj[i][j], adj[i][k] + adj[k][j]);
					}
				}
			}
//			System.out.println(Arrays.deepToString(adj));

			if (adj[0][n + 1] == INF) {
				System.out.println("sad");
			} else {
				System.out.println("happy");
			}

		}
	}
}
