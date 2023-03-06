package com.ssafy._230305;

import java.util.ArrayList;
import java.util.Scanner;

public class Solution_1767_프로세서연결하기_이경훈 {
	static class Core {
		int x, y;

		public Core(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}

	static ArrayList<Core> coreList;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int N;
	static int[][] map;
	static int curLines = Integer.MAX_VALUE;
	static ArrayList<Core> selectedList = new ArrayList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			map = new int[N][N];

			// 주변이 아닌 코어들만 위치 받아서 리스트에 넣어주기
			coreList = new ArrayList<>();

			// 입력
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
					if (map[i][j] == 1 && i != 0 && i != N - 1 && j != 0 && j != N - 1) {
						coreList.add(new Core(i, j));
					}
				}
			}
			for (int i = coreList.size(); i >= 0; i--) {
				curLines = Integer.MAX_VALUE;
				combi(0, 0, i);
				if (curLines != Integer.MAX_VALUE) {
					break;
				}
			}
			System.out.println("#" + tc + " " + curLines);

		}
	}

	private static void combi(int startIdx, int depth, int targetDepth) {
		if (depth == targetDepth) {
			dfs(0, 0);
			return;
		}
		for (int i = startIdx; i < coreList.size(); i++) {
			selectedList.add(coreList.get(i));
			combi(i + 1, depth + 1, targetDepth);
			selectedList.remove(selectedList.size() - 1);
		}
	}

	private static void dfs(int depth, int lines) {
		if (depth == selectedList.size()) {
			curLines = Math.min(curLines, lines);
			return;
		}

		Core core = selectedList.get(depth);
		for (int i = 0; i < 4; i++) {
			if (canConnect(core.x, core.y, i)) {
				lines += connect(core.x, core.y, i, 0);
				dfs(depth + 1, lines);
				lines -= recover(core.x, core.y, i, 0);
			}
		}
	}

	private static int recover(int curRow, int curCol, int dir, int depth) {
		if (curRow == 0 || curCol == 0 || curRow == N - 1 || curCol == N - 1) {
			return depth;
		}
		int newRow = curRow + dx[dir];
		int newCol = curCol + dy[dir];
		map[newRow][newCol] = 0;
		return recover(newRow, newCol, dir, depth + 1);
	}

	private static int connect(int curRow, int curCol, int dir, int depth) {
		if (curRow == 0 || curCol == 0 || curRow == N - 1 || curCol == N - 1) {
			return depth;
		}
		int newRow = curRow + dx[dir];
		int newCol = curCol + dy[dir];
		map[newRow][newCol] = 2;
		return connect(newRow, newCol, dir, depth + 1);
	}

	private static boolean canConnect(int startRow, int startCol, int dir) {
		if (startRow == 0 || startCol == 0 || startRow == N - 1 || startCol == N - 1) {
			return true;
		}
		int newRow = startRow + dx[dir];
		int newCol = startCol + dy[dir];
		if (map[newRow][newCol] == 0) {
			return canConnect(newRow, newCol, dir);
		}
		return false;
	}

}
