package com.ssafy._230328;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1149_S1_RGB거리_이경훈 {

	final static int RED = 0;
	final static int GREEN = 1;
	final static int BLUE = 2;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int N = Integer.parseInt(br.readLine());

		int[][] Cost = new int[N + 1][3];

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			Cost[i][RED] = Integer.parseInt(st.nextToken());
			Cost[i][GREEN] = Integer.parseInt(st.nextToken());
			Cost[i][BLUE] = Integer.parseInt(st.nextToken());

		}

		for (int i = 2; i <= N; i++) {
			Cost[i][RED] += Math.min(Cost[i - 1][GREEN], Cost[i - 1][BLUE]);
			Cost[i][GREEN] += Math.min(Cost[i - 1][RED], Cost[i - 1][BLUE]);
			Cost[i][BLUE] += Math.min(Cost[i - 1][RED], Cost[i - 1][GREEN]);
		}

		System.out.println(Math.min(Math.min(Cost[N][RED], Cost[N][GREEN]), Cost[N][BLUE]));
	}

}