import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;  //////////////// 이거 깃에 올렸는지 안올렸는지 모르겠네

public class Solution_5644_모의_무선충전_이경훈 {
	static int M, A;
	static int[] moveA;
	static int[] moveB;
	static charger[] chargers;
	static List<Integer> ansA;
	static List<Integer> ansB;
	static int[] dx = { 0, -1, 0, 1, 0 };
	static int[] dy = { 0, 0, 1, 0, -1 };
	static int X1, Y1, X2, Y2;

	static class charger implements Comparable<charger> {
		int X;
		int Y;
		int C;
		int P;

		public charger(int x, int y, int c, int p) {
			X = x;
			Y = y;
			C = c;
			P = p;
		}

		@Override
		public String toString() {
			return "charger [X=" + X + ", Y=" + Y + ", C=" + C + ", P=" + P + "]";
		}

		@Override
		public int compareTo(charger o) {
			return o.P - this.P;
		}

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			int sum = 0;
			M = sc.nextInt();
			A = sc.nextInt();
			X1 = 0;
			Y1 = 0;
			X2 = 9;
			Y2 = 9;

			moveA = new int[M];
			moveB = new int[M];
			for (int i = 0; i < M; i++) {
				moveA[i] = sc.nextInt();
			}
			for (int i = 0; i < M; i++) {
				moveB[i] = sc.nextInt();
			}
			chargers = new charger[A];
			for (int i = 0; i < A; i++) {
				int y = sc.nextInt() - 1;
				int x = sc.nextInt() - 1;
				chargers[i] = new charger(x, y, sc.nextInt(), sc.nextInt());
			}

			Arrays.sort(chargers);

			ansA = new ArrayList<>();
			ansB = new ArrayList<>();
			check(); // 어느 무선 충전기 영역 안에 있는지 알려주는 함
			sum += getSum();

			for (int i = 0; i < M; i++) {
				ansA = new ArrayList<>();
				ansB = new ArrayList<>();

				X1 += dx[moveA[i]];
				Y1 += dy[moveA[i]];

				X2 += dx[moveB[i]];
				Y2 += dy[moveB[i]];

				check(); // 어느 무선 충전기 영역 안에 있는지 알려주는 함

				sum += getSum();
			}

			System.out.printf("#%d %d%n", tc, sum);
		}
	}

	private static int getSum() {
		int sum = 0;
		int temp = 0;

		if (ansA.size() == 0 && ansB.size() == 0) {
		} else if (ansA.size() == 0) {
			sum += chargers[ansB.get(0)].P;
		} else if (ansB.size() == 0) {
			sum += chargers[ansA.get(0)].P;
		} else {
			if (ansA.get(0) == ansB.get(0)) {
				if (chargers[ansA.get(0)].equals(chargers[ansB.get(0)]) {
					if (ansA.size() == 1 && ansB.size() == 1) {
						sum += chargers[ansA.get(0)].P;
					} else if (ansA.size() > 1 && ansB.size() == 1) {
						sum += chargers[ansA.get(1)].P;
						sum += chargers[ansB.get(0)].P;
					} else if (ansA.size() == 1 && ansB.size() > 1) {
						sum += chargers[ansA.get(0)].P;
						sum += chargers[ansB.get(1)].P;
					} else {
						if (ansA.get(1) >= ansB.get(1)) {
							sum += chargers[ansA.get(1)].P;
							sum += chargers[ansB.get(0)].P;
						} else {
							sum += chargers[ansA.get(0)].P;
							sum += chargers[ansB.get(1)].P;
						}
					}
				} else {
					sum += chargers[ansA.get(0)].P;
					sum += chargers[ansB.get(0)].P;
				}
			} else if (ansA.get(0) != ansB.get(0)) {
				sum += chargers[ansA.get(0)].P;
				sum += chargers[ansB.get(0)].P;
			}
		}

//			for (int i : ansA) {
//				for (int j : ansB) {
//					temp = 0;
//					if (i == j) {
//						temp = chargers[i].P;
//					} else {
//						temp += chargers[i].P;
//						temp += chargers[j].P;
//					}
//					sum = Math.max(sum, temp);
//				}
//			}
//		}

		return sum;
	}

	private static void check() {
		for (int i = 0; i < A; i++) {
			charger c = chargers[i];
			int length = Math.abs(c.X - X1) + Math.abs(c.Y - Y1);
			if (length <= c.C) {
				ansA.add(i);
			}
		}

		for (int i = 0; i < A; i++) {
			charger c = chargers[i];
			int length = Math.abs(c.X - X2) + Math.abs(c.Y - Y2);
			if (length <= c.C) {
				ansB.add(i);
			}
		}
	}
}
