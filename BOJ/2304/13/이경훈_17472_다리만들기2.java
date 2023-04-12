package com.ssafy._230404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

import com.sun.org.apache.bcel.internal.classfile.Node;

public class Main_17472_G1_다리만들기2_이경훈 {
	static class Pos {
		int r, c;

		public Pos(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}

	}

	static class Node implements Comparable<Node> {
		int to;
		int from;
		int dist;

		public Node(int to, int from, int dist) {
			this.to = to;
			this.from = from;
			this.dist = dist;
		}

		@Override
		public String toString() {
			return to + " " + from + " " + dist;
		}

		@Override
		public int compareTo(Node o) {
			return this.dist - o.dist;
		}

	}

	static final int INF = Integer.MAX_VALUE;
	static int N, M;
	static int[][] map;
	static int islandCnt;
	static int visited[][];
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static int[] parents;
	static PriorityQueue<Node> pq;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visited = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				bfs(i, j);
			}
		}

		pq = new PriorityQueue<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				makeBridge(i, j, visited[i][j]);
			}
		}
		makeSet();
		int ans = useKruskal();
		System.out.println(ans == 0 ? -1 : ans);
	}

	private static int useKruskal() {
		int sum = 0;
		for (int i = 0, size = pq.size(); i < size; i++) {
			Node node = pq.poll();
			int x = node.from;
			int y = node.to;

			if (find(x) != find(y)) {
				sum += node.dist;
				union(x, y);
			}
		}
		HashSet<Integer> hs = new HashSet<>();
		for (int i = 1; i < parents.length; i++) {
			hs.add(find(i));
			if (hs.size() != 1)
				return 0;
		}
		return sum;
	}

	static void makeSet() {
		parents = new int[islandCnt + 1];
		for (int i = 1; i <= islandCnt; i++) {
			parents[i] = i;
		}
	}

	static int find(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);

		if (x == y)
			return;
		parents[y] = x;
	}

	private static void makeBridge(int x, int y, int idx) {
		if (visited[x][y] == 0)
			return;
		Deque<int[]> q = new ArrayDeque<>();

		for (int i = 0; i < 4; i++) {
			q.add(new int[] { x, y, 0 });

			while (!q.isEmpty()) {
				int[] cur = q.poll();
				int r = cur[0];
				int c = cur[1];
				int cnt = cur[2];

				int nr = r + dr[i];
				int nc = c + dc[i];

				if (!inside(nr, nc))
					continue;

				if (visited[nr][nc] != 0) {
					if (visited[nr][nc] != idx) {
						int from = idx;
						int to = visited[nr][nc];
						if (cnt > 1) {
							pq.offer(new Node(to, from, cnt));
						}
					}
					q.clear();
					break;
				}
				q.offer(new int[] { nr, nc, cnt + 1 });
			}
			q.clear();
		}
	}

	private static void bfs(int x, int y) {
		if (map[x][y] == 0 || visited[x][y] != 0)
			return;
		Deque<Pos> q = new ArrayDeque<>();
		q.add(new Pos(x, y));
		visited[x][y] = ++islandCnt;

		while (!q.isEmpty()) {
			Pos cur = q.poll();
			int r = cur.r;
			int c = cur.c;

			for (int i = 0; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];

				if (!inside(nr, nc))
					continue;

				if (map[nr][nc] == 0 || visited[nr][nc] != 0)
					continue;

				q.offer(new Pos(nr, nc));
				visited[nr][nc] = islandCnt;

			}
		}
	}

	private static boolean inside(int nr, int nc) {
		return -1 < nr && nr < N && -1 < nc && nc < M;
	}
}
