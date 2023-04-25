package com.ssafy._230405;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main_15961_G4_회전초밥_이경훈 {
	static int N, d, k, c, ans;
	static int[] chobab, visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

		chobab = new int[N];

		for (int i = 0; i < N; i++) {
			chobab[i] = Integer.parseInt(br.readLine());
		}

		visited = new int[d + 1];

		windowSlide();
		System.out.println(ans);

	}

	private static void windowSlide() {
		int total = 0;
		for (int i = 0; i < k; i++) {
			if (visited[chobab[i]] == 0)
				total++;
			visited[chobab[i]]++;
		}
		ans = total;

		for (int i = 1; i < N; i++) {
			if (total >= ans) {
				if (visited[c] == 0)
					ans = total + 1;
				else
					ans = total;
			}
			visited[chobab[i - 1]]--;
			if (visited[chobab[i - 1]] == 0)
				total--;
			if (visited[chobab[(i - 1 + k) % N]] == 0)
				total++;
			visited[chobab[(i - 1 + k) % N]]++;

		}
	}
}
