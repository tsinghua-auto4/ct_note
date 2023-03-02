package com.ssafy._230301;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Solution_7465_D4_창용마을무리의개수_이경훈 {
	static int N;
	static int[] parents;

	static void makeset() {
		parents = new int[N + 1];
		for (int i = 0; i <= N; i++) {
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
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			int M = sc.nextInt();

			makeset();

			for (int i = 0; i < M; i++) {
				union(sc.nextInt(), sc.nextInt());
			}

			for (int i = 1; i <= N; i++) {
				findset(i);
			}

			HashSet<Integer> result = new HashSet<>();
			for (int i = 1; i <= N; i++) {
				result.add(parents[i]);
			}

			System.out.printf("#%d %d", tc, result.size());
			System.out.println();
		}
	}

}
