package com.ssafy._230301;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3289_D4_서로소집합_이경훈 {
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

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(tc).append(" ");

			makeset();

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				if (st.nextToken().equals("0"))
					union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
				else {
					if (findset(Integer.parseInt(st.nextToken())) == findset(Integer.parseInt(st.nextToken()))) {
						sb.append(1);
					} else {
						sb.append(0);
					}
				}
			}
			System.out.println(sb.toString());
		}
	}
}
