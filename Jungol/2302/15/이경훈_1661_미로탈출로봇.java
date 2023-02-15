package _230215;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class 이경훈_1661_미로탈출로봇 {

	static class Node {
		int x;
		int y;

		public Node() {
		}

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}

	}

	static int X;
	static int Y;
	static int[][] map;
	static int cnt = 10001;
	static int[] dx = { -1, 1, 0, 0 }; // 상하좌우
	static int[] dy = { 0, 0, -1, 1 };
	static Node end;
	static boolean visited[][];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		Y = Integer.parseInt(st.nextToken()); // 7
		X = Integer.parseInt(st.nextToken()); // 8

		// 데이터 입력
		st = new StringTokenizer(br.readLine());
		int temp1 = Integer.parseInt(st.nextToken()) - 1;
		int temp2 = Integer.parseInt(st.nextToken()) - 1;
		int temp3 = Integer.parseInt(st.nextToken()) - 1;
		int temp4 = Integer.parseInt(st.nextToken()) - 1;
		Node start = new Node(temp2, temp1);
		end = new Node(temp4, temp3);
		map = new int[X][Y];
		for (int i = 0; i < X; i++) {
			String str = br.readLine();
			for (int j = 0; j < Y; j++) {
				map[i][j] = str.charAt(j) - '0';
			}
		}

//		bfs(start);
//		System.out.println(cnt);
		visited = new boolean[X][Y];
		dfs(start);
		System.out.println(map[end.x][end.y]);
	}

	static void bfs(Node node) {
		Queue<Node> q = new ArrayDeque<>();
		q.offer(node);
		map[node.x][node.y] = 1;

		while (!q.isEmpty()) {
			int size = q.size();
			while (--size >= 0) {
				node = q.poll();
				if (node.x == end.x && node.y == end.y) {
					return;
				}
				for (int i = 0; i < 4; i++) {
					int nx = node.x + dx[i];
					int ny = node.y + dy[i];

					if (-1 < nx && nx < X && -1 < ny && ny < Y) {
						if (map[nx][ny] == 0) {
							map[nx][ny] = 1;
							q.offer(new Node(nx, ny));
						}
					}
				}
			}
			cnt++;
		}
	}

	static void dfs(Node node) {
		if (node.x == end.x && node.y == end.y) {
			return;
		}
		int dist = map[node.x][node.y];
		for (int i = 0; i < 4; i++) {
			int nx = node.x + dx[i];
			int ny = node.y + dy[i];

			if (-1 < nx && nx < X && -1 < ny && ny < Y) {
				if (map[nx][ny] == 0 || map[nx][ny] > dist + 1) {
					map[nx][ny] = dist + 1;
					dfs(new Node(nx, ny));

				}
			}
		}
	}
}
