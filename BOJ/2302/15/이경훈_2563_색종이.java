package com.ssafy;

import java.util.Scanner;

public class 이경훈_2563_색종이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] point = new int[n][2];
		boolean[][] square = new boolean[101][101];
		int cnt = 0;

		// 데이터 입력 받음
		for (int i = 0; i < n; i++) {
			point[i][0] = sc.nextInt();
			point[i][1] = sc.nextInt();
		}

		// 주어진 점을 기준으로 10x10칸 만큼 참으로 바꿔준다.
		for (int k = 0; k < n; k++) {
			for (int i = point[k][0]; i < point[k][0] + 10; i++) {
				for (int j = point[k][1]; j < point[k][1] + 10; j++) {
					square[i][j] = true;
				}
			}
		}

		// 참인 개수를 센다.
		for (boolean[] elements : square) {
			for (boolean element : elements) {
				if (element) {
					cnt++;
				}
			}
		}

		System.out.println(cnt);

	}
}
