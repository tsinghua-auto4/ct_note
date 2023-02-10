package com.ssafy;
import java.util.Scanner;

public class Solution_1954_D2_달팽이숫자_이경훈 {
	static int N;
	static int snailNum;
	static int[][] snailArr;
	static boolean[][] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int tc = 1; tc <= N; tc++) {
			snailNum = sc.nextInt();
			snailArr = new int[snailNum][snailNum];
			visited = new boolean[snailNum][snailNum];

			makeSnail(0, 0, 1, 'r');
			System.out.println("#" + tc);
			for (int i = 0; i < snailNum; i++) {
				for (int j = 0; j < snailNum; j++) {
					System.out.print(snailArr[i][j] + " ");
				}
				System.out.println();
			}

		}
	}

	static void makeSnail(int r, int c, int cnt, char d) {
		if (cnt == snailNum * snailNum + 1)
			return;
		snailArr[r][c] = cnt;
		visited[r][c] = true;
		if (d == 'r') {
			if (c + 1 < snailNum && !visited[r][c + 1])
				makeSnail(r, c + 1, cnt + 1, 'r');
			else {
				makeSnail(r + 1, c, cnt + 1, 'd');
			}
		} else if (d == 'd') {
			if (r + 1 < snailNum && !visited[r + 1][c])
				makeSnail(r + 1, c, cnt + 1, 'd');
			else {
				makeSnail(r, c - 1, cnt + 1, 'l');
			}
		} else if (d == 'l') {
			if (c - 1 > -1 && !visited[r][c - 1])
				makeSnail(r, c - 1, cnt + 1, 'l');
			else {
				makeSnail(r - 1, c, cnt + 1, 'u');
			}
		} else {
			if (r - 1 > -1 && !visited[r - 1][c])
				makeSnail(r - 1, c, cnt + 1, 'u');
			else {
				makeSnail(r, c + 1, cnt + 1, 'r');
			}
		}
	}
}