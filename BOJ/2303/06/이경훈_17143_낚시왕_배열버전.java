package _230307;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
// 배열 이용
public class Main_17143_G1_낚시왕_이경훈 {
	static int R, C, M;

	static class Shark {
		int r, c, s, d, z;
		boolean isDead;

		public Shark(int r, int c, int s, int d, int z) {
			super();
			this.r = r;
			this.c = c;
			this.s = s;
			this.d = d;
			this.z = z;
		}

		public void dead() {
			this.isDead = true;
		}

		@Override
		public String toString() {
			return "Shark [z=" + z + "]";
		}

	}

	static int[][] map;
	static Shark[] sharkArr;
	static List<Shark> caughtList;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, 1, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		M = sc.nextInt();
		sharkArr = new Shark[M];
		caughtList = new ArrayList<>();

		for (int i = 0; i < M; i++) {
			sharkArr[i] = new Shark(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
		}
		int col = 0;

		map = new int[R + 1][C + 1];
		for (int i = 0; i < M; i++) {
			map[sharkArr[i].r][sharkArr[i].c] = i + 1;
		}
//		for (int i = 1; i <= R; i++) {
//			System.out.println(Arrays.toString(map[i]));
//		}

		while (col++ < C) { // C초 동안 시행
			catchShark(col); // cnt열의 가장 가까운 상어를 잡음
			sharkMove(col); // 상어 이동
			map = new int[R + 1][C + 1];
			for (int i = 0; i < M; i++) {
				if (!sharkArr[i].isDead) {
					int r = sharkArr[i].r;
					int c = sharkArr[i].c;
					if (map[r][c] == 0) { // 상어가 안 겹침
						map[r][c] = i + 1;
					} else if (map[r][c] != 0) { // 상어가 겹침
						if (sharkArr[map[r][c] - 1].z > sharkArr[i].z) { // 기존 상어가 더 큼
							sharkArr[i].dead();
						} else { // 현재 인덱스의 상어가 더 큼
							sharkArr[map[r][c] - 1].dead();
							map[r][c] = i + 1;
						}
					}
				}
			}
		}
		int ans = 0;
		for (Shark shark : caughtList) {
			ans += shark.z;
		}
		System.out.println(ans);
	}

	private static void sharkMove(int col) {
		for (int i = 0; i < M; i++) {
			if (!sharkArr[i].isDead) {
				int nr = sharkArr[i].r;
				int nc = sharkArr[i].c;
				int s = sharkArr[i].s;
				int d = sharkArr[i].d;

				if (d == 1) {
					s = s % ((2 * R) - 2);
					for (int j = 0; j < s; j++) {
						if (nr == 1)
							d = 2;
						else if (nr == R)
							d = 1;
						nr += dr[d - 1];
					}
					sharkArr[i].r = nr;
					sharkArr[i].d = d;

				} else if (d == 2) {
					s = s % ((2 * R) - 2);
					for (int j = 0; j < s; j++) {
						if (nr == R)
							d = 1;
						else if (nr == 1)
							d = 2;
						nr += dr[d - 1];
					}
					sharkArr[i].r = nr;
					sharkArr[i].d = d;

				} else if (d == 3) {
					s = s % ((2 * C) - 2);
					for (int j = 0; j < s; j++) {
						if (nc == C)
							d = 4;
						else if (nc == 1)
							d = 3;
						nc += dc[d - 1];
					}
					sharkArr[i].c = nc;
					sharkArr[i].d = d;
				} else if (d == 4) {
					s = s % ((2 * C) - 2);
					for (int j = 0; j < s; j++) {
						if (nc == 1)
							d = 3;
						else if (nc == C)
							d = 4;
						nc += dc[d - 1];
					}
					sharkArr[i].c = nc;
					sharkArr[i].d = d;
				}
			}
		}
	}

	private static void catchShark(int col) {
		int idx = -1;
		for (int r = 1; r <= R; r++) {
			if (map[r][col] != 0) {
				idx = map[r][col];
				break;
			}
		}

		if (idx != -1) {
			caughtList.add(sharkArr[idx - 1]);
			sharkArr[idx - 1].dead();
			return;
		}
	}
}
