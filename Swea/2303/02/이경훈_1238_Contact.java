package com.ssafy._230301;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Scanner;

public class Solution_1238_D4_Contact_이경훈 {
	static class Node {
		int from, to;

		public Node(int from, int to) {
			super();
			this.from = from;
			this.to = to;
		}

	}

	static int[] parents;

	static void makeset() {
		parents = new int[101];
		for (int i = 0; i <= 100; i++) {
			parents[i] = i;
		}
	}

	static int findset(int a) {
		if (a == parents[a])
			return a;
		return parents[a] = findset(parents[a]);
	}

	static boolean union(int a, int b) {
		int aRoot = findset(a);
		int bRoot = findset(b);

		if (aRoot == bRoot)
			return false;

		parents[bRoot] = aRoot;
		return true;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int tc = 1; tc <= 10; tc++) {
			int n = sc.nextInt();
			int rootNodeNum = sc.nextInt();
			ArrayList<Integer>[] adj = new ArrayList[101];
			for (int i = 0; i <= 100; i++) {
				adj[i] = new ArrayList<>();
			}
			boolean[] visited = new boolean[101];

			for (int i = 0; i < n / 2; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				adj[a].add(b);
			}

			Queue<Integer> q = new ArrayDeque<>();

			q.addAll(adj[rootNodeNum]);
			visited[rootNodeNum] = true;
			int result = 0;
			int tmp = 0;
			while (!q.isEmpty()) {
				int qSize = q.size();
				tmp = result;
				result = 0;
				while (qSize-- != 0) {
					int temp = q.poll();
					if (visited[temp])
						continue;
					q.addAll(adj[temp]);
					visited[temp] = true;
					result = Math.max(result, temp);
				}
			}
			if (result == 0 && tmp != 0) {
				System.out.printf("#%d %d", tc, tmp);
				System.out.println();
			} else {
				System.out.printf("#%d %d", tc, result);
				System.out.println();
			}
		}
	}
}
