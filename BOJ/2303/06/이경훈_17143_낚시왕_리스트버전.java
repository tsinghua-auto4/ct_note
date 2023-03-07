package _230307;
// 리스트 이용
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

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

	static Shark[][] map;
	static List<Shark> sharkList;
	static List<Shark> caughtList;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, 1, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		M = sc.nextInt();
		sharkList = new ArrayList<>();
		caughtList = new ArrayList<>();
		int r, c, s, d, z;
		Shark shark;
		map = new Shark[R + 1][C + 1];
		for (int i = 0; i < M; i++) {
			r = sc.nextInt();
			c = sc.nextInt();
			s = sc.nextInt();
			d = sc.nextInt();
			z = sc.nextInt();
			shark = new Shark(r, c, s, d, z);
			sharkList.add(shark);
			map[r][c] = shark;
		}
		int col = 0;

//		for (int i = 1; i <= R; i++) {
//			System.out.println(Arrays.toString(map[i]));
//		}

		while (col++ < C) { // C초 동안 시행
			catchShark(col); // cnt열의 가장 가까운 상어를 잡음
			sharkMove(); // 상어 이동
			killShark();

		}
		int ans = 0;
		for (Shark sk : caughtList) {
			ans += sk.z;
		}
		System.out.println(ans);
	}

	private static void killShark() {
		map = new Shark[R + 1][C + 1];
		int size = sharkList.size();
		for (int i = size - 1; i >= 0; i--) {
			Shark s = sharkList.get(i);
			if (map[s.r][s.c] == null) {
				map[s.r][s.c] = s;
			} else {
				if (s.z > map[s.r][s.c].z) {
					sharkList.remove(map[s.r][s.c]);
					map[s.r][s.c] = s;
				} else {
					sharkList.remove(s);
				}
			}
		}
	}

	private static void sharkMove() {
		for (Shark shark : sharkList) {

			int nr = shark.r;
			int nc = shark.c;
			int s = shark.s;
			int d = shark.d;

			if (d == 1) {
				s = s % ((2 * R) - 2);
				for (int j = 0; j < s; j++) {
					if (nr == 1)
						d = 2;
					else if (nr == R)
						d = 1;
					nr += dr[d - 1];
				}
				shark.r = nr;
				shark.d = d;

			} else if (d == 2) {
				s = s % ((2 * R) - 2);
				for (int j = 0; j < s; j++) {
					if (nr == R)
						d = 1;
					else if (nr == 1)
						d = 2;
					nr += dr[d - 1];
				}
				shark.r = nr;
				shark.d = d;

			} else if (d == 3) {
				s = s % ((2 * C) - 2);
				for (int j = 0; j < s; j++) {
					if (nc == C)
						d = 4;
					else if (nc == 1)
						d = 3;
					nc += dc[d - 1];
				}
				shark.c = nc;
				shark.d = d;
			} else if (d == 4) {
				s = s % ((2 * C) - 2);
				for (int j = 0; j < s; j++) {
					if (nc == 1)
						d = 3;
					else if (nc == C)
						d = 4;
					nc += dc[d - 1];
				}
				shark.c = nc;
				shark.d = d;
			}

		}
	}

	private static void catchShark(int col) {
		for (int r = 1; r <= R; r++) {
			if (map[r][col] != null) {
				caughtList.add(map[r][col]);
				sharkList.remove(map[r][col]);
				break;
			}
		}
	}
}
