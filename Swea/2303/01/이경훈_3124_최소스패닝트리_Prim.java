package _230228;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution_3124_D4_최소스패닝트리_이경훈_Prim {
	static class Edge implements Comparable<Edge> {
		int from;
		int to;
		int weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());

			ArrayList<Edge>[] adj = new ArrayList[N];
			for (int i = 0; i < N; i++) {
				adj[i] = new ArrayList<>();
			}
			boolean[] visited = new boolean[N];

			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken()) - 1;
				int b = Integer.parseInt(st.nextToken()) - 1;
				int c = Integer.parseInt(st.nextToken());

				adj[a].add(new Edge(a, b, c));
				adj[b].add(new Edge(b, a, c));
			}

			PriorityQueue<Edge> queue = new PriorityQueue<>();

			int cnt = 1;
			long result = 0;

			queue.addAll(adj[0]);
			visited[0] = true;

			while (cnt != N) {
				Edge min = queue.poll();
				if (visited[min.to])
					continue;
				queue.addAll(adj[min.to]);
				visited[min.to] = true;
				result += min.weight;
				cnt++;
			}
			System.out.printf("#%d %d%n", tc, result);
		}

	}
}
