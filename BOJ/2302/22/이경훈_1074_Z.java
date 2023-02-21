package _230220;

import java.util.Scanner;

public class Main_1074_S1_Z_이경훈 {
	static int N;
	static int r, c;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		r = sc.nextInt();
		c = sc.nextInt();
		System.out.println(cut((int) Math.pow(2, N), 0));
	}

	private static int cut(int size, int d) {
		int half = size / 2;
		if (size == 1) {
			return d;
		}

		if (r < half && c < half) {
			return cut(half, d + (int) Math.pow(half, 2) * 0);

		} else if (r < half && c >= half) {
			c -= half;
			return cut(half, d + (int) Math.pow(half, 2) * 1);

		} else if (r >= half && c < half) {
			r -= half;
			return cut(half, d + (int) Math.pow(half, 2) * 2);

		} else if (r >= half && c >= half) {
			r -= half;
			c -= half;
			return cut(half, d + (int) Math.pow(half, 2) * 3);
		}

		return -1;
	}

}
