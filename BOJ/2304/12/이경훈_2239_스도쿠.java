package com.ssafy._230330;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main_2239_G4_스도쿠_이경훈 {
	static int[][] graph;
	static ArrayList<int[]> list;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		graph = new int[9][9];
		list = new ArrayList<>();
		for (int i = 0; i < 9; i++) {
			String temp = br.readLine();
			for (int j = 0; j < 9; j++) {
				graph[i][j] = temp.charAt(j) - '0';
				if (graph[i][j] == 0) {
					list.add(new int[] { i, j });
				}
			}
		}
		dfs(0);
	}

	private static boolean dfs(int cnt) {

		if (cnt == list.size()) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					System.out.print(graph[i][j]);
				}
				System.out.println();
			}
			return true;
		}

		int point[] = list.get(cnt);

		for (int n = 1; n <= 9; n++) {

			if (!safe(n, point[0], point[1]))
				continue;
			graph[point[0]][point[1]] = n;

			if (dfs(cnt + 1))
				return true;
			graph[point[0]][point[1]] = 0;
		}
		return false;
	}

	private static boolean safe(int num, int row, int col) {

		for (int i = 0; i < 9; i++) {
			if (graph[row][i] == num) {
				return false;
			}
			if (graph[i][col] == num) {
				return false;
			}
		}

		int sR = row / 3 * 3;
		int sC = col / 3 * 3;
		for (int i = sR, rowSize = sR + 3; i < rowSize; i++) {
			for (int j = sC, colSize = sC + 3; j < colSize; j++) {
				if (graph[i][j] == num) {
					return false;
				}
			}
		}
		return true;
	}
}
