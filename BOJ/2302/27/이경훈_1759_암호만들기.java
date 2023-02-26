package com.ssafy._230225;

import java.util.Arrays;
import java.util.Scanner;

public class Main_1759_G5_암호만들기_이경훈 {
	static int[] alphaArray;
	static int[] alphaCandidate;
	static int L, C;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		L = sc.nextInt();
		C = sc.nextInt();
		alphaArray = new int[C];
		for (int i = 0; i < C; i++) {
			alphaArray[i] = sc.next().charAt(0);
		}
		Arrays.sort(alphaArray);
		alphaCandidate = new int[L];
		combi(0, 0);
	}

	private static void combi(int cnt, int start) {
		if (cnt == L) {
			if (isAble()) {
				for (int ch : alphaCandidate) {
					System.out.print((char) (ch));
				}
				System.out.println();
			}
			return;
		}

		for (int i = start; i < C; i++) {
			alphaCandidate[cnt] = alphaArray[i];
			combi(cnt + 1, i + 1);
		}
	}

	private static boolean isAble() {
		int length = alphaCandidate.length;
		int moum = 0;
		for (int ch : alphaCandidate) {
			if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
				moum++;
			}
		}
		if (moum < 1)
			return false;
		if (length - moum < 2)
			return false;
		return true;
	}
}
