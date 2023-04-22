package com.ssafy._230329;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_10971_S2_외판원순회2_이경훈 {
	static int N;
	static int[][] graph;
	static boolean[] visited;
	static int MIN = Integer.MAX_VALUE;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		graph = new int[N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < N; i++) {
			visited = new boolean[N];
			visited[i] = true;
			backtracking(0, i, 0, i);
		}
		System.out.println(MIN);
	}

	private static void backtracking(int cnt, int r, int sum, int start) {
		if (cnt == N - 1) {
			if (graph[r][start] != 0)
				if (MIN > sum + graph[r][start]) {
					MIN = sum + graph[r][start];
				}
			return;
		}

		for (int i = 0; i < N; i++) {
			if (graph[r][i] != 0 && !visited[i]) {
				visited[i] = true;
				backtracking(cnt + 1, i, sum + graph[r][i], start);
				visited[i] = false;
			}
		}
	}
}
