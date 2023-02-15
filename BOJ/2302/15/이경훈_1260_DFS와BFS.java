package _230215;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class 이경훈_1260_DFS와BFS {
	static boolean[][] graph;
	static boolean[] visited;
	static int N;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		graph = new boolean[N + 1][N + 1];
		int v = Integer.parseInt(st.nextToken());
		int n1 = 0;
		int n2 = 0;
		// 인접행렬에 입력을 받음
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			n1 = Integer.parseInt(st.nextToken());
			n2 = Integer.parseInt(st.nextToken());
			graph[n1][n2] = true;
			graph[n2][n1] = true;
		}
		// 방문배열 초기화
		visited = new boolean[N + 1];
		dfs(v);
		sb.append('\n');
		// 방문배열 초기화
		visited = new boolean[N + 1];
		bfs(v);
		System.out.println(sb.toString());
	}

	static void dfs(int v) {
		visited[v] = true;
		sb.append(v).append(" ");
		for (int ad = 1; ad <= N; ad++) {
			if (graph[v][ad] && !visited[ad]) {
				dfs(ad);
			}
		}

	}

	static void bfs(int v) {
		ArrayDeque<Integer> q = new ArrayDeque<>();
		q.offer(v);
		visited[v] = true;
		while (!q.isEmpty()) {
			v = q.poll();
			sb.append(v).append(" ");
			for (int ad = 1; ad <= N; ad++) {
				if (graph[v][ad] && !visited[ad]) {
					q.offer(ad);
					visited[ad] = true;
				}
			}
		}
	}

}
